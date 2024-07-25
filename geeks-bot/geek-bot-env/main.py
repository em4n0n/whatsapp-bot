from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

imcoming_msg = request.values.get('Body', '').lower()