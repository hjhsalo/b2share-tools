# -*- coding: utf-8 -*-

import click
from flask.cli import with_appcontext

from invenio_db import db
from invenio_pidstore.models import PersistentIdentifier
from invenio_records_files.api import Record


def abort_if_false(ctx, param, value):
    """Abort command is value is False."""
    if not value:
        ctx.abort()


@click.group()
def record():
    """B2SHARE administrative commands."""


@record.command('remove')
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('--yes-i-know', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Do you know that you are going to remove a record permanently?')
@click.argument('record-pid', nargs=1, required=True)
def remove_record(verbose, yes_i_know, record_pid):
    """
    Remove a record.
    """

    # Fetch record
    if verbose:
        click.secho('Fetching record with b2rec UUID {}'.format(record_pid))

    rec_pid = PersistentIdentifier.get('b2rec', record_pid)
    record = Record.get_record(rec_pid.object_uuid)
    
    if record:
        # Fetch PIDs of record
        pids = PersistentIdentifier.query.filter_by(object_type='rec', object_uuid=rec_pid.object_uuid).all()

        if not pids:
            click.secho('No PIDs found for with b2rec UUID {}'.format(record_pid))

        # Mark record as deleted

        if verbose:
            click.secho('Following record (and PIDs) were found:')
            click.secho(record)

            if pids:
                for pid in pids:
                    click.secho(pid)
            
        if yes_i_know:
            if verbose:
                click.secho('Deleting recods (and PIDs):')
            
            record.delete()

            if pids:
                # Delete PIDs
                for pid in pids:
                    pid.unassign()
                    pid.delete()
            
            # Commit changes
            db.session.commit()

    else:
        click.secho('No record found with b2rec UUID {}'.format(record_pid))
    
