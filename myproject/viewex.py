from connectdb import *



def viewex(username,uid):
    mydb = con()
    mycursor = mydb.cursor()
    total = 0
    sql = "SELECT * from expense WHERE `username`=%s and `uid`=%s"
    val = (username,uid)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    for i in data:
        if i[3] == 'expense':
            total -= float(i[8])
        else:
            total += float(i[8])

    return data,total