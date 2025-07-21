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

# initial username input
username = input("please enter your username: ")
infoFile = username + ".txt"

# run program loop
while runScript == True:

    # initial inputs
    start_string = input("do you want to enter a question? y/n: ")

    if start_string == "y":

        # inputs
        print("username: " + username)
        input_question = input("please enter your question: ") 
        print("input_question: " + input_question)

        # save question in username based txt file
        if not os.path.exists(infoFile):
            with open(infoFile, "a") as f:
                f.write(input_question + "\n") # append question to file with line break
        elif os.path.exists(infoFile):
            with open(infoFile, "a") as f:
                f.write(input_question + "\n") # append question to file with line break

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

        # does not work !!
        remove_file = input("do you want to remove the saved chat info? y/n: ")
        if remove_file == "y":
            if os.path.exists(username + ".txt"):
                os.remove(username + ".txt")
                print("removed saved chat info.")
            else:
                print("no saved chat info found.")
        elif remove_file == "n":
            print("saved chat info will not be removed.")
        else:
            print("invalid input, saved chat info will not be removed.")

        runScript = False 
        break