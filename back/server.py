import asyncpg
from fastapi import FastAPI
from models import PaginatedBooks, BookModel, AuthorModel

app = FastAPI()


def pg_to_python(rows):
    return [dict(row) for row in rows]

@app.get("/book")
async def get_books() -> PaginatedBooks:
    """
    Возвращает книги
    """
    conn = await asyncpg.connect('postgresql://books:books@localhost:5433/books')
    authors = pg_to_python(await conn.fetch('SELECT * FROM author;'))
    books = pg_to_python(await conn.fetch('SELECT * FROM book;'))
    tags = pg_to_python(await conn.fetch('SELECT * FROM tag;'))
    books_to_tags = pg_to_python(await conn.fetch('SELECT * FROM tags_to_book;'))

    for book in books:
        author_id = book.pop("author_id")
        for author in authors:
            if author.get("id") == author_id:
                book["author"] = author

        book['tags'] = []
        for i in books_to_tags:
            if i.get("book_id") == book.get("id"):
                for tag in tags:
                    if tag.get("id") == i.get("tag_id"):
                        book["tags"].append(tag.get("title"))

    print(books)

    return PaginatedBooks(
        skip=0,
        limit=10,
        books=books
    )
