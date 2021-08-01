from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title: str


app = FastAPI()

db = []


@app.get("/books")
def get_all_books():
    return db


@app.post("/books")
def add_a_book(book: Book):
    return db.append(book)

@app.get("/books/{book_id}")
def get_a_book(book_id: int):
    return db[book_id - 1]


@app.delete("/books/{book_id}")
def delete_a_book(book_id: int):
    return db.pop(book_id - 1)