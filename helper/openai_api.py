import os
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text complteion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dictionary as a resutl
    '''
    try:
        response = openai.Completion.create(
            model='text-davinci-003', #text model suitable for providing accurate answers to a good extent
            prompt=f'Human: {prompt}\nAI: ', #prompt format
            temperature=0.9,
            max_tokens=150, #max lim for no fo tokens/words ro be generated

            top_p=1,              
            frequency_penalty=0, #these 3 terms refer to penalty terms induced tat is higher values generates less repeating words as
              # well as maintains relevance to the context
            presence_penalty=0.6,

            stop=['Human:', 'AI:'] #stops the req
        )
        return { # a successful response is returned
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except: #empty response upon a failure
        return {
            'status': 0,
            'response': ''
        }
        