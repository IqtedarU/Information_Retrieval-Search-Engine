from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from web_spider import WebSpider  # Adjust import statement

def main():
    # Create a CrawlerProcess instance with project settings
    process = CrawlerProcess(get_project_settings())

    # Run the spider
    process.crawl(WebSpider)
    process.start()  # the script will block here until the crawling is finished

if __name__ == "__main__":
    main()