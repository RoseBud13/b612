"""
config.py
- settings for the flask application object
Created by Rosebud on 2022-06-13.
Copyright © 2022 Rosebud. All rights reserved.
"""

class BaseConfig(object):
    DEBUG = True
    # used for encryption and session management
    # SECRET_KEY generated from python secrets library
    # secrets.token_hex(16)
    SECRET_KEY = '95edf18c2e4a2e3211d615b5a12abf7d'
    MONGODB_SETTINGS = {
        'db': 'b612DB',
        'host': 'localhost',
        'port': 27017,
        'connect': True,
    }