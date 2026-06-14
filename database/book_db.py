from db_connection import get_connect
class BookDB:
    def __init__(self,):
        pass
    

    def create_book(self,title,author,genre):
        try:
            conn = get_connect()

            cursor = conn.cursor()

            cursor.execute("INSERT INTO books(title,author,genre)VALUES(%s,%s,%s);",(title, author, genre))

            return "add a book"
        
        except Exception as e:
            return f"you have exception {e}"
        
        finally:
            if conn:
                conn.commit()
                cursor.close()
                conn.close()

if __name__ == "__main__":
    b = BookDB()
    print(b.create_book("is a test","M.R.","other"))