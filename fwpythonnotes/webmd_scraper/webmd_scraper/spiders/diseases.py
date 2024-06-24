import scrapy

class WebMDSpider(scrapy.Spider):
    name = "diseases"
    start_urls = ['https://www.webmd.com/a-to-z-guides/health-topics']

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if '/a-to-z-guides/' in link:
                yield response.follow(link, self.parse_topic)

    def parse_topic(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'description': response.css('div.article-page.active-page data-page="1"').getall(),
            'symptoms': response.css('div.symptoms-section ul li::text').getall(),
            'causes': response.css('div.causes-section ul li::text').getall(),
            'treatments': response.css('div.treatments-section ul li::text').getall()
        }
