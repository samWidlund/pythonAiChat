import os
import requests
import json
from dotenv import load_dotenv

runScript = True

# load api key
load_dotenv()
API_TOKEN = os.environ.get("HF_TOKEN")
if not API_TOKEN:
    raise ValueError("please set the HF_TOKEN to valid Hugging Face API key in .env file.")

# fetch api
API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# run program loop
while runScript == True:
    start_string = input("do you want to enter a question? y/n: ")
    if start_string == "y":

        # inputs
        input_question = input("please enter your question: ") 
        print("input_question: " + input_question)

        # filter api input
        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": input_question
                }
            ],
            "model": "moonshotai/Kimi-K2-Instruct:together"
        })

        # filter api input
        pretty_str_response = json.dumps(response, indent=2)

        # print output
        print("current running model:", response["model"])
        print("response from Ai: \n"+ response["choices"][0]["message"]["content"])

    elif start_string == "n":
        print("until next time!")
        runScript = False 
        break