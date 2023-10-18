```python
import scrapy
from scrapy.http import FormRequest
from ..items import SafepinsItem

class SafepinsSpider(scrapy.Spider):
    name = 'safepins'
    start_urls = ['http://safepins.eu/login']

    def parse(self, response):
        return FormRequest.from_response(response,
                                         formdata={'username': 'your_username', 'password': 'your_password'},
                                         callback=self.after_login)

    def after_login(self, response):
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        else:
            return scrapy.Request(url="http://safepins.eu/",
                                  callback=self.parse_pages)

    def parse_pages(self, response):
        items = SafepinsItem()

        all_div_products = response.css('div.product')

        for products in all_div_products:
            product_name = products.css('.product-name::text').extract()
            product_price = products.css('.product-price::text').extract()

            items['product_name'] = product_name
            items['product_price'] = product_price

            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse_pages)
```