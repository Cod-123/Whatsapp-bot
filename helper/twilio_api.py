import os
from twilio.rest import Client #

#loads environent variables frm .env file
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token) #instance of class Client to make req


def send_message(to: str, message: str) -> None: 
    '''
    Parameters:
        - from : is frm the whatsapp no: +14.. used by twilio api
        to(str): sender whatsapp number in the general phone no format taken as str i/p
        - message(str): text message to send

    Returns:
        - None
    '''

    #underscore obj retuned since its not used for storing
    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )
