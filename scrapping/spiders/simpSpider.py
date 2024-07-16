import scrapy

# inherit the class 'Spider' from 'scrapy' package
class my_page_scraper(scrapy.Spider):
    # give your cute arachnid a name
    name = 'spidy'

    # tell the 'DOMAIN' that needs to be scraped
    # important so our crawler doesn't go outside our domain
    allowed_domains = ['books.toscrape.com']

    # tell the 'URL' where scraping starts
    start_urls = ['https://books.toscrape.com/']

    # parse function is called when the 'response' comes back
    def parse(self,response):

        # after trying some 'css' methods in ipython shell
        # you know how to use the 'css' selector

        # stores a 'tag' containing all the books is grabbed
        books = response.css('artice.product_pod')

        # no. of loops = no. of books
        for book in books:
            # 'yield' is like 'returning' an object
            # it contains 'key-value' pairs of our required values
            yield {
                'name': book.css('h3 a::text').get(),
                'price': book.css('p.product_pod .price_color'),
                'url': book.css('h3 a').attrib['href']
            }
        # nextPage = response.css('.next a::text').attrib['href'] or
        next_page = response.css('.next a::attr(href)').get()

        # if there is a tag for 'next page' button
        if next_page is not None:
            if 'catalogue/' in next_page:
                # url of website + url from 'next' btn = full next page url
                next_pg_url = 'https://books.toscrape.com/' + next_page
            else:
                # url of website(can be a little different so make sure) + url from 'next' btn = full next page url
                next_pg_url = 'https://books.toscrape.com/catalogue/' + next_page
                # if we get a 'response' from the 'next_pg_url'
                # run a function(callback) that will,
                # run the 'parse method' on the 'response object'
            yield response.follow(next_pg_url, callback=self.parse)

        # code is from chatGpt
        # if next_page is not None:
        #     next_pg_url = response.urljoin(next_page)
        #     self.log(f'Next page URL: {next_pg_url}')  # Debug log to check the next page URL
        #     yield response.follow(next_pg_url, callback=self.parse)

    # def closed(self, reason):
    #     item_count = self.crawler.stats.get_value('item_scraped_count')
    #     self.logger.info(f'Number of items scraped: {item_count}')
