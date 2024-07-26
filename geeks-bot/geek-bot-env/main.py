from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

incoming_msg = request.values.get('Body', '').lower()

response = MessagingResponse()
msg = response.message()
msg.body('this is the response/reply  from the bot.')

# chatbot logic
def bot():
    user_msg = request.values.get('Body', '').lower()