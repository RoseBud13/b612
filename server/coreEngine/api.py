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

from .models import db, Musubi, Reiteki, Post, BubbleJar, Bubble
from .utils import Tools, DataHandler


api = Blueprint('api', __name__)


@api.route('/test/', methods=['GET'])
def test():
    return '孙婉宁我爱你呀'


# -------------------------------------- Registration ---------------------------------

# Test
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


# Reitki (first user account)
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


# Reiteki (second user account)
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


# Musubi (user couple entity)
@api.route('/create-musubi/<default_musubi_code>/', methods=['POST'])
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


# Login
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
            'uid': get_reiteki.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=60)
        }, current_app.config['SECRET_KEY'], algorithm="HS256"),
        print(Tools.convert_tuple(token))

        is_musubi_completed = Musubi.query.filter_by(musubi_code=get_reiteki.musubi_code).first()
        count_reiteki = Reiteki.query.filter_by(musubi_code=get_reiteki.musubi_code).count()
        if not is_musubi_completed and count_reiteki == 1:
            return jsonify({'token': Tools.convert_tuple(token), 'username': get_reiteki.username, 'id': get_reiteki.id, 'status': 'not completed'}), 200
        else:
            return jsonify({'token': Tools.convert_tuple(token), 'username': get_reiteki.username, 'id': get_reiteki.id, 'status': 'completed'}), 200
    # returns 403 if password is wrong
    return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 403


# -------------------------------------- Data CRUD---------------------------------


# Musubi code
@api.route('/update-musubi-code/<musubi_code>/', methods=['PUT'])
def update_musubi_code(musubi_code):
    musubi = Musubi.query.filter_by(musubi_code=musubi_code).first()
    reiteki_list = Reiteki.query.filter_by(musubi_code=musubi_code).all()
    if not musubi or not reiteki_list:
        return jsonify({'message': 'musubi code not valid'}), 404

    data = request.get_json(force=True)
    print(data)
    new_musubi_code = data['musubi_code']

    check_musubi_code_musubi = Musubi.query.filter_by(musubi_code=new_musubi_code).count()
    print(check_musubi_code_musubi)
    check_musubi_code_reiteki = Reiteki.query.filter_by(musubi_code=new_musubi_code).count()
    print(check_musubi_code_reiteki)

    if check_musubi_code_musubi == 0 and check_musubi_code_reiteki == 0:
        musubi.musubi_code = new_musubi_code
        for r in reiteki_list:
            r.musubi_code = new_musubi_code
        db.session.commit()
        return jsonify({'message': 'musubi code updated', 'musubi': musubi.to_dict(), 'reitekis': [r.to_dict() for r in reiteki_list]}), 201
    else:
        return jsonify({'message': 'musubi code already used'}), 406


# Musubi
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


@api.route('/get-update-musubi-info/<musubi_code>/', methods=['GET', 'PUT'])
def get_update_musubi_info(musubi_code):
    musubi = Musubi.query.filter_by(musubi_code=musubi_code).first()
    if not musubi:
        return jsonify({'message': 'musubi not found'}), 404

    if request.method == 'GET':
        return jsonify({'musubi': musubi.to_dict()})

    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data)
        about = data['about']
        musubi.about = about
        db.session.commit()
        return jsonify(musubi.to_dict()), 201


# Reiteki
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
    return jsonify({'reitekis': [r.to_dict() for r in reitekis]})


@api.route('/get-update-reiteki-by-username/<reiteki_username>/', methods=['GET', 'PUT'])
def get_update_reiteki_by_username(reiteki_username):
    reiteki = Reiteki.query.filter_by(username=reiteki_username).first()
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    
    if request.method == 'GET':
        return jsonify({'reiteki': reiteki.to_dict()})

    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data)

        if data.get('username'):
            check_username = Reiteki.query.filter_by(username=data['username']).first()
            if check_username:
                return jsonify({'message': 'username already exists'}), 406
            else:
                reiteki.username = data['username']
        if data.get('disname'):
            reiteki.disname = data['disname']
        if data.get('profile'):
            reiteki.profile = data['profile']
        
        db.session.commit()
        return jsonify({'message':'reiteki updated', 'reiteki': reiteki.to_dict()}), 201


