from connectdb import *



def delex(id):
    mydb = con()
    mycursor = mydb.cursor()
    sql = "DELETE from expense WHERE `id`=%s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()