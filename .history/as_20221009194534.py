# -*- coding: utf-8 -*-
"""Research Paper Abstract  Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pcls0XEeC5oU8Zsnc2-HfYYl2vDJqS8C

# **Scrape PubMed**
>  simple scraper to scrape pub med and get title abstract and keywords to csv file.
"""

# Imports
import pandas as pd
import requests
import json
import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess

# Add pubmed URL to scrape
TITLE = 'PubMed' # enter a title for your job

# Xpath variables to scrape html elements
# get_title = '//*a[@data-ga-category="result_click"]/text()' # get title

# run spider and crawl pubmed
class PubMedSpider(Spider):
    name = 'pubmedScraper'
    start_urls = [
        'https://pubmed.ncbi.nlm.nih.gov/?term=electronic+nose+early+detection+machine+learning&format=abstract&size=200',
    ]

    custom_settings = {
            'FEED_FORMAT': 'csv',
            'FEED_URI': TITLE + '_data.csv', #'Rename current working data set',
            }

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        # yield request

    def parse(self,response):
        title = 'header/div[1]/h1/a'
        for q in response.xpath('//article/' + title):
            print(q.response.xpath('//article/header/div[1]/h1/a/text()').get())
            yield {
                'title': q.xpath('text()').get(),
            }
        abstract = '/div[1]/div/p'
        for r in response.xpath('//article' + abstract):
            print (r.xpath('text()').get())
            yield {
                'abstract': r.xpath('text()').get(),
            }
#             }}
# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[3]/article/div[1]/div
# # /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[2]/article
# # /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[3]
# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[3]/article
        #    article/div[1]/div/p
        # for s in response.xpath('//article/'):
        #     yield {
        #         'keywords': s.xpath('div[1]/p/strong/text()[1]').get(),
        #     }

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PubMedSpider)
    process.start()





