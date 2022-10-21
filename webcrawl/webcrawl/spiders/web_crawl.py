#import scrapy
import scrapy
from webcrawl.items import WebcrawlItem

class WebCrawl(scrapy.Spider):
    #the name of the spider
    name = "web"

    allowed_domains =['ocado.com']

    #the url of the first page that we want to scrape
    start_urls = ['https://www.ocado.com/browse/value-just-for-you-323660/everyday-savers-323640?clkInTab=Everyday%20Savers'] 

    def parse(self, response):
        web_item=WebcrawlItem()

        #here we are looping thru the products and extracting the name price and url
        products = response.xpath("//div[@class='fop-contentWrapper']")
        for product in products:
            
            web_item['name']= product.xpath("//h4[@class='fop-title']/span/text()").extract(),
            # web_item['weight']=product.xpath("//span[@class='fop-catch-weight-inline']/text()"),
            web_item['price'] =product.xpath("//span[@class='fop-price fop-value-delivered price-offer']/text()").extract(),
            web_item['url']= product.xpath("//div[@class='fop-contentWrapper']/a/@href").extract()

        yield web_item
            

