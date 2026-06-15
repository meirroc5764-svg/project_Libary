from fastapi import APIRouter
from database.db_connection import logger

from database.book_db import BookDB
from database.member_db import Member

bdb = BookDB()
m = Member()

router = APIRouter()

@router.get("/reports/summary",status_code=200)
def summary():
    logger.info("take a data...")
    total_books = bdb.books_total_count()
    avalibale_books = bdb.count_available_books()
    currently_borrowed = bdb.count_borrowed_books()
    active_members = m.count_active_members()
    logger.info("return a data from user")
    return {"total_books":total_books, "avalibale_books":avalibale_books, "currently_borrowed":currently_borrowed, "active_members":active_members}

@router.get("/reports/books-by-genre",status_code=200)
def count_genre():
    logger.info("will count a genre...")
    all_genre = bdb.count_by_genre()
    logger.info("return count genre")
    return all_genre

@router.get("/reports/top-member")
def top_member():
    logger.info("will count a top member...")
    the_member = m.get_top_member()
    logger.info("return top member")
    return the_member

