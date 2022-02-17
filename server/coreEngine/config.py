"""
config.py
- settings for the flask application object
Created by Xiong, Kaijie on 2022-02-15.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    # SECRET_KEY generated from python secrets library
    # secrets.token_hex(16)
    SECRET_KEY = '95edf18c2e4a2e3211d615b5a12abf7d'