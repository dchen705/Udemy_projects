gimport scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    
    start_urls = ['http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='lister-item-content']/h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
        yield {
          'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
          'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
          'rating': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
          'url': response.url,
        }

   

  