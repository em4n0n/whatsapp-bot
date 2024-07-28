from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

incoming_msg = request.values.get('Body', '').lower() # Receive message from user

response = MessagingResponse()
msg = response.message()
msg.body('this is the response/reply from the bot.')

# chatbot logic
def bot():
    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse

    # User Query
    q = user_msg + "google.com"

    # list to store urls
    result = []
