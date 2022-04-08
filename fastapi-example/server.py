from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn

app = FastAPI()

books = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/books/{book_id}/")
def read_book(book_id: int):
    return books.get(book_id, {"book_id": book_id})


@app.get("/books")
def read_books():
    return books


@app.post("/books")
def create_book(book: str):
    books[len(books)] = book
    return book


@app.exception_handler(Exception)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder(
            {"code": "internal_server_error", "message": "Internal Server Error"})
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
