from flask import Flask, jsonify, request
"""
Ejemplo de CRUD implementado con Flask
"""
app = Flask(__name__)

# Datos ficticios para simular una base de datos
productos = [
    {"id": 1, "nombre": "Producto A", "precio": 10.0},
    {"id": 2, "nombre": "Producto B", "precio": 15.0},
    {"id": 3, "nombre": "Producto C", "precio": 20.0}
]

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    for producto in productos:
        if producto['id'] == producto_id:
            return jsonify(producto)
    return jsonify({'mensaje': 'Producto no encontrado'})

# Ruta para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    nuevo_producto = {
        'id': request.json['id'],
        'nombre': request.json['nombre'],
        'precio': request.json['precio']
    }
    productos.append(nuevo_producto)
    return jsonify({'mensaje': 'Producto creado exitosamente'})

# Ruta para actualizar un producto existente
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    for producto in productos:
        if producto['id'] == producto_id:
            producto['nombre'] = request.json['nombre']
            producto['precio'] = request.json['precio']
            return jsonify({'mensaje': 'Producto actualizado exitosamente'})
    return jsonify({'mensaje': 'Producto no encontrado'})

# Ruta para eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    for producto in productos:
        if producto['id'] == producto_id:
            productos.remove(producto)
            return jsonify({'mensaje': 'Producto eliminado exitosamente'})
    return jsonify({'mensaje': 'Producto no encontrado'})

if __name__ == '__main__':
    app.run(debug=True)