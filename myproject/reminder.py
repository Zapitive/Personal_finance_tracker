import arrow
from datetime import datetime

from celery import Celery
from twilio.rest import Client
from connectdb import *


account_sid = "ACfcad04a9ee469e537d8e1f92b35858b5"
auth_token = "ba7ebbf3401cc7df8ed940156ff242e9"
twilio_number = "+15074172424"
client = Client(account_sid, auth_token)

def reminder():
    mydb = con()
    mycursor = mydb.cursor()
    sql = "SELECT * from user_bills"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    today = datetime.now()
    current_time = today.strftime('%Y-%m-%d %H:%M:00')
    for i in data:
        jank = i[3].strftime('%Y-%m-%d %H:%M:00')
        if jank==current_time:
            sql1 = "SELECT * from userdetails WHERE `uid`=%s"
            val = (i[1],)
            mycursor.execute(sql1,val)
            users = mycursor.fetchall()
            client.messages.create(
                body=users[0][2]+" you have your "+i[2]+" due of amount "+str(i[4]),
                from_="+15074172424",
                to="+353894679458"
            )

