
import mysql.connector
import make
from mysql.connector import Error
from mysql.connector import errorcode

currentKey = ""
alphabet = make.alphabet

def parse():
    #connection = mysql.connector.connect(host='localhost', database='encryption', user='root', password='')
    #DB INFO:
    #TABLE: crypto
    #COLLUMNS:
    #   id - int (auto increment off with a static value of 1)
    #   crypto - Long Text
    #!!!!!A ROW MUST BE INSERTED INTO DATABASE WITH AN ID OF 1 AND A PLACEHOLDER VALUE FOR CRYPTO!!
    #!!!!!APPLICATION WILL NOT WORK WITHOUT IT!!!!!!
    connection = mysql.connector.connect(host='', database='', user='', password='')
    
    try:

        mysql_select_query = "SELECT * FROM crypto"
        cursor = connection.cursor()
        cursor.execute(mysql_select_query)
        select = cursor.fetchall()
        for row in select:
            global currentKey
            currentKey = row[1]
        connection.commit()
    except mysql.connector.Error as error:
        print("Failure to retrieve")
    finally:
        if connection.is_connected():
            connection.close()
    return currentKey


def start():
    keyString = parse()
    keyList = []
    keyList[:0] = keyString
    x=0
    return keyList


start()