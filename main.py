# -------------------------------------------------#
# Title: main.py
# Dev: Scott Luse
# Date: 07/22/2018
# Mashup random fact with Pig Latinizer
# -------------------------------------------------#

import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_pig(fact):
    # print(fact)
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', data=dict(input_text=fact))
    return response.url

@app.route('/')
def home():
    fact = get_fact().strip()
    body = get_pig(fact)
    return Response(response=body, mimetype="text/html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