# Post
@api.route('/create-post/', methods=['POST'])
def create_post():
    data = request.get_json(force=True)
    new_post = Post(**data)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201


@api.route('/get-all-posts/', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    return jsonify({'posts': [p.to_dict() for p in posts]})


@api.route('/get-all-public-posts/', methods=['GET'])
def get_all_pubicl_posts():
    posts = Post.query.all()
    posts_list = []
    for p in posts:
        if p.is_public == True:
            posts_list.append(p)
    return jsonify({'posts': [p.to_dict() for p in posts_list]})


@api.route('/get-posts-by-reiteki/<int:reiteki_id>/', methods=['GET'])
def get_posts_by_reiteki(reiteki_id):
    reiteki = Reiteki.query.get(reiteki_id)
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'posts': reiteki.get_all_posts()})


@api.route('/get-posts-by-username/<reiteki_username>/', methods=['GET'])
def get_posts_by_username(reiteki_username):
    reiteki = Reiteki.query.filter_by(username=reiteki_username).first()
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'posts': reiteki.get_all_posts()})


@api.route('/get-update-post/<int:post_id>/', methods=['GET', 'PUT'])
def get_update_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'post not exists'}), 404

    if request.method == 'GET':
        return jsonify({'post': post.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data)
        post.content = data['content']
        db.session.commit()
        return jsonify({'message':'post content updated', 'post': post.to_dict()}), 201


@api.route('/update-post-visibility/<int:post_id>/', methods=['PUT'])
def update_post_visibility(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'post not exists'}), 404

    data = request.get_json(force=True)
    print(data)
    post.is_public = data['is_public']
    db.session.commit()
    return jsonify({'message':'post visibility updated', 'post': post.to_dict()}), 201


@api.route('/delete-post/<int:post_id>/', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'post not exists'}), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'post deleted'}), 201


# Bubble jar
@api.route('/create-bubblejar/', methods=['POST'])
def create_bubblejar():
    data = request.get_json(force=True)
    new_bubblejar = BubbleJar(**data)
    db.session.add(new_bubblejar)
    db.session.commit()
    return jsonify(new_bubblejar.to_dict()), 201


@api.route('/get-all-bubblejars/', methods=['GET'])
def get_all_bubblejars():
    bubblejars = BubbleJar.query.all()
    return jsonify({'bubblejars': [b.to_dict() for b in bubblejars]})


@api.route('/get-bubblejars-by-reiteki/<int:reiteki_id>/', methods=['GET'])
def get_bubblejars_by_reiteki(reiteki_id):
    reiteki = Reiteki.query.get(reiteki_id)
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'bubblejars': reiteki.get_all_bubblejars()})


@api.route('/get-bubblejars-by-username/<reiteki_username>/', methods=['GET'])
def get_bubblejars_by_username(reiteki_username):
    reiteki = Reiteki.query.filter_by(username=reiteki_username).first()
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'bubblejars': reiteki.get_all_bubblejars()})


