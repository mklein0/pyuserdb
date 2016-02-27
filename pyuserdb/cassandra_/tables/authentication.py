#
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.user import UserHasAccount


class AuthenticationUserTable(Model):
    """
    Authentication Lookup Table to leverage scaling of primary keys in Cassandra. Secondary Keys are node local and
    would require a full DC scan.

    https://pantheon.io/blog/cassandra-scale-problem-secondary-indexes

    """
    __table_name__ = 'authentication_user'

    username = columns.Text(primary_key=True)
    password = columns.Text()
    user_uuid = columns.UUID()

    accounts = columns.List(columns.UserDefinedType(UserHasAccount))

    last_logged_in_at = columns.DateTime()

    # Authentication related flags
    property_should_change_password = columns.Boolean(default=False)
