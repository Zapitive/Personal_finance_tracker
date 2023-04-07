from connectdb import *
mydb = con()

mycursor = mydb.cursor()

def abill(uid,bt,bd,ba):
    sql = "INSERT INTO user_bills (uid,bill_type,bill_due,bill_amt) VALUES (%s, %s, %s,%s)"
    val = (uid,bt,bd,ba)
    mycursor.execute(sql, val)
    mydb.commit()