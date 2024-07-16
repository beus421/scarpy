# Sigma Spider
# goes into every book and scraps data
# for a better understaing check simpSpider.py

# import scrapy
#
# class my_book_scaper(scrapy.Spider):
#     name = 'sigma_spidy'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['https://books.toscrape.com/']
#
#     # scraps data from the main page
#     def parse(self,response):
#
#         # A list that contains all the books in a page
#         books = response.css('artice.product_pod')
#
#         # loops through all the books in the page
#         for book in books:
#             rel_url = response.css('h3 a::attr(href)').get()
#             if rel_url is not None:
#                 if 'catalogue/' in rel_url:
#                     book_url = 'https://books.toscrape.com/' + rel_url
#                 else:
#                     book_url = 'https://books.toscrape.com/catalogue/' + rel_url
#                 # runs the 'parse_page' function on each book in the list
#                 yield response.follow(book_url, callback=self.parse)
#
#         # moves to the next page
#         next_page = response.css('.next a::attr(href)').get()
#         if next_page is not None:
#             if 'catalogue/' in next_page:
#                 next_pg_url = 'https://books.toscrape.com/' + next_page
#             else:
#                 next_pg_url = 'https://books.toscrape.com/catalogue/' + next_page
#             yield response.follow(next_pg_url, callback=self.parse)
#
#     # Scrapes data from the book page
#     def page_parse(self, response):
#         table_rows = response.css('.table tr')
#         yield {
#             'URL': response.url,
#             'TITLE': response.css('.product_main h1::text').get(),
#             'PRODUCT TYPE': table_rows[1].css('td::text').get(),
#             'PRICE(INCL. TAX)': table_rows[3].css('td::text').get(),
#             'TAX': table_rows[4].css('td::text').get(),
#             'AVAILABILITY': table_rows[5].css('td::text').get(),
#             'REVIEW': table_rows[6].css('td::text').get(),
#             'STARS': response.css('p.star-rating').attrib['class'],
#             # we'll get this using the 'xpath' notation
#             'CATEGORIES': response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li["
#                                          "1]/a/text()").get(),
#             'DESCRIPTION': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
#         }
#
#         # Debugging print statements to track the spider's progress
#         self.log(f"Scraped data from: {response.url}")
#         self.log(f"Title: {response.css('.product_main h1::text').get()}")

# chatgpt:-

# import scrapy
from scrapping.items import BookItem  # Adjust the import according to your project structure


class MyBookScraper(scrapy.Spider):
    name = 'sigma_spidy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        # A list that contains all the books on the page
        books = response.css('article.product_pod')

        # Loops through all the books on the page
        for book in books:
            rel_url = book.css('h3 a::attr(href)').get()
            if rel_url:
                if not rel_url.startswith('catalogue/'):
                    rel_url = 'catalogue/' + rel_url
                book_url = response.urljoin(rel_url)
                # Runs the 'page_parse' function on each book in the list
                yield response.follow(book_url, callback=self.page_parse)

        # Moves to the next page
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def page_parse(self, response):
        table_rows = response.css('.table tr')

        # Creating an instance of BookItem and populating it
        book_item = BookItem()
        book_item['url'] = response.url
        book_item['title'] = response.css('.product_main h1::text').get()
        book_item['product_type'] = table_rows[1].css('td::text').get()
        book_item['price_incl_tax'] = table_rows[3].css('td::text').get()
        book_item['tax'] = table_rows[4].css('td::text').get()
        book_item['availability'] = table_rows[5].css('td::text').get()
        book_item['review'] = table_rows[6].css('td::text').get()
        book_item['stars'] = response.css('p.star-rating').attrib['class'].split()[-1]
        book_item['categories'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()

        yield book_item

        # Debugging print statements to track the spider's progress
        self.log(f"Scraped data from: {response.url}")
        self.log(f"Title: {book_item['title']}")

# To run the spider and store output in a CSV file
# Use the following command in the terminal:
# scrapy crawl sigma_spidy -o books.csv -t csv
