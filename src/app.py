from helper.openai_api import text_complition
from helper.twilio_api import send_message


from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


#default route to check for simple working

@app.route('/')
def home():
    return 'Its working!'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incoming parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Make request to openai
        result = text_complition(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200 #http ok response status
