import os
from os.path import join, dirname

from dotenv import load_dotenv

from openai import OpenAI

dotenv_path = os.path.join(os.path.abspath(os.path.join(dirname(__file__),os.pardir,os.pardir, '.env')))

load_dotenv(dotenv_path)


def key():
    key = os.environ.get("key")
    print(key)

    return key

def endpoint():
    endpoint = os.environ.get("endpoint")
    print(endpoint)
    return endpoint

def llmKey():

    client = OpenAI(
    api_key=os.environ.get("LLM_API_KEY")
        )

    return client


