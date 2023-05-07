from typing import List
from pydantic import BaseModel


class AuthorModel(BaseModel):
    id: int
    name: str
    born: int
    died: int


class BookModel(BaseModel):
    id: int
    title: str
    tags: List[str]
    year: int
    author: AuthorModel


class PaginatedBooks(BaseModel):
    skip: int
    limit: int
    books: List[BookModel]
