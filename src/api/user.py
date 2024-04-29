from flask import Blueprint, Flask, session, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model.user import user


routes_user = Blueprint("routes_user", __name__)



@routes_user.route('/guardar', methods=['POST'])
def guardar():
    name = request.json["nombre"]
    lastname = request.json["apellidos"]
    email = request.json["correo"]
    message = request.json["mensaje"]

    new_user = user(name,lastname,email,message)
    db.sesion.add(new_user)
    db.sesion.commit()
    return "registro exitoso"