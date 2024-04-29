from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
from model.user import user


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

