from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

from database.book_db import BookDB
bdb = BookDB()

router = APIRouter()

class BooksModel(BaseModel):
    title: str
    author: str
    genre: str

@router.post("/books",status_code=201)
def create_a_book(body:BooksModel):
    try:
        book = bdb.create_book(body.title,body.author,body.genre)
        if not book:
            raise HTTPException(status_code=422,detail="not good enter")
        return {"message":book}
    
    except Exception as e:
        raise HTTPException(status_code=401,detail=(e))



