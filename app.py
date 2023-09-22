import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import *
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    print(app)
    print("Hello-------")
    CORS(app)
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    from blueprints.blueprint import blueprint
    app.register_blueprint(blueprint)
    return app