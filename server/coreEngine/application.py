"""
application.py
- creates a Flask app instance and registers the database object
Created by Xiong, Kaijie on 2022-02-15.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='B612'):
    app = Flask(app_name)
    app.config.from_object('coreEngine.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from coreEngine.api import api
    app.register_blueprint(api, url_prefix="/api")

    from coreEngine.models import db
    db.init_app(app)

    from coreEngine.commands import cmd
    app.register_blueprint(cmd)

    return app