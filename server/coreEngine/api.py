"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
Created by Xiong, Kaijie on 2022-02-15.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

from flask import Blueprint, jsonify, request, current_app

from werkzeug.security import check_password_hash
import jwt

from datetime import datetime, timedelta
import random
import requests

from .models import db, Musubi, MusubiAlpha, MusubiBeta
from .utils import Tools, DataHandler


api = Blueprint('api', __name__)


@api.route('/test/', methods=['GET'])
def test():
    return '...'


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


@api.route('/register-alpha/', methods=['POST'])
def register_alpha():
    data = request.get_json(force=True)
    default_musubi_code = Tools.gen_default_musubi_code()
    data['musubi_code'] = default_musubi_code
    print(data)
    new_username = data['username']
    new_password = data['password']

    if not new_username or not new_password:
        return jsonify({'message': 'Please fill the needed info'}), 406

    find_username_alpha = MusubiAlpha.query.filter_by(username=new_username).first()
    find_username_beta = MusubiBeta.query.filter_by(username=new_username).first()

    if find_username_alpha or find_username_beta:
        # returns 409 if the username exists
        return jsonify({'message': 'Username exists'}), 409
    
    musubi_alpha = MusubiAlpha(**data)
    db.session.add(musubi_alpha)
    db.session.commit()
    return jsonify(musubi_alpha.to_dict()), 201


@api.route('/register-beta/<default_musubi_code>/', methods=['POST'])
def register_beta(default_musubi_code):
    find_alpha = MusubiAlpha.query.filter_by(musubi_code=default_musubi_code).first()
    if not find_alpha:
        return jsonify({'message': 'default musubi code from alpha not exists'}), 406

    find_beta = MusubiBeta.query.filter_by(musubi_code=default_musubi_code).first()
    if find_beta:
        return jsonify({'message': 'musubi code already used'}), 406

    data = request.get_json(force=True)
    data['musubi_code'] = default_musubi_code
    print(data)
    new_username = data['username']
    new_password = data['password']

    if not new_username or not new_password:
        return jsonify({'message': 'Please fill the needed info'}), 406

    find_username_alpha = MusubiAlpha.query.filter_by(username=new_username).first()
    find_username_beta = MusubiBeta.query.filter_by(username=new_username).first()

    if find_username_alpha or find_username_beta:
        # returns 409 if the username exists
        return jsonify({'message': 'Username exists'}), 409
    
    musubi_beta = MusubiBeta(**data)
    db.session.add(musubi_beta)
    db.session.commit()
    return jsonify(musubi_beta.to_dict()), 201


@api.route('/merge-musubi/<default_musubi_code>/', methods=['GET'])
def merge_musubi(default_musubi_code):
    find_musubi = Musubi.query.filter_by(musubi_code=default_musubi_code).first()
    if find_musubi:
        return jsonify({'message': 'Musubi code already used'}), 406
        
    data = DataHandler.get_ab_data(default_musubi_code)
    new_data = {}

    if isinstance(data, dict):
        new_musubi_code = data['musubi_code']
    
        if not new_musubi_code:
            return jsonify({'message': 'musubi code needed'}), 406
        
        find_musubi_code = MusubiAlpha.query.filter_by(musubi_code=new_musubi_code).first()
        if not find_musubi_code:
            # returns 409 if the musubi code exists
            return jsonify({'message': 'Musubi code not exists'}), 409
        
        new_data['musubi_code'] = data['musubi_code']
        new_data['username_alpha'] = data['alpha']['username']
        new_data['password_alpha'] = data['alpha']['password']
        new_data['disname_alpha'] =data['alpha']['disname']
        new_data['username_beta'] = data['beta']['username']
        new_data['password_beta'] = data['beta']['password']
        new_data['disname_beta'] =data['beta']['disname']
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

    is_alpha = MusubiAlpha.query.filter_by(username=username).first()
    is_beta = MusubiBeta.query.filter_by(username=username).first()

    if not is_alpha and not is_beta:
        # returns 401 if the cdsid is not existing
        return jsonify({'message': 'User not found', 'authenticated': False}), 401
    
    if is_alpha:
        if check_password_hash(is_alpha.password, password):
            # generates the JWT Token
            token = jwt.encode({
                'uid': is_alpha.username,
                'iat': datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=60)
            }, current_app.config['SECRET_KEY'], algorithm="HS256"),
            print(Tools.convert_tuple(token))

            is_musubi_completed = Musubi.query.filter_by(musubi_code=is_alpha.musubi_code).first()
            if not is_musubi_completed:
                return jsonify({'token': Tools.convert_tuple(token), 'username': is_alpha.username, 'type': 'alpha', 'status': 'not completed'}), 200
            else:
                return jsonify({'token': Tools.convert_tuple(token), 'username': is_alpha.username, 'type': 'alpha', 'status': 'completed'}), 200
        # returns 403 if password is wrong
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 403
    else:
        if check_password_hash(is_beta.password, password):
            # generates the JWT Token
            token = jwt.encode({
                'uid': is_beta.username,
                'iat': datetime.utcnow(),
                'exp': datetime.utcnow() + timedelta(minutes=60)
            }, current_app.config['SECRET_KEY'], algorithm="HS256"),
            print(Tools.convert_tuple(token))
            return jsonify({'token': Tools.convert_tuple(token), 'username': is_beta.username, 'type': 'beta'}), 200
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


@api.route('/musubialphas/', methods=['GET'])
def get_musubialphas():
    """This function is used to get all users that stored in local database

    Args:
        current_user (String): the uid of current user

    Returns:
        JSON: All users' info in database
    """
    musubialphas = MusubiAlpha.query.all()
    return jsonify({'musubialphas': [m.to_dict() for m in musubialphas]})


@api.route('/musubibetas/', methods=['GET'])
def get_musubibetas():
    """This function is used to get all users that stored in local database

    Args:
        current_user (String): the uid of current user

    Returns:
        JSON: All users' info in database
    """
    musubibetas = MusubiBeta.query.all()
    return jsonify({'musubibetas': [m.to_dict() for m in musubibetas]})

