from database.db_connection import ConnectDB
from database.member_db import Member

c= ConnectDB()
m = Member()


class BookDB:
    def __init__(self,):
        pass
    

    def create_book(self,title,author,genre):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("INSERT INTO books(title,author,genre)VALUES(%s,%s,%s);",(title, author, genre))

            conn.commit()

            return "add a book"
        
        except Exception as e:
            return None
        
        finally:
            if conn:
                cursor.close()
                conn.close()


    
    def show_all(self,):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM books")

            data = cursor.fetchall()
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


        return data
    
    
    def get_a_book_by_id(self,id):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM books WHERE id = %s",(id,))

            my_data = cursor.fetchone()

            return my_data
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    
    
    def update_a_book(self,id,data):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()
            for key,value in data.items():
                query = f"UPDATE books SET {key} = %s WHERE id = %s"
                cursor.execute(query,(value,id))

                conn.commit()

            return "data update"
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    def the_book_is_vailibale(self,id):
        my_book = self.get_a_book_by_id(id)
        
        if not my_book:
            return None
        
        return my_book
        
    
    def set_available(self,id, val, member_id):
        conn = None
        book = self.the_book_is_vailibale(id)

        status_book = book["is_available"]

        if not book:
            return None
        
        if status_book == val:
            return "not posble update this val" 
        
        try:
            conn = c.get_connect()

            cursor = conn.cursor(dictionary=True)

            cursor.execute("UPDATE books SET is_available = %s ,id_member_by_borrowed = %s WHERE id = %s",(val,member_id,id))

            conn.commit()

            m.increment_borrows(member_id)

            return "update status book"
        
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()
             
    
    def books_total_count(self):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) AS total_books FROM books")

            all_books_sum = cursor.fetchone()

            return all_books_sum[0]
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()
        
    
    def count_available_books(self):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) AS available_books FROM books WHERE is_available = %s",(True,))

            all_books_sum = cursor.fetchone()

            return all_books_sum[0]
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def count_borrowed_books(self):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) AS borrowed_books FROM books WHERE is_available = %s",(False,))

            all_books_sum = cursor.fetchone()

            return all_books_sum[0]
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    
    def count_by_genre(self):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT genre,COUNT(*) AS count FROM books " \
            "GROUP BY genre")

            all_books_sum = cursor.fetchall()

            return all_books_sum
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()





if __name__ == "__main__":
    b = BookDB()
    # print(b.create_book("is a test","M.R.","other"))
    # print(b.show_all())
    # print(b.get_a_book_by_id(6))
    # text = "title = its a up test"
    # print(b.update_a_book(2,{"title":"its a up test"}))
    # print(b.set_available(1,False,1))
    print(b.books_total_count())
    print(b.count_available_books())
    print(b.count_borrowed_books())
    print(b.count_by_genre())