"""
commands.py
- provides a command line utility for interacting with the 
    application to perform interIdle debugging and setup
Created by Rosebud on 2022-06-13.
Copyright © 2022 Rosebud. All rights reserved.
"""

import sys, inspect
import click
from flask import Blueprint
from .models import User, Post, Comment, Like, BoardingPass
from .utils import Tools

cmd = Blueprint('cmd', __name__)


def str_to_class(classname):
    """Convert string variable to class object"""
    return getattr(sys.modules[__name__], classname)


def get_all_collections():
    """Get all classes as collections of database included in this module except 'Blueprint'"""
    class_name_list = []
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls_obj in clsmembers:
        class_name_list.append(cls_obj[0])
    class_name_list.remove('Blueprint')
    return class_name_list


def forge_test_bpcode():
    bps = [
        {"passcode": "passcodetest1", "pending_code": "not_pending_test1"},
        {"passcode": "passcodetest2", "pending_code": "not_pending_test2"},
    ]

    for b in bps:
        bpass = BoardingPass(passcode=b['passcode'], pending_code=b['pending_code'])
        bpass.save()


@cmd.cli.command()
@click.argument('pcode')
def forgebp(pcode):
    if pcode == 'forge':
        forge_test_bpcode()
        click.echo('Test boarding pass code added')
    else:
        check_bp = BoardingPass.objects(passcode=pcode).first()
        if check_bp:
            click.echo('code exists')
        else:
            default_pencode = 'not_pending_' + Tools.gen_random_code(16)
            new_bp = BoardingPass(passcode=pcode, pending_code=default_pencode)
            new_bp.save()
            click.echo('New boarding pass code added')



def forge_user():
    users = [
        {'uid': 'user_init_1', 'email': 'test1@test.com', 'username': 'rosebud_test', 'password': 'test123', 'name': 'RoseGod', 'profile': 'hello world', 'avatar_url': 'test.com', 'user_type': ['superadmin', 'user']},
        {'uid': 'user_init_2', 'email': 'test2@test.com', 'username': 'andy_test', 'password': 'test123', 'name': 'Andy', 'profile': 'hello', 'avatar_url': 'test.com', 'user_type': ['admin', 'user']},
        {'uid': 'user_init_3', 'email': 'test3@test.com', 'username': 'catt', 'password': 'test123', 'name': 'Cat', 'profile': 'meow', 'avatar_url': 'test.com', 'user_type': ['user']},
        {'uid': 'user_init_4', 'email': 'test4@test.com', 'username': 'doge', 'password': 'test123', 'name': 'Dog', 'profile': 'wooo', 'avatar_url': 'test.com', 'user_type': ['user']}
    ]

    for u in users:
        user = User(uid=u['uid'], email=u['email'], username=u['username'], name=u['name'], profile=u['profile'], avatar_url=u['avatar_url'], user_type=u['user_type'])
        user.hash_password(u['password'])
        user.save()


def forge_post():
    posts = [
        {'post_id': 'post_init_1', 'title': '🪐 B612星球的第一篇公开电报! 🎉', 'cover': 'https://picsum.photos/360/400?random=1', 'author_uid': 'user_init_1', 'author': '', 'content': '<p>五月初开始，荒废了快一年的个人主页终于重新开始施工了。所谓的个人主页，也不仅仅是“我自己的”主页，希望以后这里可以有小伙伴们一同玩耍，每个人都能拥有一颗属于自己的星球🌍。</p><p>困的不行了，我先睡一觉起来再好好写吧。</p><p>💤</p><br><br><br><br>', 'post_type': 'blog', 'is_public': True},
        {'post_id': 'post_init_2', 'title': '想吃好吃的', 'cover': 'https://picsum.photos/360/400?random=1', 'author_uid': 'user_init_1', 'author': '', 'content': '<p>想吃香辣鸡腿堡🍔</p><p>想吃嫩牛五方🌯</p><p>想吃烧烤🍢</p><p>想吃周黑鸭🐤</p>', 'post_type': 'blog', 'is_public': True},
    ]

    for p in posts:
        post = Post(post_id=p['post_id'], title=p['title'], cover=p['cover'], author_uid=p['author_uid'], author=p['author'], content=p['content'], post_type=p['post_type'], is_public=p['is_public'])
        post.save()


def forge_comment():
    comments = [
        {"comment_id": "comment_init_1", "comment_of": "post_init_1", "content": "well done boy", "author_uid": "user_init_3", "likes": "2324"},
        {"comment_id": "comment_init_2", "comment_of": "post_init_1", "content": "up up", "author_uid": "user_init_4", "likes": "322"}
    ]

    for c in comments:
        comment = Comment(comment_id=c['comment_id'], comment_of=c['comment_of'], content=c['content'], author_uid=c['author_uid'], likes=c['likes'])
        comment.save()


def forge_like():
    likes = [
        {"like_id": "like_init_1", "like_of": "post_init_1", "author_uid": "user_init_3"},
        {"like_id": "like_init_2", "like_of": "post_init_1", "author_uid": "user_init_4"},
        {"like_id": "like_init_3", "like_of": "post_init_1", "author_uid": "user_init_2"}
    ]

    for l in likes:
        like = Like(like_id=l['like_id'], like_of=l['like_of'], author_uid=l['author_uid'])
        like.save()


@cmd.cli.command()
@click.argument('collection_name')
def drop(collection_name):
    """Drop the specified collection"""

    if collection_name == 'all':
        collections = get_all_collections()
        for c in collections:
            str_to_class(c).drop_collection()
            click.echo('Collection {} dropped'.format(c))
    else:
        try:
            str_to_class(collection_name).drop_collection()
            click.echo('Collection {} dropped'.format(collection_name))
        except AttributeError:
            click.echo('Collection {} not exists'.format(collection_name))


@cmd.cli.command()
def forgedata():
    """Generate mockup data"""
    forge_user()
    click.echo('User data forged')
    forge_post()
    click.echo('Post data forged')
    forge_comment()
    click.echo('Comment data forged')
    forge_like()
    click.echo('Like data forged')
    click.echo('Done')


@cmd.cli.command()
def forgeuser():
    """Generate mockup user data"""
    forge_user()
    click.echo('User data forged')


@cmd.cli.command()
def forgepost():
    """Generate mockup post data"""
    forge_post()
    click.echo('Post data forged')


@cmd.cli.command()
def forgecomment():
    """Generate mockup comment data"""
    forge_comment()
    click.echo('Comment data forged')


@cmd.cli.command()
def forgelike():
    """Generate mockup like data"""
    forge_like()
    click.echo('Like data forged')

