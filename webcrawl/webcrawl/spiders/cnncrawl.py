import scrapy 

class CnnCrawl(scrapy.Spider):
    name ='domain'

    allowed_domains = ['https://cnn.com']

    start_urls=[
        'https://edition.cnn.com/specials/world/cnn-climate',
        'https://edition.cnn.com/business/tech'
    ]

    def parse(self,response):
        
        climate_headlines=response.xpath("//h3[@class='cd__headline']")
        for climate_headline in climate_headlines:
            yield{
                'climate_headline_text':climate_headline.xpath("//span[@class='cd__headline-text vid-left-enabled']").getall(),

                'climate_headline_author':climate_headline.xpath("//div[@class='cd__auxiliary']").getall(),

                'climate_headline_link':response.xpath("//h3[@class='cd__headline']/a/@href").getall()
            }
        # tech_vertical_headlines = response.xpath("//div[@class='container__field-links container_vertical-strip__field-links")
        tech_headlines =response.xpath("//div[@class='zone zone--t-light']")
        for tech_headline in tech_headlines:
            yield{
                'tech_vertical_headline' : tech_headline.xpath("//div[@class='container__headline container_vertical-strip__headline']").getall(),
                'tech_headline_with_images' : tech_headline.xpath("//div[@class='container__headline container_lead-plus-headlines-with-images__headline']").getall()}



        
        

        

        
