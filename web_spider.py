import os
import scrapy

class WebSpider(scrapy.Spider):
    name = "web_spider"
    allowed_domains = ['en.wikipedia.org']  # Limit crawling to Wikipedia
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']  # Starting URL
    max_pages = 10000  # Maximum number of pages to crawl

    def parse(self, response):
        # Extract content from the current page
        content = {
            'url': response.url,
            'title': response.css('title::text').get(),
            'body': response.css('p::text').getall()+ response.css('h1::text').getall() + response.css('h2::text').getall() + response.css('h3::text').getall(),
        }

        # Save content to file
        self.save_content(content)

        # Extract links from the current page and follow them if within max depth and max pages limit
        if response.meta.get('depth', 1) < 6 and self.max_pages > 0:
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

        # Construct file path using the URL
        file_name = f"{content['title'].replace(' ', '_')}.html"  # Include doc_id in the file name
        file_path = os.path.join(directory, file_name)

        # Write HTML content to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"<html><head><title>{content['title']}</title></head><body>")
            for paragraph in content['body']:
                f.write(f"<p>{paragraph}</p>")
            f.write("</body></html>")