from flask import Flask, render_template, jsonify
from products import products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)


