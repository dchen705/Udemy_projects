import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.web.archive.org']
    start_urls = ['https://www.web.archive.org/web/20190313062620/https://www.tinydeal.com/it/specials.html']

    def parse(self, response):
      
      for listing in response.xpath("//ul[@class='productlisting-ul']/div/li"):

        yield{
          'name': listing.xpath(".//a[@class='p_box_title']/text()").get(),
          'link': listing.xpath(".//a[@class='p_box_img']/@href").get(),
          'discount_price': listing.xpath(".//div[@class='p_box_price']/span[@class='productSpecialPrice fl']/text()").get(),
          'full_price': listing.xpath(".//div[@class='p_box_price']/span[@class='normalprice fl']/text()").get()
        }

      next_page = response.xpath("//a[@class='nextPage']/@href").get()

      if next_page:
        yield scrapy.Request(url=next_page, callback=self.parse)

