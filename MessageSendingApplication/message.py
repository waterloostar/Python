'''
Created on 2017 M08 25

@author: 69339
'''
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "###############"
# Your Auth Token from twilio.com/console
auth_token = "################"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+##########",
    from_="+########",
    body="Hello world!")

print(message.sid)
