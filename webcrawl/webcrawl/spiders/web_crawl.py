#import scrapy
import scrapy
from webcrawl.items import webcrawlItem
from webcrawl.settings import *
import time

class WebCrawl(scrapy.Spider):
    #the name of the spider
    name = "web"

    allowed_domains =['ocado.com']

    #the url of the first page that we want to scrape
    start_urls = ['https://www.ocado.com/browse/value-just-for-you-323660/everyday-savers-323640?clkInTab=Everyday%20Savers'] 

    def parse(self, response):
        

        #here we are looping thru the products and extracting the name price and url
        products = response.xpath("//ul[@class='fops fops-regular fops-shelf']//li")
        

        for product in products:
            web_item=webcrawlItem()
            web_item['name'] = product.xpath(".//h4[@class='fop-title']/span/text()").get(),
            web_item['weight']=product.xpath(".//span[@class='fop-catch-weight-inline']/text()").get(),
            web_item['price'] = product.xpath(".//span[@class='fop-price fop-value-delivered price-offer']/text()").get(),
            web_item['url'] = product.xpath(".//div[@class='fop-contentWrapper']/a/@href").get()


            yield web_item