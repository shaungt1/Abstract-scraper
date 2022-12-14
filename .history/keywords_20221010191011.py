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
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

# Add pubmed URL to scrape
TITLE = 'PubMed_Keywords' # enter a title for your job

# run spider and crawl pubmed
class PubMedSpider(Spider):
    name = 'pubmedScraper'
    start_urls = [
        'https://pubmed.ncbi.nlm.nih.gov/?term=electronic+nose+%28e-nose%29%2C+machine+learning+detection&size=100',
    ]

    custom_settings = {
            'FEED_FORMAT': 'csv',
            'FEED_URI': TITLE + '_data.csv', #'Rename current working data set',
            # FEED : {'_data.csv' : { 'format' : 'csv' } }
            }

    # def start_request(self):
    #     request = Request(url = self.start_urls, callback=self.parse)



    def parse(self, response):
        # get the title//*[@id="search-results"]/section[2]/div[1]/div/article[1]/div[2]/div[1]/a
        # title = response.css('h1.title::text').get()
        title = response.css('a').getall()
        # # get the abstract
        # abstract = response.css('div.abstract-content.selected::text').get()
        # # get the keywords
        # keywords = response.css('div.keywords-section::text').getall()
        # # get the authors
        # authors = response.css('span.authors-list__name::text').getall()
        # # get the journal
        # journal = response.css('div.journal-citation__journal::text').get()
        # # get the date
        # date = response.css('span.article-details__value::text').get()
        # # get the doi
        # doi = response.css('a.article-details__link::text').get()

        yield {
            'title': title,
            'abstract': abstract,
            'keywords': keywords,
            'authors': authors,
            'journal': journal,
            'date': date,
            'doi': doi,
        }
        # yield request
        # abstract = '/div[1]/div/p'
        # for r in response.xpath('//article' + abstract):
        #     print (r.xpath('text()').get())
        #     yield {
        #         'abstract': r.xpath('text()').get(),
            # }
# /html/body/main/div[9]/div[2]/section[2]/div[1]/div/div[3]/article/div[1]/p/text()

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PubMedSpider)
    process.start()





