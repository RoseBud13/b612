"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
Created by Xiong, Kaijie on 2022-02-18.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

from flask import Blueprint, jsonify, request, current_app

from werkzeug.security import check_password_hash
import jwt

from datetime import datetime, timedelta
import random
import requests

from .models import db, Musubi, Reiteki
from .utils import Tools, DataHandler


api = Blueprint('api', __name__)


@api.route('/test/', methods=['GET'])
def test():
    return '孙婉宁我爱你呀'


# -------------------------------------- Registration ---------------------------------


@api.route('/register-test/', methods=['POST'])
def register_test():
    """
    This function is used to test registration of new user to local database

    Returns:
        JSON: input data
    """
    data = request.get_json(force=True)
    new_musubi_code = data['musubi_code']
    
    if not new_musubi_code:
        return jsonify({'message': 'Please fill the musubi code'}), 406
    
    find_musubi = Musubi.query.filter_by(musubi_code=new_musubi_code).first()

    if find_musubi:
        # returns 409 if the musubi code exists
        return jsonify({'message': 'Musubi code exists'}), 409

    musubi = Musubi(**data)
    db.session.add(musubi)
    db.session.commit()
    return jsonify(musubi.to_dict()), 201


@api.route('/register-reiteki/', methods=['POST'])
def register_reiteki():
    data = request.get_json(force=True)
    default_musubi_code = Tools.gen_default_musubi_code()
    data['musubi_code'] = default_musubi_code
    print(data)
    new_username = data['username']
    new_password = data['password']

    if not new_username or not new_password:
        return jsonify({'message': 'Please fill the needed info'}), 406

    find_username = Reiteki.query.filter_by(username=new_username).first()

    if find_username:
        # returns 409 if the username exists
        return jsonify({'message': 'Username exists'}), 409
    
    new_reiteki = Reiteki(**data)
    db.session.add(new_reiteki)
    db.session.commit()
    return jsonify(new_reiteki.to_dict()), 201


@api.route('/bind-reiteki/<default_musubi_code>/', methods=['POST'])
def bind_reiteki(default_musubi_code):
    get_first_reiteki = Reiteki.query.filter_by(musubi_code=default_musubi_code).first()
    if not get_first_reiteki:
        return jsonify({'message': 'default musubi code from first reiteki not exists'}), 406

    count_reiteki = Reiteki.query.filter_by(musubi_code=default_musubi_code).count()
    if count_reiteki > 1:
        return jsonify({'message': 'musubi code already used'}), 406

    data = request.get_json(force=True)
    data['musubi_code'] = default_musubi_code
    print(data)

    new_username = data['username']
    new_password = data['password']
    if not new_username or not new_password:
        return jsonify({'message': 'Please fill the needed info'}), 406

    find_username = Reiteki.query.filter_by(username=new_username).first()
    if find_username:
        # returns 409 if the username exists
        return jsonify({'message': 'Username already used'}), 409
    
    another_reiteki = Reiteki(**data)
    another_reiteki.bound = 1
    db.session.add(another_reiteki)
    get_first_reiteki.bound = 1
    db.session.commit()

    return jsonify(another_reiteki.to_dict()), 201


@api.route('/create-musubi/<default_musubi_code>/', methods=['GET'])
def create_musubi(default_musubi_code):
    # find_musubi_code = Reiteki.query.filter_by(musubi_code=default_musubi_code).first()
    # if not find_musubi_code:
    #     # returns 409 if the musubi code exists
    #     return jsonify({'message': 'Musubi code not exists'}), 409
    
    find_musubi = Musubi.query.filter_by(musubi_code=default_musubi_code).first()
    if find_musubi:
        return jsonify({'message': 'Musubi code already used'}), 406
        
    data = DataHandler.get_paired_reiteki(default_musubi_code)
    new_data = {}

    if isinstance(data, dict):
        new_musubi_code = data['musubi_code']
    
        if not new_musubi_code:
            return jsonify({'message': 'musubi code needed'}), 406
        
        new_data['musubi_code'] = data['musubi_code']
        print(new_data)

        musubi = Musubi(**new_data)
        db.session.add(musubi)
        db.session.commit()
        return jsonify(musubi.to_dict()), 201

    return jsonify(data), 406