@api.route('/get-update-bubblejar/<int:bubblejar_id>/', methods=['GET', 'PUT'])
def get_update_bubblejar(bubblejar_id):
    bubblejar= BubbleJar.query.get(bubblejar_id)
    if not bubblejar:
        return jsonify({'message': 'bubblejar not exists'}), 404

    if request.method == 'GET':
        return jsonify({'bubblejar': bubblejar.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data)

        if data.get('name'):
            bubblejar.name = data['name']
        if data.get('description'):
            bubblejar.description = data['description']
        db.session.commit()
        return jsonify({'message':'bubblejar updated', 'bubblejar': bubblejar.to_dict()}), 201


@api.route('/update-bubblejar-visibility/<int:bubblejar_id>/', methods=['PUT'])
def update_bubblejar_visibility(bubblejar_id):
    bubblejar = BubbleJar.query.get(bubblejar_id)
    if not bubblejar:
        return jsonify({'message': 'bubblejar not exists'}), 404

    data = request.get_json(force=True)
    print(data)
    bubblejar.is_public = data['is_public']
    db.session.commit()
    return jsonify({'message':'bubblejar visibility updated', 'bubblejar': bubblejar.to_dict()}), 201


@api.route('/delete-bubblejar/<int:bubblejar_id>/', methods=['DELETE'])
def delete_bubblejar(bubblejar_id):
    bubblejar = BubbleJar.query.get(bubblejar_id)
    if not bubblejar:
        return jsonify({'message': 'bubblejar not exists'}), 404
    
    related_bubbles = get_bubbles_by_jar(bubblejar_id)
    for i in related_bubbles['bubbles']:
        db.session.delete(i)
    
    db.session.delete(bubblejar)
    db.session.commit()
    return jsonify({'message': 'bubblejar and related bubbles deleted'}), 201


# Bubble
@api.route('/create-bubble/', methods=['POST'])
def create_bubble():
    data = request.get_json(force=True)
    new_bubble = Bubble(**data)
    db.session.add(new_bubble)
    db.session.commit()
    return jsonify(new_bubble.to_dict()), 201


@api.route('/get-all-bubbles/', methods=['GET'])
def get_all_bubbles():
    bubbles = Bubble.query.all()
    return jsonify({'bubbles': [b.to_dict() for b in bubbles]})


@api.route('/get-bubbles-by-reiteki/<int:reiteki_id>/', methods=['GET'])
def get_bubbles_by_reiteki(reiteki_id):
    reiteki = Reiteki.query.get(reiteki_id)
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'bubbles': reiteki.get_all_bubbles()})


@api.route('/get-bubbles-by-username/<reiteki_username>/', methods=['GET'])
def get_bubbles_by_username(reiteki_username):
    reiteki = Reiteki.query.filter_by(username=reiteki_username).first()
    if not reiteki:
        return jsonify({'message': 'user not found'}), 404
    return jsonify({'bubbles': reiteki.get_all_bubbles()})


@api.route('/get-bubbles-by-jar/<int:jar_id>/', methods=['GET'])
def get_bubbles_by_jar(jar_id):
    jar = BubbleJar.query.get(jar_id)
    if not jar:
        return jsonify({'message': 'Bubble Jar not found'}), 404
    return jsonify({'bubbles': jar.get_all_bubbles()})


@api.route('/get-update-bubble/<int:bubble_id>/', methods=['GET', 'PUT'])
def get_update_bubble(bubble_id):
    bubble= Bubble.query.get(bubble_id)
    if not bubble:
        return jsonify({'message': 'bubble not exists'}), 404

    if request.method == 'GET':
        return jsonify({'bubble': bubble.to_dict()})
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data)

        if data.get('title'):
            bubble.title = data['title']
        if data.get('content'):
            bubble.content = data['content']
        db.session.commit()
        return jsonify({'message':'bubble updated', 'bubble': bubble.to_dict()}), 201


@api.route('/update-bubble-visibility/<int:bubble_id>/', methods=['PUT'])
def update_bubble_visibility(bubble_id):
    bubble = Bubble.query.get(bubble_id)
    if not bubble:
        return jsonify({'message': 'bubble not exists'}), 404

    data = request.get_json(force=True)
    print(data)
    bubble.is_public = data['is_public']
    db.session.commit()
    return jsonify({'message':'bubble visibility updated', 'bubble': bubble.to_dict()}), 201


@api.route('/delete-bubble/<int:bubble_id>/', methods=['DELETE'])
def delete_bubble(bubble_id):
    bubble = Bubble.query.get(bubble_id)
    if not bubble:
        return jsonify({'message': 'bubble not exists'}), 404
    
    db.session.delete(bubble)
    db.session.commit()
    return jsonify({'message': 'bubble deleted'}), 201


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

