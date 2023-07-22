from flask import Flask, render_template, jsonify, request
import sqlite3
from products import products

app = Flask(__name__)

DATABASE_NAME = 'database.db'

def createDatabase():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL NOT NULL, quantity INTEGER NOT NULL, image TEXT NOT NULL)')
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Products list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        product = jsonify({"product": productFound[0]})
        template = f"<!DOCTYPE html><html lang='es'><head><title>{product['name']}</title></head><body><center><h1>{product['name']}</h1></center><center><img src='{product['image']}'></center><center><p>{product['price']}</p></center><center><p>{product['quantity']}</p></center></body></html>"
        return template
    return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    
# Path: templates/index.html

