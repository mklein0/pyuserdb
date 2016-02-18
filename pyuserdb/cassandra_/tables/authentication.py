#
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.user import UserHasAccount


# TODO: Why not use a secondary index for username/authentication lookup?

class AuthenticationUserTable(Model):
    """
    """
    __table_name__ = 'authentication_user'

    username = columns.Text(primary_key=True)
    password = columns.Text()
    user_uuid = columns.UUID()

    accounts = columns.List(columns.UserDefinedType(UserHasAccount))

    last_logged_in_at = columns.DateTime()

    # Authentication related flags
    should_change_password = columns.Boolean(default=False)
