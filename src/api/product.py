from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from flask_sqlalchemy import SQLAlchemy
from model.product import product


routes_product = Blueprint("routes_product", __name__)



@routes_product.route('/mostrarproductos', methods=['GET'])
def mostrar_product():

    productos = product.query.all()

    detalles_productos = []

    for producto in productos:
        detalles_producto = {
            "id": producto.id,
            "nombre": producto.name,
        }
        detalles_productos.append(detalles_producto)
    return jsonify(detalles_productos), 200