from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
from model.user import user
from model.product import product, productSchema


routes_user = Blueprint("routes_user", __name__)

@routes_user.route('/guardar', methods=['POST'])
def guardar():
    name = request.json['name']
    lastname = request.json['lastname']
    phone = request.json['phone']
    product = request.json['product']

    new_user = user(name,lastname,phone,product)
    db.session.add(new_user)
    db.session.commit()
    return "registro exitoso"

@routes_user.route('/mostrarusuarios', methods=['GET'])
def mostrar_user():

    usuarios = user.query.all()

    detalles_usuarios = []

    for usuario in usuarios:
        detalles_usuario = {
            "id": usuario.id,
            "nombre": usuario.name,
            "apellidos": usuario.lastname,
            "telefono": usuario.phone,
            "productos": db.session.query(product.name).filter(product.id == usuario.product).first().name,
        }
        detalles_usuarios.append(detalles_usuario)
    return jsonify(detalles_usuarios), 200

@routes_user.route('/actualizarusuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.json

    if datos:
        usuario = user.query.get_or_404(id)

        usuario.name = datos.get('nombre', usuario.name)
        usuario.lastname = datos.get('apellidos', usuario.lastname)
        usuario.phone = datos.get('telefono', usuario.phone)
        usuario.product = datos.get('productos', usuario.product)

        db.session.commit()

        return jsonify({'mensaje': 'Usuario actualizado con éxito'}), 200
    else:
        return jsonify({'error': 'Datos no proporcionados'}), 400

@routes_user.route('/eliminarusuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):

    usuario = user.query.get_or_404(id)

    if usuario:
        db.session.delete(usuario)
        db.session.commit()

        return jsonify({'mensaje': 'Usuario eliminado con éxito'}), 200
    else:
        return jsonify({'error': 'No se encontró el usuario'}), 404
    
@routes_user.route('/llenarusuarios/<int:id>', methods=['GET'])
def mostrar_users(id):
    usuario = user.query.get_or_404(id)

    detalles_usuario = {
        "id": usuario.id,
        "nombre": usuario.name,
        "apellidos": usuario.lastname,
        "telefono": usuario.phone,
        "productos": usuario.product,
    }

    return jsonify(detalles_usuario), 200
