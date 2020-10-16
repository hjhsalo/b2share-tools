# -*- coding: utf-8 -*-

"""B2share tools extension"""

from __future__ import absolute_import, print_function

import click

from .commands import record as record_cmd

@click.group()
def b2tools():
    """Demonstration commands."""

class B2ShareTools(object):
    """B2Share tools extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['b2share-tools'] = self
        b2tools.add_command(record_cmd)
        app.cli.add_command(b2tools)

    def init_config(self, app):
        """Initialize configuration."""
        pass