# -------------------------------------- Login ---------------------------------


@api.route('/login/', methods=['POST'])
def login():
    """
    This function is constructed for local login.

    Method: First check if the input is valid or not,
        then check if the user exists in the database,
        if not, return error message,
        or continueing check the password validity,
        if true, return the token and user info wrapped in JSON data.

    Returns:
        JSON: the status of whether logined successfully,
            and if yes, return the token and user info.
    """

    data = request.get_json(force=True)
    username = data['username']
    password = data['password']

    if not username or not password:
        # returns 401 if any username or / and password is missing
        return jsonify({'message': 'Login required', 'authenticated': False}), 401

    get_reiteki = Reiteki.query.filter_by(username=username).first()

    if not get_reiteki:
        # returns 401 if the cdsid is not existing
        return jsonify({'message': 'User not found', 'authenticated': False}), 401
    
    if check_password_hash(get_reiteki.password, password):
        # generates the JWT Token
        token = jwt.encode({
            'uid': get_reiteki.username,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=60)
        }, current_app.config['SECRET_KEY'], algorithm="HS256"),
        print(Tools.convert_tuple(token))

        is_musubi_completed = Musubi.query.filter_by(musubi_code=get_reiteki.musubi_code).first()
        count_reiteki = Reiteki.query.filter_by(musubi_code=get_reiteki.musubi_code).count()
        if not is_musubi_completed and count_reiteki == 1:
            return jsonify({'token': Tools.convert_tuple(token), 'username': get_reiteki.username, 'status': 'not completed'}), 200
        else:
            return jsonify({'token': Tools.convert_tuple(token), 'username': get_reiteki.username, 'status': 'completed'}), 200
    # returns 403 if password is wrong
    return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 403


# -------------------------------------- Get all data ---------------------------------


@api.route('/musubis/', methods=['GET'])
def get_musubis():
    """This function is used to get all users that stored in local database

    Args:
        current_user (String): the uid of current user

    Returns:
        JSON: All users' info in database
    """
    musubis = Musubi.query.all()
    return jsonify({'musubis': [m.to_dict() for m in musubis]})


@api.route('/get-musubis-by-code/<musubi_code>/', methods=['GET'])
def get_musubis_by_code(musubi_code):
    musubis = Musubi.query.filter_by(musubi_code=musubi_code).all()
    if not musubis:
        return jsonify({'message': 'musubi code not valid'}), 406
    return jsonify({'musubis': [m.to_dict() for m in musubis]})


@api.route('/reitekis/', methods=['GET'])
def get_reitekis():
    """This function is used to get all users that stored in local database

    Args:
        current_user (String): the uid of current user

    Returns:
        JSON: All users' info in database
    """
    reitekis = Reiteki.query.all()
    return jsonify({'reiteki': [r.to_dict() for r in reitekis]})


@api.route('/get-reitekis-by-code/<musubi_code>/', methods=['GET'])
def get_reitekis_by_code(musubi_code):
    reitekis = Reiteki.query.filter_by(musubi_code=musubi_code).all()
    if not reitekis:
        return jsonify({'message': 'musubi code not valid'}), 406
    return jsonify({'musubis': [r.to_dict() for r in reitekis]})


# @api.route('/musubialphas/', methods=['GET'])
# def get_musubialphas():
#     """This function is used to get all users that stored in local database

#     Args:
#         current_user (String): the uid of current user

#     Returns:
#         JSON: All users' info in database
#     """
#     musubialphas = MusubiAlpha.query.all()
#     return jsonify({'musubialphas': [m.to_dict() for m in musubialphas]})


# @api.route('/musubibetas/', methods=['GET'])
# def get_musubibetas():
#     """This function is used to get all users that stored in local database

#     Args:
#         current_user (String): the uid of current user

#     Returns:
#         JSON: All users' info in database
#     """
#     musubibetas = MusubiBeta.query.all()
#     return jsonify({'musubibetas': [m.to_dict() for m in musubibetas]})

