"""
models.py
- Data classes for the application
Created by Xiong, Kaijie on 2022-02-15.
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
    username_alpha = db.Column(db.String(120), unique=True, nullable=False)
    password_alpha = db.Column(db.String(255), nullable=False)
    disname_alpha = db.Column(db.String(120))
    username_beta = db.Column(db.String(120), unique=True, nullable=False)
    password_beta = db.Column(db.String(255), nullable=False)
    disname_beta = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    musubi_alpha = db.relationship('MusubiAlpha', backref="musubi", lazy=False)
    musubi_beta = db.relationship('MusubiBeta', backref="musubi", lazy=False)

    def __init__(self, **kwargs):
        super(Musubi, self).__init__(**kwargs)

    def to_dict(self):
        return dict(id = self.id, 
                    musubi_code = self.musubi_code, 
                    username_alpha = self.username_alpha,
                    disname_alpha = self.disname_alpha,
                    username_beta = self.username_beta,
                    disname_beta = self.disname_beta,
                    created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    musubi_alpha = [m.to_dict() for m in self.musubi_alpha],
                    musubi_beta = [m.to_dict() for m in self.musubi_beta])


class MusubiAlpha(db.Model):
    __tablename__ = 'musubialphas'

    id = db.Column(db.Integer, primary_key=True)
    musubi_code = db.Column(db.String(120), db.ForeignKey('musubis.musubi_code'), unique=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    disname = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, password, **kwargs) -> None:
        super(MusubiAlpha, self).__init__(**kwargs)
        self.password = generate_password_hash(password, method='sha256')
        

    def to_dict(self):
        return dict(id = self.id,
                    musubi_type = 'alpha',
                    musubi_code = self.musubi_code,
                    username = self.username,
                    password = self.password,
                    disname = self.disname,
                    created_at = self.created_at)


class MusubiBeta(db.Model):
    __tablename__ = 'musubibetas'

    id = db.Column(db.Integer, primary_key=True)
    musubi_code = db.Column(db.String(120), db.ForeignKey('musubis.musubi_code'), unique=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    disname = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, password,  **kwargs) -> None:
        super(MusubiBeta, self).__init__(**kwargs)
        self.password = generate_password_hash(password, method='sha256')

    def to_dict(self):
        return dict(id = self.id,
                    musubi_type = 'beta',
                    musubi_code = self.musubi_code,
                    username = self.username,
                    password = self.password,
                    disname = self.disname,
                    created_at = self.created_at)

