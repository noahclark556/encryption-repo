import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def upload(newString):
    #connection = mysql.connector.connect(host='localhost', database='encryption', user='root', password='')
    connection = mysql.connector.connect(host='remotemysql.com', database='7le0c8z5UM', user='7le0c8z5UM', password='fd4uKfNxvp')
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
