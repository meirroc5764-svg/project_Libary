from mysql import connector
import logging

logging.basicConfig(
    level = logging.INFO,
    filename= "logs/app.log",
    format="%(asctime)s|%(levelname)s|%(name)s|%(message)s"
)
logger = logging.getLogger(__name__)




class ConnectDB:
    def __init__(self):
         self.host = "localhost"
         self.user = "root"
         self.password = "root"
         self.database = "Libary_db"
    
    def get_connect(self):
            return connector.connect(
            user = self.user,
            password = self.password,
            database = self.database,
            host = self.host
            )
c = ConnectDB()

def create_db():

    conn = c.get_connect()
    
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(50) NOT NULL,
                author VARCHAR(50) NOT NULL,
                genre ENUM("Fiction","Non-Fiction","Science","History","Other") NOT NULL,
                is_available BOOLEAN DEFAULT TRUE,
                id_member_by_borrowed INT DEFAULT NULL)""")
    
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS members(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL,
                is_active BOOLEAN NOT NULL,
                total_borrows INT NOT NULL)""")



    conn.commit()
    cursor.close()
    conn.close()

    return 



if __name__ == "__main__":
    c.get_connect()
    create_db()