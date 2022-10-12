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
TITLE = 'Abstract_search' # enter a title for your job

# Xpath variables to scrape html elements
# get_title = '//*a[@data-ga-category="result_click"]/text()' # get title

# run spider and crawl pubmed
class PubMedSpider(Spider):
    name = 'pubmedScraper'
    start_urls = [
        'https://pubmed.ncbi.nlm.nih.gov/?term=electronic+nose+%28e-nose%29%2C+machine+learning+detection&format=abstract&size=100',
    ]

    custom_settings = {
            'FEED_FORMAT': 'csv',
            'FEED_URI': TITLE + '1' '_data.csv', #'Rename current working data set',
            }

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        # yield request

    def parse(self,response):
        Abstract = 'header/div[1]/h1/a'
        # for q in response.xpath('//article/' + title or abstract):
        #     yield {
        #         'title': q.xpath('text()').get(),
        #     }

        for q in response.xpath('//article/div/div/p'):
            yield {
                'Abstract': q.xpath('text()').get(),
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PubMedSpider)
    process.start()





