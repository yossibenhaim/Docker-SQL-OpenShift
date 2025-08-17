import mysql.connector


class DAL:

    def __init__(self):
            self.host="mysql"
            self.user="myuser"
            self.password='mypassword'
            self.port=3306
            self.database="mydb"

    def connect(self):
        self.mysql_conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database)
        self.my_cursor = self.mysql_conn.cursor()

    def get_query(self,query,value = ""):
        self.connect()
        self.my_cursor.execute(query,value)
        result = self.my_cursor.fetchall()
        return result


    def get_all_data(self):
        query = "select * from mydb"
        result = self.get_query(query)
        self.close_conn()
        return result

    def close_conn(self):
        self.my_cursor.close()
        self.mysql_conn.close()
