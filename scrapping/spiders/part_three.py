# # part 3
# # using the 'items.py' file inplace of 'yield'
#
# import scrapy
# #importing 'items.py' file
# from scrapping.scrapping.items import BookItem
#
# class MyBookScraper(scrapy.Spider):
#     name = 'sigma_spidy'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['https://books.toscrape.com/']
#
#     def parse(self, response):
#         # A list that contains all the books on the page
#         books = response.css('article.product_pod')
#
#         # Loops through all the books on the page
#         for book in books:
#             rel_url = book.css('h3 a::attr(href)').get()
#             if rel_url:
#                 if not rel_url.startswith('catalogue/'):
#                     rel_url = 'catalogue/' + rel_url
#                 book_url = response.urljoin(rel_url)
#                 # Runs the 'page_parse' function on each book in the list
#                 yield response.follow(book_url, callback=self.page_parse)
#
#         # Moves to the next page
#         next_page = response.css('.next a::attr(href)').get()
#         if next_page is not None:
#             next_page_url = response.urljoin(next_page)
#             yield response.follow(next_page_url, callback=self.parse)
#
#     def page_parse(self, response):
#         table_rows = response.css('.table tr')
#         book_items = BookItem()
#         book_items['URL'] = response.url,
#         book_items['TITLE'] = response.url
#         book_items['PRODUCT TYPE'] = response.url
#         book_items['PRICE (INCL. TAX)'] = response.url
#         book_items['TAX'] = response.url
#         book_items['AVAILABILITY'] = response.url
#         book_items['REVIEW'] = response.url
#         book_items['STARS'] = response.url
#         book_items['CATEGORIES'] = response.xpath
#         book_items['DESCRIPTION'] = response.url
#
#         yield book_items
#         # Debugging print statements to track the spider's progress
#         self.log(f"Scraped data from: {response.url}")
#         self.log(f"Title: {response.css('.product_main h1::text').get()}")
