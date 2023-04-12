from connectdb import *
from passlib.hash import sha256_crypt
mydb = con()

mycursor = mydb.cursor()

def loginf(email,psw):
    sql = "SELECT * from userdetails WHERE Email=%s"
    val = (email,)
    mycursor.execute(sql, val)
    data = mycursor.fetchall()

    if data[0][4] == psw:
        return True, data[0][0], data[0][2]
    else:
        return False, None, None
    
def a_login(email,psw):
    sql = "SELECT * from admindetails WHERE a_email=%s"
    val = (email,)
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    if sha256_crypt.verify(psw,data[0][2]):
        return True, data[0][0]
    else:
        return False,None