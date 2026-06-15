from fastapi import APIRouter

from database.book_db import BookDB
from database.member_db import Member

bdb = BookDB()
m = Member()

router = APIRouter()

@router.get("/reports/summary",status_code=200)
def summary():
    total_books = bdb.books_total_count()
    avalibale_books = bdb.count_available_books()
    currently_borrowed = bdb.count_borrowed_books()
    active_members = m.count_active_members()
    return {"total_books":total_books, "avalibale_books":avalibale_books, "currently_borrowed":currently_borrowed, "active_members":active_members}

@router.get("/reports/books-by-genre",status_code=200)
def count_genre():
    all_genre = bdb.count_by_genre()
    return all_genre

@router.get("/reports/top-member")
def top_member():
    the_member = m.get_top_member()
    return the_member

