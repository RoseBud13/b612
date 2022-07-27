"""
api.py
- provides the API endpoints for consuming and producing REST requests and responses
Created by Rosebud on 2022-06-13.
Copyright © 2022 Rosebud. All rights reserved.
"""

from flask import Blueprint, jsonify, request, current_app
from mongoengine.queryset.visitor import Q
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash
import jwt
from functools import wraps

from .models import User, Post, Comment, Like, BoardingPass
from .utils import Tools


api = Blueprint('api', __name__)


# -------------------------------------- Registration ---------------------------------

def check_boarding_pass(bp_passcode):
    boarding_pass = BoardingPass.objects(passcode=bp_passcode).first()
    if not boarding_pass:
        return False, 'Boarding pass code not found'
    
    # bp_info = boarding_pass.to_dict()
    if boarding_pass.expired == False:
        # if bp_info['pending_code'].startswith('not'):
        if boarding_pass.pending_code.startswith('not'):
            pencode = 'pending_' + Tools.gen_random_code(16)
            boarding_pass.update(pending_code=pencode)
            return True, pencode
        else:
            # return True, bp_info['pending_code']
            return True, boarding_pass.pending_code
    else:
        return False, 'Boarding pass already used'


def check_bp_pencode(pencode):
    boarding_pass = BoardingPass.objects(pending_code=pencode).first()
    if not boarding_pass:
        return False
    else:
        return True


def dump_boarding_pass(pencode, user_uid):
    boarding_pass = BoardingPass.objects(pending_code=pencode).first()
    if not boarding_pass:
        return False, 'Boarding pass not found'
    
    # bp_info = boarding_pass.to_dict()
    if boarding_pass.expired == False and boarding_pass.pending_code.startswith('pending'):
        # if pencode == bp_info['pending_code']:
        if pencode == boarding_pass.pending_code:
            new_pencode = pencode.replace('pending', 'used')
            boarding_pass.update(expired=True, used_by=user_uid, expired_at=datetime.utcnow, pending_code=new_pencode)
            return True, 'Verified, boarding pass expired'
        else:
            return False, 'Pending code invalid'
    else:
        return False, 'Boarding pass invalid'


@api.route('/verify-bp-code', methods=['POST'])
def verify_bp_code():
    data = request.get_json(force=True)

    bp_code = data['passcode']
    print(bp_code)
    status, pending_code = check_boarding_pass(bp_code)
    if status == True:
        return jsonify({'status': status, 'pending_code': pending_code})
    else:
        return jsonify({'status': status, 'message': pending_code})


@api.route('/register-user', methods=['POST'])
def register_user():
    data = request.get_json(force=True)

    pencode = data['pending_code']
    print(pencode)

    if check_bp_pencode(pencode):

        new_email = data['email'] if data['email'] else 'unset_' + Tools.gen_random_code(6) + '@test.com'
        new_username = data['username']
        new_password = data['password']
        new_name = data['name'] if data['name'] else 'unset_' + Tools.gen_random_code(6)


        if not new_email or not new_username or not new_password or not new_name:
            return jsonify({'status': False, 'code': 406, 'message': 'Please fill the needed info'})

        check_email = User.objects(email=new_email).first()
        check_username = User.objects(username=new_username).first()

        if check_email and check_username:
            # returns 409 if email and username exist
            return jsonify({'status': False, 'code': 409, 'message': 'Email and username already used'})
        elif check_email:
            # returns 409 if email exists
            return jsonify({'status': False, 'code': 409, 'message': 'Email already used'})
        elif check_username:
            # returns 409 if username exists
            return jsonify({'status': False, 'code': 409, 'message': 'Username already used'})
        
        new_uid = 'B612' + Tools.gen_random_code(8)
        data['uid'] = new_uid
        data['user_type'] = ['user']

        try:
            if data['birthday']:
                data['birthday'] = datetime.fromisoformat(data['birthday'])
        except KeyError:
            data['birthday'] = None

        del data['pending_code']
        del data['password']
        data['email'] = new_email
        data['name'] = new_name
        print(data)
        
        new_user = User(**data)
        new_user.hash_password(new_password)
        new_user.save()

        pb_result, pb_msg = dump_boarding_pass(pencode, new_uid)
        print(pb_msg)

        if pb_result:
            return jsonify({'status': True, 'code': 201, 'data': new_user.to_dict()})
        else:
            return jsonify({'status': False, 'code': 403, 'message': 'Boarding pass pending code invalid'})
    else:
        return jsonify({'status': False, 'code': 403, 'message': 'Boarding pass pending code invalid'})


# -------------------------------------- Login & Authentication---------------------------------

# Login
@api.route('/login', methods=['POST'])
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
        return jsonify({'status': False, 'code': 401, 'message': 'Credentials required'})

    user = User.objects(username=username).first()

    if not user:
        # returns 401 if the user not exists
        return jsonify({'status': False, 'code': 402, 'message': 'User not found'})

    if check_password_hash(user.password_hash, password):
        # generates the JWT Token
        token = jwt.encode({
            'uid': user.uid,
            'role': user.user_type,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=72)
        }, current_app.config['SECRET_KEY'], algorithm="HS256"),
        print(Tools.tuple_to_str(token))
        return jsonify({'status': True, 'code': 200, 'token': Tools.tuple_to_str(token), 'userInfo': {'username': user.username, 'uid': user.uid, 'avatar': user.avatar_url, 'name': user.name, 'email': user.email}})

    # returns 403 if password is wrong
    return jsonify({'status': False, 'code': 403, 'message': 'Invalid credentials'})


