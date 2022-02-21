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
from coreEngine.models import db, Musubi, Reiteki, Post, BubbleJar, Bubble

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

    reitekis = [
      {'musubi_code': 'sun_to_jupiter', 'username': 'wanning', 'password': '123123', 'disname': '孙婉宁', 'profile': '我喜欢熊恺杰', 'bound': 1},
      {'musubi_code': 'sun_to_jupiter', 'username': 'kaijie', 'password': '123123', 'disname': '熊恺杰', 'profile': '我喜欢孙婉宁', 'bound': 1},
    ]
    for r in reitekis:
        reiteki = Reiteki(musubi_code=r['musubi_code'], username=r['username'], password=r['password'], disname=r['disname'], profile=r['profile'], bound=r['bound'])
        db.session.add(reiteki)
    
    musubis = [
      {'musubi_code': 'sun_to_jupiter', 'about': '孙婉宁和熊恺杰的测试小数据'},
    ]
    for m in musubis:
        musubi = Musubi(musubi_code=m['musubi_code'], about=m['about'])
        db.session.add(musubi)
    
    posts = [
      {'content': '第一条动态, 今天吃了好多', 'author_id': 1},
      {'content': '第二条动态, 昨天也吃了好多', 'author_id': 2},
      {'content': '第三条动态, 天天都吃了好多', 'author_id': 2}
    ]
    for p in posts:
        post = Post(content=p['content'], author_id=p['author_id'])
        db.session.add(post)
    
    bubblejars = [
      {'name': '第一个泡泡罐子', 'description': '测试数据', 'author_id': 1}
    ]
    for b in bubblejars:
        bubblejar = BubbleJar(name=b['name'], description=b['description'], author_id=b['author_id'])
        db.session.add(bubblejar)
    
    bubbles = [
      {'title': '第一个泡泡', 'content': '测试数据啦啦啦', 'bubblejar_id': 1, 'author_id': 1},
      {'title': '第二个泡泡', 'content': '测试数据啦啦啦', 'bubblejar_id': 1, 'author_id': 1},
    ]
    for b in bubbles:
        bubble = Bubble(title=b['title'], content=b['content'], bubblejar_id=b['bubblejar_id'], author_id=b['author_id'])
        db.session.add(bubble)

    db.session.commit()
    click.echo('Done.')
