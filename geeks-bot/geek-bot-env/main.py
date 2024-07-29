from flask import Flask, request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
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

    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)

    # displaying result
    msg = response.msg(f"--- Results for '{user_msg}' ---")
    for result in search:
        msg = response.message(result)
    
    return str(response)

if __name__ == "__main__":
    app.run()



