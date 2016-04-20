from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "AC6720dab93f0bfd755e38d5194e80889a"
auth_token  = "cd0a979c74fdecb33d478f3ef2eca1bb"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="sup",
  to="+18317103519",    # Replace with your phone number
  from_="+12014821837") # Replace with your Twilio number
print message.sid