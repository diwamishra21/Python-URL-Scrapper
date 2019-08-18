# -*- coding: utf-8 -*-
import scrapy


class ClinicaltrialSpider(scrapy.Spider):
    name = 'pythonscrapper'
    start_urls = [
        'https://clinicaltrials.gov/ct2/show/study/NCT04045704?rank=1',
        'https://clinicaltrials.gov/ct2/show/NCT04045704?rank=3',
        'https://clinicaltrials.gov/ct2/show/NCT04045717?rank=2',
        'https://clinicaltrials.gov/ct2/show/NCT04045691',
        'https://clinicaltrials.gov/ct2/show/NCT04045678',
        'https://clinicaltrials.gov/ct2/show/NCT04045665',
        'https://clinicaltrials.gov/ct2/show/NCT04045639',
        'https://clinicaltrials.gov/ct2/show/NCT04045626',
        'https://clinicaltrials.gov/ct2/show/NCT04045613',
        'https://clinicaltrials.gov/ct2/show/NCT04045717',
    ]

    def parse(self, response):
        for quote in response.css('div#wrapper'):
            yield {
                'Identifier': quote.css(".tr-column.tr-right > table tr:first-child > td::text").extract_first(),
                'Condition_or_Disease': quote.css("table.tr-data_table td:first-child > span:first-child::text").extract_first(),
            }
