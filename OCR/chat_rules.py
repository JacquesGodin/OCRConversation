# import the following modules
import json
import requests
from datetime import date

today = date.today()
print("Today's date:", today)

def get_fun_fact(_):
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use GET request
    response = requests.request("GET", url)
    
    # Load the request in json file
    data = json.loads(response.text)
    
    useless_fact = data["text"]


def rules(question):

    question = question.lower()

    if question == "what is the best business school out there?":
        answer = "NOVA SBE, from Carcavelos to the World!"
    elif question == "what is DEL's mission?":
        answer = "To be a digital transformation tool box in order to prepare the future digital transformation leaders"
    elif question == "what day is today?":
        answer = f"Today is {today}"
    #elif question == "tell me a fun fact":
    elif question == "the long way home":
        answer = get_fun_fact()