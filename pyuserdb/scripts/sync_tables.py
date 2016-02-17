#
"""
Sync the Cassandra Table definitions
"""
import os
import textwrap
import inspect
import argparse
import logging

from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model

from cassandra.cqlengine.management import sync_table, CQLENG_ALLOW_SCHEMA_MANAGEMENT

from pyuserdb.cassandra_ import models


log = logging.getLogger(__name__)


def is_cqlengine_model(obj):
    """

    :param Any obj: Object to test if a CQL Engine Model.

    :return: True if object given is an instance of a CQL Engine Model.
    :rtype: bool
    """
    return inspect.isclass(obj) and issubclass(obj, Model)


def sync_all_tables():
    """
    Determine all the Cassandra Tables in module and update tables.
    """
    for _, cls in inspect.getmembers(models, predicate=is_cqlengine_model):
        log.info('Syncing %r', cls)
        sync_table(cls)


def setup_connection(host, keyspace):
    # Connect to the keyspace on our cluster
    connection.setup([host], keyspace,  protocol_version=3)

    session = connection.session
    rsp = session.execute('SELECT * FROM system_schema.keyspaces WHERE keyspace_name=%s', (keyspace,))
    if len(rsp.current_rows) < 1:
        # Keyspace does not exist.
        msg = textwrap.dedent("""\
        Keyspace '{0}' does not exist.

        In CQLSH try executing the following:

        CREATE KEYSPACE {0} WITH replication = {{
            'class': 'SimpleStrategy',
            'replication_factor': '1'
        }};
        """.format(keyspace))
        raise ValueError(msg)


def main(argv=None):
    """
    :param list[str] argv: Command line Arguements
    """
    parser = argparse.ArgumentParser(description='Update cassandra cluster with latest DB table schemas.')
    parser.add_argument('-H', '--host', required=True, action='store')
    parser.add_argument('-K', '--keyspace', required=True, action='store')
    parser.add_argument('-n', '--dryrun', action='store_true')

    args = parser.parse_args(args=argv)

    logging.basicConfig(level=logging.INFO)

    # Set override flag to allow schema updates.
    os.environ[CQLENG_ALLOW_SCHEMA_MANAGEMENT] = '1'

    setup_connection(args.host, args.keyspace)
    sync_all_tables()