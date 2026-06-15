from database.db_connection import ConnectDB

c= ConnectDB()

class Member:
    def __init__(self):
        pass

    def create_members(self,data):
        conn = None
        try: 
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("INSERT INTO members(name, email, is_active, total_borrows) " \
            "VALUES(%s,%s,%s,%s)",(data["name"],data["email"],data["is_active"],0))

            conn.commit()

        finally:
            if conn:
                cursor.close()
                conn.close()

    
    def show_all(self):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM members")

            all_data = cursor.fetchall()
            
            if not all_data:
                return None
            
            return all_data
        except Exception as e:
            raise e
        
        finally:
            if conn:
                cursor.close()
                conn.close()

   
    
    def get_member_by_id(self,id):
        conn = None
        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM members WHERE id = %s",(id,))

            my_member = cursor.fetchone()

            return my_member
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    
    
    def change_by_id(self,id, data):
        
        if not self.get_member_by_id(id):
            return None
        
        conn = None
        
        try:
            conn = c.get_connect()

            cursor = conn.cursor()
            for key,value in data.items():
                update=f"UPDATE members SET {key} = %s WHERE id = %s"
                cursor.execute(update,(value,id))
                conn.commit()
            return "update member"
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


    def diactivate_by_id(self,id):
        
        if not self.get_member_by_id(id):
            return None
        
        conn = None
        
        try:
            conn = c.get_connect()

            cursor = conn.cursor()
            
            update=f"UPDATE members SET is_active = %s WHERE id = %s"
            cursor.execute(update,(False,id))
            
            conn.commit()
            
            return "diactivate a member"
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()

    
    def activate_by_id(self,id):
        
        if not self.get_member_by_id(id):
            return None
        
        conn = None
        
        try:
            conn = c.get_connect()

            cursor = conn.cursor()
            
            update=f"UPDATE members SET is_active = %s WHERE id = %s"
            cursor.execute(update,(True,id))
            
            conn.commit()
            
            return "activate a member"
        
        except Exception as e:
            raise e

        finally:
            if conn:
                cursor.close()
                conn.close()


    def increment_borrows(self,id):
        if not self.get_member_by_id(id):
            return None
        
        conn = None

        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT total_borrows FROM members WHERE id = %s",(id,))

            num_active = cursor.fetchone()

            new_num = num_active[0] + 1

            cursor.execute("UPDATE members SET total_borrows = %s WHERE id = %s",(new_num,id))

            conn.commit()

            return "adds 1 to total_borrows"
        
        except Exception as e:
            raise e

    
    def count_active_members(self):
        
        conn = None

        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM members WHERE is_active = %s",(True,))

            the_sum = cursor.fetchone()

            
            return the_sum
        except Exception as e:
            raise e


    def get_top_member(self):
        
        conn = None

        try:
            conn = c.get_connect()

            cursor = conn.cursor()

            cursor.execute("SELECT MAX(total_borrows) FROM members")

            max_total = cursor.fetchone()
            
            cursor.execute("SELECT id,name FROM members WHERE total_borrows = %s",(max_total[0],))

            the_top_member = cursor.fetchall()

            return the_top_member
        except Exception as e:
            raise e







if __name__ == "__main__":
    m = Member()
    # new_dict = {"name":"Meir", "email":"rotitar@", "is_active":True}
    # m.create_members(new_dict)
    print(m.show_all())
    # print(m.get_member_by_id(6))
    # print(m.change_by_id(1,{"name": "roch"}))
    # print(m.diactive_by_id(1))
    print(m.increment_borrows(1))
    # print(m.count_active_members())
    print(m.get_top_member())
