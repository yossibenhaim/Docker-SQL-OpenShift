import mysql.connector

class DAL:

    def __init__(self):
        self.mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            database="data-loder")

    def connect(self):
        self.my_cursor = self.mysql_conn.cursor()

    def get_query(self,query,value = ""):
        self.connect()
        self.my_cursor.execute(query,value)
        my_result = self.my_cursor.fetchall()
        people = []
        for i in my_result:
            people.append(i)
        return people

    def get_all_data(self):
        query = "select * from pepole"
        return self.get_query(query)
