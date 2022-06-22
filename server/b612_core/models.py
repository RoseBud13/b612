"""
models.py
- Data classes for the application
Created by Rosebud on 2022-06-13.
Copyright © 2021 Rosebud. All rights reserved.
"""

from flask_mongoengine import MongoEngine
from datetime import datetime
from werkzeug.security import generate_password_hash
import time


db = MongoEngine()


def get_disname_by_uid(uid):
    user = User.objects(uid=uid).first()
    user_dict = user.to_dict()
    return user_dict['name']


def convert_utc_to_local(utc_datetime):
    if utc_datetime:
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        local_time = utc_datetime + offset
        return local_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None


class BoardingPass(db.Document):
    passcode = db.StringField(required=True, max_length=64, unique=True)
    pending_code = db.StringField(required=True, max_length=64, unique=True)
    expired = db.BooleanField(Required=True, default=False)
    used_by = db.StringField(max_length=64, verbose_name="user_uid")
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)
    expired_at = db.DateTimeField()

    meta = {
        'collection': 'boarding_pass',
        'ordering': ['-created_at'],
        'allow_inheritance': True,
    }

    def __init__(self, **kwargs):
        super(BoardingPass, self).__init__(**kwargs)

    def to_dict(self):
        return dict(passcode = self.passcode,
                    pending_code = self.pending_code,
                    expired = self.expired,
                    used_by = self.used_by,
                    created_at = convert_utc_to_local(self.created_at),
                    expired_at = convert_utc_to_local(self.expired_at))


class User(db.DynamicDocument):
    uid = db.StringField(required=True, max_length=64, unique=True)
    email = db.EmailField(required=True, allow_utf8_user=True, unique=True)
    username = db.StringField(required=True, max_length=128, unique=True)
    password_hash = db.StringField(required=True, max_length=256)
    name = db.StringField(required=True, max_length=128)
    profile = db.StringField(max_length=512)
    avatar_url = db.StringField()
    birthday = db.DateTimeField()
    user_type = db.ListField(db.StringField(required=True))
    created_at = db.DateTimeField(required=True, default=datetime.utcnow)

    meta = {
        'collection': 'user',
        'ordering': ['-created_at'],
        'allow_inheritance': True,
    }

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')
    
    def to_dict(self):
        return dict(uid = self.uid,
                    email = self.email,
                    username = self.username,
                    password = self.password_hash,
                    name = self.name,
                    profile_text = self.profile,
                    avatar_url = self.avatar_url,
                    birthday = convert_utc_to_local(self.birthday),
                    user_type = self.user_type,
                    created_at = convert_utc_to_local(self.created_at))


class Post(db.DynamicDocument):
    post_id = db.StringField(required=True, max_length=64, unique=True)
    title = db.StringField(required=True, max_length=128)
    cover = db.StringField(required=True, max_length=512)
    author_uid = db.StringField(required=True, max_length=64)
    content = db.StringField()
    post_type = db.StringField(required=True)
    is_public = db.BooleanField(required=True, default=False)
    timestamp = db.DateTimeField(required=True, default=datetime.utcnow)
    likes = db.LongField()

    meta = {
        'collection': 'post',
        'ordering': ['-timestamp'],
        'allow_inheritance': True,
        'indexes': ['-timestamp', 'title', 'author_uid']
    }

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)

    def to_dict(self):
        return dict(post_id = self.post_id,
                    title = self.title,
                    cover = self.cover,
                    author_uid = self.author_uid,
                    author = get_disname_by_uid(self.author_uid),
                    content = self.content,
                    post_type = self.post_type,
                    is_public = self.is_public,
                    timestamp = convert_utc_to_local(self.timestamp),
                    likes = self.likes)


class Comment(db.DynamicDocument):
    comment_id = db.StringField(required=True, max_length=64, unique=True)
    comment_of = db.StringField(required=True, max_length=64, verbose_name="post_comment_id")
    content = db.StringField(required=True, verbose_name="comment")
    author_uid = db.StringField(required=True, max_length=64, verbose_name="uid")
    timestamp = db.DateTimeField(required=True, default=datetime.utcnow)
    likes = db.LongField()

    meta = {
        'collection': 'comment',
        'ordering': ['-timestamp'],
        'allow_inheritance': True,
        'indexes': ['-timestamp', 'author_uid', 'likes', 'comment_of']
    }

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def to_dict(self):
        return dict(comment_id = self.comment_id,
                    comment_of = self.comment_of,
                    content = self.content,
                    author_uid = self.author_uid,
                    author = get_disname_by_uid(self.author_uid),
                    timestamp = convert_utc_to_local(self.timestamp),
                    likes = self.likes)


class Like(db.DynamicDocument):
    like_id = db.StringField(required=True, max_length=64, unique=True)
    like_of = db.StringField(required=True, max_length=64, verbose_name="post_comment_id")
    author_uid = db.StringField(required=True, max_length=64, verbose_name="uid")
    timestamp = db.DateTimeField(required=True, default=datetime.utcnow)

    meta = {
        'collection': 'like',
        'ordering': ['-timestamp'],
        'allow_inheritance': True,
        'indexes': ['-timestamp', 'author_uid', 'like_of']
    }

    def __init__(self, **kwargs):
        super(Like, self).__init__(**kwargs)
    
    def to_dict(self):
        return dict(like_id = self.like_id,
                    like_of = self.like_of,
                    author_uid = self.author_uid,
                    author = get_disname_by_uid(self.author_uid),
                    timestamp = convert_utc_to_local(self.timestamp))
