from web_poet import field, handle_urls, WebPage, Returns

from ..items import CategorizedBook, Book


@handle_urls("books.toscrape.com")
class BookPage(WebPage[Book]):

    @field
    async def title(self):
        return self.xpath("//h1/text()").get()


@handle_urls("books.toscrape.com")
class CategorizedBookPage(BookPage, Returns[CategorizedBook]):
    @field
    async def category(self):
        return self.css(".breadcrumb a::text").getall()[-1]