from connectdb import *

mydb = con()

mycursor = mydb.cursor()
def register(email,pno,username,psw):
    sql = "INSERT INTO userdetails (email,pno,username,password) VALUES (%s, %s, %s, %s)"
    val = (email,pno,username,psw)
    mycursor.execute(sql, val)
    mydb.commit()