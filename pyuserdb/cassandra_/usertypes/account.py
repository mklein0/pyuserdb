#
from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType


class AccountHasUser(UserType):
    user_uuid = columns.UUID()
    user_role = columns.Text()
