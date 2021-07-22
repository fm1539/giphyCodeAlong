# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import os
import requests

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
@app.route('/gif', methods=["GET", "POST"])
def gif():
    API_KEY = "MGBOzorZpu01A1c5pO1CH6bwi0RJmEOe"
    URL = "http://api.giphy.com/v1/gifs/trending?api_key=" + API_KEY + "&limit=25"
    results = requests.get(URL).json()
    #return results
    return render_template('results.html', results=results)	