from web_poet import consume_modules
from web_poet.example import get_item

from books.items import Book

consume_modules("books.pages")

item = get_item(
    "http://books.toscrape.com/catalogue/the-exiled_247/index.html",
    Book,
)
print(item)