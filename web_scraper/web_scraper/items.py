```python
import scrapy

class SafepinsItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_description = scrapy.Field()
    product_image = scrapy.Field()
    product_price = scrapy.Field()
    product_wholesale_price = scrapy.Field()
```