'''
A set of models that improve on GPT-3.5 and can understand as well as 
generate natural language or code
'''

# build a python app that interacts with the user in the terminal for answering questions based on the information available on the internet

import requests
import json
from secrets_1 import OpenAI_API_KEY

def get_answer(user_input):
    url = 'https://api.openai.com/v1/chat/completions'

    # refer to documentation for refined parameters: https://platform.openai.com/docs/api-reference/chat/create
    request_body = {"role" : "user", "content" : user_input}

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OpenAI_API_KEY
    }

    # Send a GET request to the API with the question as a query parameter
    response = requests.post(url, data=json.dumps(request_body), headers=headers)
    
    if response.status_code == 200:
        # Parse the response JSON data
        data = json.loads(response.text)
        answer = data['answer']  # Extract the answer from the response
        return answer
    else:
        return "Sorry, I couldn't retrieve the answer at the moment."
    
    return response

def chat():
    print("Welcome to the Question Answering System!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Ask a question: ")
        
        if user_input.lower() == 'exit':
            break
        
        answer = get_answer(user_input)
        print("Answer:", answer)
        print()
    
    print("Goodbye!")

