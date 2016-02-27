#
import uuid
import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.user import UserState, PhoneNumber, UserHasAccount


class UserTable(Model):
    """
    Authoritative record on User Data. Authentication Lookup is handle via a separate table for performance reasons.

    State flags like need to change password are held in authentication tables.
    """
    __table_name__ = "user"

    user_uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_state = columns.Text(default=UserState.CREATED)

    created_at = columns.DateTime(default=datetime.datetime.utcnow)
    updated_at = columns.DateTime(default=datetime.datetime.utcnow)
    last_login_at = columns.DateTime()

    username = columns.Text()
    password = columns.Text()

    first_name = columns.Text()
    last_name = columns.Text()
    display_name = columns.Text()

    email = columns.Text()
    # primary_phone = columns.UserDefinedType(
    #     PhoneNumber, default=lambda: PhoneNumber(role='', phone_type='', country_code='', number='', extension=''))
    phone_numbers = columns.List(columns.UserDefinedType(PhoneNumber))

    accounts = columns.List(columns.UserDefinedType(UserHasAccount))
