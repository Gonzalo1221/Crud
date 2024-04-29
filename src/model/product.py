from config.db import db, app, ma 

class product(db.Model):
    __tablename__ = "tblproduct"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


    def __init__(self, name):
        self.name = name
    
def create_producto():
    # Verificar si ya existen registros en la tabla
    if product.query.count() == 0:
        # Crear registros de administradores
        new_pro = product("arroz")
    
        # Guardar los registros en la base de datos
        db.session.add(new_pro)

        db.session.commit()

with app.app_context():
    db.create_all() 
    create_producto()