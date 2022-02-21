"""
models.py
- Data classes for the application
Created by Xiong, Kaijie on 2022-02-18.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()

class Musubi(db.Model):
    __tablename__ = 'musubis'

    id = db.Column(db.Integer, primary_key=True)
    musubi_code = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reiteki = db.relationship('Reiteki', backref="musubi", lazy=False)

    def __init__(self, **kwargs):
        super(Musubi, self).__init__(**kwargs)

    def to_dict(self):
        return dict(id = self.id, 
                    musubi_code = self.musubi_code, 
                    about = self.about,
                    created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    reiteki = [r.to_dict() for r in self.reiteki])


class Reiteki(db.Model):
    __tablename__ = 'reitekis'

    id = db.Column(db.Integer, primary_key=True)
    musubi_code = db.Column(db.String(120), db.ForeignKey('musubis.musubi_code'))
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    disname = db.Column(db.String(120))
    profile = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bound = db.Column(db.Integer, default=0)
    post = db.relationship('Post', backref='reiteki', lazy='dynamic', cascade='all, delete-orphan')
    bubblejar = db.relationship('BubbleJar', backref='reiteki', lazy='dynamic', cascade='all, delete-orphan')
    bubble = db.relationship('Bubble', backref='reiteki', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, password, **kwargs) -> None:
        super(Reiteki, self).__init__(**kwargs)
        self.password = generate_password_hash(password, method='sha256')
        

    def to_dict(self):
        return dict(id = self.id,
                    musubi_code = self.musubi_code,
                    username = self.username,
                    password = self.password,
                    disname = self.disname,
                    profile = self.profile,
                    created_at = self.created_at,
                    bound = self.bound)
    
    # def get_all_posts(self):
    #     post_list = []
    #     posts = self.post
    #     for i in posts:
    #         post_list.append(i.to_dict())
    #     return post_list
    def get_all_posts(self):
        return [p.to_dict() for p in self.post]
    
    def get_all_bubblejars(self):
        return [b.to_dict() for b in self.bubblejar]
    
    def get_all_bubbles(self):
        return [b.to_dict() for b in self.bubble]


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    is_public = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('reitekis.id'))

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)

    def to_dict(self):
        return dict(id = self.id,
                    content = self.content,
                    is_public = self.is_public,
                    timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    author_id = self.author_id)


class BubbleJar(db.Model):
    __tablename__ = 'bubblejars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(256))
    is_public = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('reitekis.id'))
    bubble = db.relationship('Bubble', backref='bubblejar', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super(BubbleJar, self).__init__(**kwargs)
    
    def to_dict(self):
        return dict(id = self.id,
                    name = self.name,
                    description = self.description,
                    is_public = self.is_public,
                    timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    author_id = self.author_id)
    
    def get_all_bubbles(self):
        return [b.to_dict() for b in self.bubble]


class Bubble(db.Model):
    __tablename__ = 'bubbles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text())
    is_public = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    bubblejar_id = db.Column(db.Integer, db.ForeignKey('bubblejars.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('reitekis.id'))

    def __init__(self, **kwargs):
        super(Bubble, self).__init__(**kwargs)

    def to_dict(self):
        return dict(id = self.id,
                    title = self.title,
                    content = self.content,
                    is_public =self.is_public,
                    timestamp = self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    bubblejar_id = self.bubblejar_id,
                    author_id = self.author_id)



# class MusubiAlpha(db.Model):
#     __tablename__ = 'musubialphas'

#     id = db.Column(db.Integer, primary_key=True)
#     musubi_code = db.Column(db.String(120), db.ForeignKey('musubis.musubi_code'), unique=True)
#     username = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     disname = db.Column(db.String(120))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __init__(self, password, **kwargs) -> None:
#         super(MusubiAlpha, self).__init__(**kwargs)
#         self.password = generate_password_hash(password, method='sha256')
        

#     def to_dict(self):
#         return dict(id = self.id,
#                     musubi_type = 'alpha',
#                     musubi_code = self.musubi_code,
#                     username = self.username,
#                     password = self.password,
#                     disname = self.disname,
#                     created_at = self.created_at)


# class MusubiBeta(db.Model):
#     __tablename__ = 'musubibetas'

#     id = db.Column(db.Integer, primary_key=True)
#     musubi_code = db.Column(db.String(120), db.ForeignKey('musubis.musubi_code'), unique=True)
#     username = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     disname = db.Column(db.String(120))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __init__(self, password,  **kwargs) -> None:
#         super(MusubiBeta, self).__init__(**kwargs)
#         self.password = generate_password_hash(password, method='sha256')

#     def to_dict(self):
#         return dict(id = self.id,
#                     musubi_type = 'beta',
#                     musubi_code = self.musubi_code,
#                     username = self.username,
#                     password = self.password,
#                     disname = self.disname,
#                     created_at = self.created_at)

