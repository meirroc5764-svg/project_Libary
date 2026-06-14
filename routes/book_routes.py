from fastapi import APIRouter,HTTPException
from pydantic import BaseModel


router = APIRouter()

class BooksModel(BaseModel):
    title: str
    author: str
    genre: str

@router.post("/books")
def create_a_book(body:BooksModel):
    pass