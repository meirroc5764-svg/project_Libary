from database.db_connection import ConnectDB

c= ConnectDB()

class BookDB:
    def __init__(self,):
        pass
    

    def create_book(self,title,author,genre):
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
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

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

    


if __name__ == "__main__":
    b = BookDB()
    # print(b.create_book("is a test","M.R.","other"))
    print(b.show_all())
    print(b.get_a_book_by_id(6))
    text = "title = its a up test"
    print(b.update_a_book(2,{"title":"its a up test"}))