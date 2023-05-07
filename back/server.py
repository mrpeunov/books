from fastapi import FastAPI
from models import PaginatedBooks

app = FastAPI()


@app.get("/book")
async def get_books() -> PaginatedBooks:
    """
    Возвращает книги
    """
    # return PaginatedBooks(
    #     limit=10,
    #     skip=0,
    #     books=[]
    # )
    return {
        "limit": 10,
        "skip": 0,
        "books": [
            {
                "id": 1,
                "title": "Горе от ума",
                "year": 1824,
                "tags": ["Комедия"],
                "author": {
                    "id": 1,
                    "name": "Грибоедов А.C.",
                    "born": 1795,
                    "died": 1829
                }
            },
            {
                "id": 2,
                "title": "Капитанская дочка",
                "year": 1836,
                "tags": ["Роман", "Повесть"],
                "author": {
                    "id": 2,
                    "name": "Пушкин А.C.",
                    "born": 1799,
                    "died": 1837
                }
            }
        ]
    }
