#
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.user import UserHasAccount


class UserAuthenticationTable(Model):

    username = columns.Text(primary_key=True)
    password = columns.Text()
    user_uuid = columns.UUID()

    accounts = columns.List(columns.UserDefinedType(UserHasAccount))

    last_logged_in_at = columns.DateTime()

    # Authentication related flags
    should_change_password = columns.Boolean(default=False)
