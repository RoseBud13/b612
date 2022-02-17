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
from coreEngine.models import db, Musubi

cmd = Blueprint('cmd', __name__)


@cmd.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')