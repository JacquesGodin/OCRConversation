# import the following modules
import json
import requests
from datetime import date

today = date.today()
print("Today's date:", today)

def get_fun_fact():
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use GET request
    response = requests.request("GET", url)
    
    # Load the request in json file
    data = json.loads(response.text)
    
    useless_fact = data["text"]
    
    return useless_fact

def rules(question):

    question_t1 = question.lower().replace(" ","")
    
    question_t2 = question_t1.splitlines( )
    question = question_t2[0]
    
    
    print(len(question))
    print(question)

    #if question == "what is the best country in the world?":
    #    answer = "Pangea!"
    #elif question == "what is DEL's mission?":
    #    answer = "To be a digital transformation tool box in order to prepare the future digital transformation leaders"
    if question == "whatdayistoday?":
        answer = f"Today is {today}"
        print(answer)
    elif question == "tellmeafunfact":
        answer = get_fun_fact()
        print(answer)
    
    else: 
        answer = "didn't understand"
    
    return answer
