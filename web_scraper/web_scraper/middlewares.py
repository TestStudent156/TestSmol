```python
from scrapy import signals
from scrapy.http import FormRequest

class WebScraperSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WebScraperDownloaderMiddleware:

    def process_request(self, request, spider):
        if request.url == 'https://www.safepins.eu/login':
            return FormRequest.from_response(
                response,
                formdata={'username': 'user', 'password': 'pass'},
                callback=spider.after_login
            )

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass
```