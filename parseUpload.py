import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def upload(newString):
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

        mysql_insert_query = "UPDATE crypto set crypto = '" + newString + "' WHERE id=1"
        cursor = connection.cursor()
        cursor.execute(mysql_insert_query)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failure to upload".format(error))
    finally:
        if connection.is_connected():
            connection.close()
    return "Key \n" + newString + " \nUploaded to database successfully"
