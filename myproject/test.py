# from passlib.hash import sha256_crypt

# password = sha256_crypt.encrypt("password")
# password2 = sha256_crypt.encrypt("password")

# print(password)
# print(password2)

# # print(sha256_crypt.verify("password", password2))

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACfcad04a9ee469e537d8e1f92b35858b5"
auth_token = "ba7ebbf3401cc7df8ed940156ff242e9"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello Nitin",
  from_="+15074172424",
  to="+353894679458"
)
print(message.sid)

# from datetime import datetime

# today = datetime.now()
# current_time = today.strftime('%Y-%m-%d %H:%M')
# print(current_time)