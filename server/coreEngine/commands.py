"""
commands.py
- provides a command line utility for interacting with the
  application to perform interIdle debugging and setup
CI Hub server

Created by Xiong, Kaijie on 2021-07-30.
Copyright © 2021 Volvo Car Corporation. All rights reserved.
"""

import click

from flask import Blueprint
from sqlalchemy import false
from coreEngine.models import db, Musubi, User, Post, BubbleJar, Bubble

cmd = Blueprint('cmd', __name__)


@cmd.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@cmd.cli.command()
def forge():
    """Generate mockup data."""

    users = [
      {'is_reiteki': True, 'musubi_code': 'sun_to_jupiter', 'username': 'wanning', 'password': '123123', 'disname': '孙婉宁', 'profile': '我喜欢熊恺杰', 'bound': 1},
      {'is_reiteki': True, 'musubi_code': 'sun_to_jupiter', 'username': 'kaijie', 'password': '123123', 'disname': '熊恺杰', 'profile': '我喜欢孙婉宁', 'bound': 1},
    ]
    for u in users:
        user = User(is_reiteki=u['is_reiteki'], musubi_code=u['musubi_code'], username=u['username'], password=u['password'], disname=u['disname'], profile=u['profile'], bound=u['bound'])
        db.session.add(user)
    
    musubis = [
      {'musubi_code': 'sun_to_jupiter', 'about': '孙婉宁和熊恺杰的测试小数据'},
    ]
    for m in musubis:
        musubi = Musubi(musubi_code=m['musubi_code'], about=m['about'])
        db.session.add(musubi)
    
    posts = [
      {'content': '第一条动态, 今天吃了好多', 'is_public': False, 'author_id': 1},
      {'content': '第二条动态, 昨天也吃了好多', 'is_public': False, 'author_id': 2},
      {'content': '第三条动态, 天天都吃了好多', 'is_public': False, 'author_id': 2},
      {'content': '今天好困啊阿啊', 'is_public': True, 'author_id': 2}
    ]
    for p in posts:
        post = Post(content=p['content'], is_public=p['is_public'], author_id=p['author_id'])
        db.session.add(post)
    
    bubblejars = [
      {'name': '第一个泡泡罐子', 'description': '测试数据', 'author_id': 1},
      {'name': '第二个泡泡罐子', 'description': '测试数据', 'author_id': 2}
    ]
    for b in bubblejars:
        bubblejar = BubbleJar(name=b['name'], description=b['description'], author_id=b['author_id'])
        db.session.add(bubblejar)
    
    bubbles = [
      {'title': '第一个泡泡', 'content': '测试数据啦啦啦', 'bubblejar_id': 1, 'author_id': 1},
      {'title': '第二个泡泡', 'content': '测试数据啦啦啦', 'bubblejar_id': 1, 'author_id': 1},
      {'title': '泡泡', 'content': '测试数据啦啦啦', 'bubblejar_id': 2, 'author_id': 2}
    ]
    for b in bubbles:
        bubble = Bubble(title=b['title'], content=b['content'], bubblejar_id=b['bubblejar_id'], author_id=b['author_id'])
        db.session.add(bubble)

    db.session.commit()
    click.echo('Done.')
