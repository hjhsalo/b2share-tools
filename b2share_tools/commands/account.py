# -*- coding: utf-8 -*-

import click
from flask.cli import with_appcontext

from invenio_db import db
from invenio_accounts.models import User
from flask_security.utils import encrypt_password
from flask import current_app
from flask_login import current_user

from urllib.parse import urlunsplit

from invenio_oauth2server import current_oauth2server
from invenio_oauth2server.models import Token


def abort_if_false(ctx, param, value):
    """Abort command is value is False."""
    if not value:
        ctx.abort()


@click.group()
def account():
    """B2SHARE records related commands."""


@account.command('add-service-account')
@with_appcontext
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('-u', '--update', is_flag=True, default=False,
              help='updates if necessary')
@click.argument('name', nargs=1, required=True)
@click.argument('token-name', nargs=1, required=False, default='SRV_ACCOUNT_TOKEN')
def add_service_account(verbose, update, name, token_name):
    """
    Add service account.
    This account cannot be used to login.
    Usage only via token.
    """

    passwd = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

    user_info = {
        'id': None,
        'name': name,
        'email': name + '@b2share.serviceaccount.b2share',
        'password': passwd,
    }

    # TODO: Check if user exists

    # Create user
    with db.session.begin_nested():
        accounts = current_app.extensions['invenio-accounts']
        user = accounts.datastore.create_user(
            email=user_info.get('email'),
            active=True,
        )
        db.session.add(user)
        user_info['id'] = user.id
        user_info['user'] = user

    base_url = urlunsplit((
            current_app.config.get('PREFERRED_URL_SCHEME', 'http'),
            # current_app.config['SERVER_NAME'],
            current_app.config['JSONSCHEMAS_HOST'],
            current_app.config.get('APPLICATION_ROOT') or '', '', ''
    ))

    # Create token
    with current_app.test_request_context('/', base_url=base_url):
        current_app.login_manager.reload_user(user_info['user'])
        scopes = current_oauth2server.scope_choices()
        token = Token.create_personal(
                    token_name, current_user.get_id(), scopes=[s[0] for s in scopes]
                )
        db.session.commit()
        click.secho(token.access_token)
        click.secho(user_info.get('email'))
