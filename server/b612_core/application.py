"""
application.py
- creates a Flask app instance and registers the database object
Created by Rosebud on 2022-02-15.
Copyright © 2022 Rosebud. All rights reserved.
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='B612'):
    app = Flask(app_name)
    app.config.from_object('b612_core.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    from b612_core.api import api
    app.register_blueprint(api, url_prefix="/api")

    from b612_core.models import db
    db.init_app(app)

    from b612_core.commands import cmd
    app.register_blueprint(cmd)

    return app