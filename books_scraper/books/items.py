from attrs import define
from typing import Optional


@define
class Book:
    title: str
    

@define
class CategorizedBook(Book):
    category : str
    category_rank : Optional[int] = None