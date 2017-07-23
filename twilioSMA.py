from twilio import rest

# put your own credentials here
account_sid = "AC3079e5e522d4c6507eda2079c39ee8e7"
auth_token = "c73bde7ad625ed6b45da02xxxxxxxxxxx"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+1xxx62xx8825",
    from_="+1559206xxxx",
    body="texttexttext?")

print(message.sid)
