import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port=3306,
    database="mydb"
)
my_cursor = myDB.cursor()


def get_query(query,value = ""):
    my_cursor.execute(query,value)
    my_result = my_cursor.fetchall()
    for i in my_result:
        print(i)