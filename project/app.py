import requests
from bs4 import BeautifulSoup
import flask
import sqlite3
import scraping

app = flask.Flask(__name__)
    
@app.route('/')
def tuhorizontal_bars():
    return scraping.app_route()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10100, debug=True)

