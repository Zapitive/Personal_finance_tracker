from passlib.hash import sha256_crypt
from connectdb import *
mydb = con()

mycursor = mydb.cursor()

def admin():
    sql = "SELECT * from userdetails"
    mycursor.execute(sql)
    users = mycursor.fetchall()

    return users
