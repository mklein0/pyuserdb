#
import uuid
import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.account import AccountHasUser


class AccountTable(Model):

    __table_name__ = "account"

    account_uuid = columns.UUID(primary_key=True, default=uuid.uuid4)
    account_name = columns.Text()

    email = columns.Text()

    users = columns.List(columns.UserDefinedType(AccountHasUser))

    created_at = columns.DateTime(default=datetime.datetime.utcnow)
    updated_at = columns.DateTime(default=datetime.datetime.utcnow)
