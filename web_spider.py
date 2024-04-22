import os
import scrapy

class WebSpider(scrapy.Spider):
    name = "web_spider"
    allowed_domains = ['en.wikipedia.org']  # Limit crawling to Wikipedia
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']  # Starting URL
    max_pages = 10000  # Maximum number of pages to crawl
    max_depth = 6

    def parse(self, response):
        # Extract content from the current page
        content = {
            'url': response.url,
            'title': response.css('title::text').get(),
            'body': response.css('p::text').getall()+ response.css('h1::text').getall() + response.css('h2::text').getall() + response.css('h3::text').getall() + response.css('h4::text').getall() +
            response.css('h5::text').getall() +
            response.css('h6::text').getall() +
            response.css('li::text').getall() +  # List items
            response.css('.mw-parser-output > *::text').getall(),
        }

        # Save content to file
        self.save_content(content)

        # Extract links from the current page and follow them if within max depth and max pages limit
        if response.meta.get('depth', 1) < self.max_depth and self.max_pages > 0:
            for link in response.css('a::attr(href)').getall():
                if self.max_pages <= 0:
                    break
                self.max_pages -= 1
                yield response.follow(link, callback=self.parse, meta={'depth': response.meta.get('depth', 1) + 1})

    def save_content(self, content):
        # Create a directory to store HTML files if it doesn't exist
        directory = 'C:/website_content'
        if not os.path.exists(directory):
            os.makedirs(directory)


        file_name = f"{content['title'].replace(' ', '_')}.html"
        text_file_name = f"{content['title'].replace(' ', '_')}.txt"
        file_path = os.path.join(directory, file_name)
        text_file_path = os.path.join(directory, text_file_name)

        # Write URL to a separate text file
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(f"URL: {content['url']}\n")

        # Write HTML content to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"<html><head><title>{content['title']}</title></head><body>")
            for paragraph in content['body']:
                f.write(f"<p>{paragraph}</p>")
            f.write("</body></html>")
