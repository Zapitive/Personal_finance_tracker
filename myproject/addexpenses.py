from connectdb import *
mydb = con()

mycursor = mydb.cursor()

def addex(eid,username,exp,date,category,note,cur,amt):
    sql = "INSERT INTO expense (uid, username, expense,ex_date,category,note,currency,amount) VALUES (%s, %s, %s,%s, %s, %s, %s, %s)"
    val = (eid, username, exp,date,category,note,cur,amt)
    mycursor.execute(sql, val)
    mydb.commit()