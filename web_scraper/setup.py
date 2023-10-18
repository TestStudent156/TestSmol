from setuptools import setup, find_packages

setup(
    name='web_scraper',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = web_scraper.settings']},
    install_requires=[
        'Scrapy',
    ],
)