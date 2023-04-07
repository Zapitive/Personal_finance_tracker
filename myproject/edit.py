from connectdb import *



def edex(exp,date,category,note,cur,amt,id):
    mydb = con()
    mycursor = mydb.cursor()
    sql = "UPDATE expense SET expense = %s , ex_date= %s,category=%s,note=%s,currency=%s,amount=%s WHERE id = %s;"
    val = (exp,date,category,note,cur,amt,id)
    print(exp,date,category,note,cur,amt,id)
    mycursor.execute(sql,val)
    mydb.commit()