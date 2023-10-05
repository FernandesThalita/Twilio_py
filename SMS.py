

#importando o twilio
from twilio.rest import Client

#minha conta
Account_SID = 'your account sid'

#meu token
Auth_Token = 'your auth token'

client = Client(Account_SID, Auth_Token)

client.messages.create(from_="one valid number", body="body message",to="other valid number")
