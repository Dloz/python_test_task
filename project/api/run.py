import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

from flask import Flask
from DAL import config

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from api.app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from DAL.models import db
    app.app_context().push()
    db.init_app(app)
        
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app(config)
    app.run(debug=True)