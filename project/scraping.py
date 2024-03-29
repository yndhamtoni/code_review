import requests
from bs4 import BeautifulSoup
import sqlite3
import flask
import os

def scraper(prod, prices):
    url = 'https://book24.ru/catalog/estestvennye-nauki-1347/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = [a.get_text().strip() for a in soup.find_all('a', {"class" : "product-card__name"})]
    authors = [a.get_text().split() for a in soup.find_all('a', {"class" : "author-list__item smartLink"})]
    authors_new = []

    for product in products:
        print(product)

    for author in authors:
        string = ' '.join(author)
        authors_new.append(string)
    for product in products:
        prod.append(product)
    
    for author_new in authors_new:
        prices.append(author_new)

def start(conn, cur):
    prod = []
    author = []
    scraper(prod, author)
    data = list(zip(prod, author))
    cur.execute('DROP TABLE IF EXISTS list_of_products')
    cur.execute('''
        CREATE TABLE list_of_products (
            name  VARCHAR(255),
            price VARCHAR(255)
        )''')

    sql = 'INSERT INTO list_of_products (name, price) values(?, ?)'

    with conn:
        conn.executemany(sql, data)
        data1 = conn.execute("SELECT * FROM list_of_products")
        for row in data1:
            print(row)

def app_route():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    start(conn, cur)
    cur.execute("SELECT * FROM list_of_products")
    data = cur.fetchall()
    cur.close()
    return flask.render_template('table.html', data=data)