import requests
import scrapy
import json
from os import path
import logging


class Interspeech2019Spider(scrapy.Spider):
    name = "interspeech15"

    ustom_settings = {
    # WARNING, INFO, DEBUG
    'LOG_LEVEL': 'INFO',
    }

    start_urls =[
        'https://www.isca-speech.org/archive/interspeech_2015/'
    ]

    def gen_scrapy_response(url):
        # define user agent to simulate interactive user
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        req = requests.get(url, headers={ "user-agent": user_agent })
        return scrapy.http.TextResponse(req.url, body=req.text, encoding='utf-8')

    def parse(self, response):
        for container in response.css("center center"):
            for paragraph in container.css("p"):
                if paragraph: 
                    nextpage = paragraph.css("a::attr('href')").extract_first()           
                    yield response.follow(str(nextpage), callback=self.parse_data)

    
    def parse_data(self,response):
        title = ''
        abstract = ''
        for title_tex in response.xpath('//center/h2//text()').extract():
            title +=  title_tex
        author = response.xpath('normalize-space(//center/h3/text())').extract_first()
        author = author.split(',')
        for abstract_text in response.xpath('//p[not(@align="left")]//text()').extract():
            abstract +=  abstract_text



        item = dict(
            title = title,
            abstract = abstract,
            author = author
        )

        yield item