# Authentication
def auth_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        """This decorator function is used to check if the credential token is included
        during requiring from client to server

        Raises:
            RuntimeError: 'User not found'

        Returns:
            [JSON]: If authentocation succeed, returns the uid of current user.
                If faild, returns error message and corresponding HTTP code.
        """

        token = None

        invalid_msg = {
            'message': 'Invalid token. Registeration or authentication required',
            'authenticated': False,
            'code': 401
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False,
            'code': 401
        }

        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token required'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
            print(data)
            current_user = data['uid']
            current_user_role = data['role']
            print(current_user)
            if not current_user:
                raise RuntimeError('User not found')
            return f(current_user, current_user_role, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


# -------------------------------------- Data CRUD---------------------------------


@api.route('/users', methods=['GET'])
@auth_required
def get_all_users(current_user, current_user_role):
    """Get all users stored in the database

    UrlArgs: ?sort=
        asc-by-time,
        asc-by-username,
        asc-by-email,
        type-is-superadmin,
        type-is-admin,
        type-is-user

    Returns:
        JSON: All users' info in database, default ordering is descending by create time
    """

    if 'superadmin' in current_user_role:
        order_method = request.args.get('sort')
        match order_method:
            case 'asc-by-time':
                users = User.objects.order_by("+created_at")
            case 'asc-by-username':
                users = User.objects.order_by("+username")
            case 'asc-by-email':
                users = User.objects.order_by("+email")
            case 'type-is-superadmin':
                users = User.objects(user_type='superadmin')
            case 'type-is-admin':
                users = User.objects(user_type='admin')
            case 'type-is-user':
                users = User.objects(user_type='user')
            case _:
                users = User.objects
        return jsonify({'users': [u.to_dict() for u in users]})
    else:
        return jsonify({'message': 'Access denied. Superadmin required.', 'authenticated': False}), 401


@api.route('/user/<uid>', methods=['GET', 'PUT'])
@auth_required
def get_update_user(current_user, current_user_role, uid):
    user = User.objects(uid=uid).first()

    if not user:
        return jsonify({'status': False, 'code': 402, 'message': 'User not found'})

    if request.method == 'GET':
        return jsonify({'status': True, 'code': 200, 'user': user.to_dict_protected()})
    
    elif request.method == 'PUT':
        data = request.get_json(force=True)

        if 'email' in data:
            check_email = User.objects(email=data['email']).first()
            if check_email:
                return jsonify({'status': False, 'code': 409, 'message': 'Email already used'})
        
        if 'superadmin' in current_user_role:
            user.update(**data)
            updatedUser = User.objects(uid=uid).first()
            return jsonify({'status': True, 'code': 200, 'user': updatedUser.to_dict_protected()})
        elif 'uid' not in data and 'user_type' not in data and 'created_at' not in data and 'password_hash' not in data:
            if current_user == uid:
                user.update(**data)
                updatedUser = User.objects(uid=uid).first()
                return jsonify({'status': True, 'code': 200, 'user': updatedUser.to_dict_protected()})
            else:
                return jsonify({'status': False, 'code': 401, 'message': 'Access denied. Not current user.'})  
        else:
            return jsonify({'status': False, 'code': 401, 'message': 'Access denied. Superadmin required.'})


@api.route('/posts', methods=['GET'])
def get_all_posts():
    time_order = request.args.get('time')
    author_order = request.args.get('author')
    public = request.args.get('public')

    if public == 'true':
        if author_order:
            match time_order:
                case 'asc':
                    posts = Post.objects(Q(author_uid=author_order) & Q(is_public=True)).order_by("+timestamp")
                case _:
                    posts = Post.objects(Q(author_uid=author_order) & Q(is_public=True))
        elif time_order:
            match time_order:
                case 'asc':
                    posts = Post.objects(is_public=True).order_by("+timestamp")
                case _:
                    posts = Post.objects(is_public=True)
        else:
            posts = Post.objects(is_public=True)
    elif public == 'false':
        if author_order:
            match time_order:
                case 'asc':
                    posts = Post.objects(Q(author_uid=author_order) & Q(is_public=False)).order_by("+timestamp")
                case _:
                    posts = Post.objects(Q(author_uid=author_order) & Q(is_public=False))
        elif time_order:
            match time_order:
                case 'asc':
                    posts = Post.objects(is_public=False).order_by("+timestamp")
                case _:
                    posts = Post.objects(is_public=False)
        else:
            posts = Post.objects(is_public=False)
    else:
        if author_order:
            match time_order:
                case 'asc':
                    posts = Post.objects(author_uid=author_order).order_by("+timestamp")
                case _:
                    posts = Post.objects(author_uid=author_order)
        elif time_order:
            match time_order:
                case 'asc':
                    posts = Post.objects.order_by("+timestamp")
                case _:
                    posts = Post.objects
        else:
            posts = Post.objects

    return jsonify({'posts': [p.to_dict() for p in posts]})


@api.route('/comments', methods=['GET'])
def get_all_comments():
    comments = Comment.objects

    return jsonify({'comments': [c.to_dict() for c in comments]})


@api.route('/likes', methods=['GET'])
def get_all_likes():
    likes = Like.objects

    return jsonify({'likes': [l.to_dict() for l in likes]})