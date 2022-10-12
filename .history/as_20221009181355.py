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
for
get_title = '//div[{i}]/article/header/div[1]/h1/a/text()' # get title
# get_abstract = '//*[@id="P570"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/text()'
# get_keywords = '//*[@id="P570"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/text()'

# //*[@id="search-results"]/section[2]/div[1]/div/div[2]/article
# # //*[@id="search-result-1-1-full-view-heading"]/h1/a
# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[2]/article/header/div[1]/h1/a
# //*[@id="search-result-1-1-full-view-heading"]/h1/a
# //*[@id="search-results"]/section[2]/div[1]/div/div[2]
# //*article/header/div[1]/h1/a

# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[2]/article/header/div[1]/h1/a
# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[3]/article/header/div[1]/h1/a
# run spider and crawl pubmed
class PubMedSpider(Spider):
    name = 'pubmedScraper'
    start_urls = [
        'https://pubmed.ncbi.nlm.nih.gov/?term=electronic+nose+early+detection+machine+learning&format=abstract&size=200',
    ]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
    custom_settings = {
            'FEED_FORMAT': 'csv',
            'FEED_URI': TITLE + '_data.csv', #'Rename current working data set',
            }

    # with open('poi_scraper\spiders\wikidata_Q_Value_892022.csv') as file:
    #     start_urls = [line.strip() for line in file]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        # yield request

    def parse(self,response):
        # Xpath variables,
        GET_TITLE = response.xpath(get_title).get(),
        # GET_ABSTRACT = response.xpath(get_abstract).get()
        # GET_KEYWORDS = response.xpath(get_keywords).get()

        # Get the wikidata response
        yield {
                    'GET_TITLE': GET_TITLE,
                    # 'GET_ABSTRACT': GET_ABSTRACT,
                    # 'GET_KEYWORDS': GET_KEYWORDS,

            }
    # pass

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PubMedSpider)
    process.start()





