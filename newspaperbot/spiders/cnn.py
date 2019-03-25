# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from newspaperbot.items import NewspaperbotItem

class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['https://edition.cnn.com/sport', 'https://edition.cnn.com/entertainment', 'https://edition.cnn.com/health', 'https://edition.cnn.com/business']

    def parse(self, response):
        # Goto every post and return the request to parse_article
        articles = response.css('h3.cd__headline a::attr(href)').extract()
        cate = response.url.split('/')[-1]
        for article in articles:
            url = urljoin(response.url, article)
            yield scrapy.Request(url, callback=self.parse_article, meta={'cate': cate})

    def parse_article(self, response):
        # Extract all title, summary, content, type and save to cnn.json
        article = NewspaperbotItem()
        string_list = response.css('.zn-body__paragraph::text').extract()
        content = ''.join(subtext for subtext in string_list)

        article['title'] = response.css('h1.pg-headline::text').extract_first()
        if article['title'] != None:
            article['cate'] = response.meta['cate']
            article['content'] = content.replace('\"', '')

            yield article
