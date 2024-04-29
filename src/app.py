#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/

from flask import Flask ,session, render_template
from config.db import db, app, ma

#importar los model en orden
from model.product import product
from model.user import user


# importacion de los api
from api.user import routes_user
from api.product import routes_product


app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_product, url_prefix="/api")

@app.route("/")
def index():
    return render_template('main/index.html')

if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    