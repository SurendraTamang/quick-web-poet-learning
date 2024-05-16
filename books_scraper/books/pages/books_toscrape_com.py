from web_poet import field, handle_urls, WebPage

from ..items import Book


@handle_urls("books.toscrape.com")
class BookPage(WebPage[Book]):

    @field
    async def title(self):
        return self.xpath("//h1/text()").get()