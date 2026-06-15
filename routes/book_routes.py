from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import Literal
from database.db_connection import logger

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
    logger.info("start create...")
    book = bdb.create_book(body.title, body.author, body.genre)
    if not book:
        logger.error("user enter not valibol")
        raise HTTPException(status_code=422,detail="not good enter")
    logger.info("create successfully")
    return {"message":book}
    

@router.get("/books",status_code=200)
def get_all_books():
    
    try:
        logger.info("take all data...")
        all_data = bdb.show_all()
        logger.info("return to user all data")
        return all_data
    
    except:
        logger.error("not found a data")
        raise HTTPException(status_code=404,detail="not found")



@router.get("/books/{id}",status_code=200)
def get_book_by_id(id:int):
    my_data = bdb.get_a_book_by_id(id)
    logger.info("searches book by ID...")
    if not my_data:
        logger.error("not found a data by id")
        raise HTTPException(status_code=404,detail="not found a book with this id")
    logger.info("return to user a book by id")
    return my_data

@router.put("/books/{id}",status_code=200)
def update_book(id:int,body:BooksUpModel):
    logger.info("start update data...")
    my_update = bdb.update_a_book(id,body.model_dump(exclude_none=True))
    
    if not my_update:
        logger.error("false update not found a data to update")
        raise HTTPException(status_code=404,detail="not found a book")
    logger.info("update finish successfully")
    return {"message":my_update}

@router.put("/books/{id}/borrow/{member_id}",status_code=200)
def set_available_borrow(id:int, member_id:int):
    logger.info("searches by ID...")
    if not bdb.get_a_book_by_id(id):
        logger.error("not found a data by id")
        raise HTTPException(status_code=404,detail="not fouund a book")
    logger.info("start update status borrow...")
    update = bdb.set_available(id, False, member_id)
    logger.info("update status borrow successfully")
    return{"message":update}

@router.put("/books/{id}/return/{member_id}",status_code=200)
def set_available_return(id:int):
    logger.info("searches by ID...")
    if not bdb.get_a_book_by_id(id):
        logger.error("not found a data by id")
        raise HTTPException(status_code=404,detail="not fouund a book")
    logger.info("start update status return...")
    update = bdb.set_available(id, True, None)
    logger.info("update status return successfully")
    return{"message":update}