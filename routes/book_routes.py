from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal

from database.book_db import BookDB
bdb = BookDB()

router = APIRouter()

class BooksModel(BaseModel):
    title: str
    author: str
    genre: Literal["Fiction","Non-Fiction","Science","History","Other"]

class BooksUpModel(BaseModel):
    title: str|None = None
    author: str|None = None
    genre: Literal["Fiction","Non-Fiction","Science","History","Other"]|None = None


@router.post("/books",status_code=201)
def create_a_book(body:BooksModel):
    book = bdb.create_book(body.title, body.author, body.genre)
    if not book:
        raise HTTPException(status_code=422,detail="not good enter")
    return {"message":book}
    

@router.get("/books",status_code=200)
def get_all_books():
    
    try:
        all_data = bdb.show_all()
        return all_data
    
    except:
        raise HTTPException(status_code=404,detail="not found")







@router.get("/books/{id}",status_code=200)
def get_book_by_id(id:int):
    my_data = bdb.get_a_book_by_id(id)
    if not my_data:
        raise HTTPException(status_code=404,detail="not found a book with this id")
    return my_data

@router.put("/books/{id}",status_code=200)
def update_book(id:int,body:BooksUpModel):
    my_update = bdb.update_a_book(id,body.model_dump(exclude_none=True))
    
    if not my_update:
        raise HTTPException(status_code=404,detail="not found a book")
    
    return {"message":my_update}

@router.put("/books/{id}/borrow/{member_id}",status_code=200)
def set_available_borrow(id:int, member_id:int):
    if not bdb.get_a_book_by_id(id):
        raise HTTPException(status_code=404,detail="not fouund a book")
    
    update = bdb.set_available(id, False, member_id)
    return{"message":update}

@router.put("/books/{id}/return/{member_id}",status_code=200)
def set_available_return(id:int):
    if not bdb.get_a_book_by_id(id):
        raise HTTPException(status_code=404,detail="not fouund a book")
    
    update = bdb.set_available(id, True, None)
    return{"message":update}