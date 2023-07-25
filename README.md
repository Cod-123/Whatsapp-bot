# Whatsapp-bot

# WhatsApp-OpenAI Bot
this repository is a demo project on connecting Twilio and OpenAI to provide answers to all the users questions using OpenAI GPT-3. This is written in `Python` and served with `Flask`. This bot can only handle:
 text messgaes


# Steps for creation

 OpenAI API key
 Twilio project, to get an `Account SID` and `Auth Token` for that project, we will need this to make requests. 
 NGROK for local testing.

# Usage:
steps:
 create a `.env` file inside the root directory, create these environmental variables:
    ```
    TWILIO_ACCOUNT_SID=YOUR ACCOUNT SID
    TWILIO_AUTH_TOKEN=YOUR AUTH TOKEN
    OPENAI_API_KEY=YOUR OPENAI API KEY
    FROM=whatsapp:+14155238886
    ```
This FROM variable in the .env file is same for the Twilio WhatsApp Sandbox.
 create a virtual environment and activate it before installing the packages
 install all the required dependencies from the `requirements.txt` file
```python
pip install -r requirements.txt
```
 run the server with either of the following commands
```python
python run.py
```

 start NGROK engine on the same port as the python application is running.
 provide the NGROk urlon `Twilio WhatsApp Sandbox` for all incoming request.
 test the setup using your WhatsApp


