from flask import Blueprint, Flask, session, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.product import product


routes_product = Blueprint("routes_product", __name__)



@routes_product.route('/mostrar', methods=['GET'])
def mostrar_producto():

    productos = product.query.all()

    detalles_productos = []

    for producto in productos:
        detalles_producto = {
            "id": producto.id,
            "nombre": producto.name,
        }
        detalles_productos.append(detalles_producto)
    return jsonify(detalles_productos), 200