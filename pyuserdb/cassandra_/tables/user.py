#
import uuid
import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.user import Address, PhoneNumber, UserHasAccount


class UserTable(Model):
    user_uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_state = columns.Text(default='created')

    created_at = columns.DateTime(default=datetime.datetime.utcnow)
    updated_at = columns.DateTime(default=datetime.datetime.utcnow)
    last_login_at = columns.DateTime()

    username = columns.Text()
    password = columns.Text()

    firstname = columns.Text()
    lastname = columns.Text()
    display_name = columns.Text()

    email = columns.Text()
    primary_phone = columns.UserDefinedType(PhoneNumber)
    phone_numbers = columns.List(columns.UserDefinedType(PhoneNumber))

    accounts = columns.List(columns.UserDefinedType(UserHasAccount))
