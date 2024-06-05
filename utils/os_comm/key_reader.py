import os
from os.path import join, dirname
import streamlit as st
from dotenv import load_dotenv

from openai import OpenAI

dotenv_path = os.path.join(os.path.abspath(os.path.join(dirname(__file__),os.pardir,os.pardir, '.env')))

load_dotenv(dotenv_path)


st.secrets["key"]

# os.environ["endpoint"] == st.secrets["endpoint"]


def key():
    key = st.secrets["key"]

    print(key)

    return key

def endpoint():
    endpoint = st.secrets["key"]

    print(endpoint)
    return endpoint

def llmKey():

    client = OpenAI(
    api_key=os.environ.get("LLM_API_KEY")
        )

    return client


