import requests
import os
import json
from pprint import pprint
from settings import TOKEN, DEFAULT_CHANNEL, SLACK_BASE_URL
token =TOKEN


def send_notification(text):
    payload = {"token":token, "channel":DEFAULT_CHANNEL, "text":text}
    responce = requests.post(SLACK_BASE_URL+"/chat.postMessage",
                                data=payload)
    responce.raise_for_status()
    return True
            
if __name__ =="__main__":
    text = input()
    pprint(send_notification(text))