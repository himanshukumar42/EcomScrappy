from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import psycopg2
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "HomePage File"


@app.route("/public/healthz")
def health():
    return "OK", 200


def scrape_url(url="https://www.jamesedition.com/cars"):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    quotes = []
    table = soup.find('div', attrs={'class': "ListingCard _initialized"})

    for row in table.findAll('div', attrs={'class': "ListingCard_price"}):
        quote = {}
        quote