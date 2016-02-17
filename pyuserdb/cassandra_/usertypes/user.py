#
from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType


class Address(UserType):
    role = columns.Text()

    street = columns.Text()
    city = columns.Text()
    zip_code = columns.Text()

    # Province / Prefecture / State
    province = columns.Text()
    # Local region / County
    local_region = columns.Text()
    # Block / Neighborhood in City
    neighborhood = columns.Text()


class PhoneNumber(UserType):
    role = columns.Text()
    phone_type = columns.Text()
    country_code = columns.SmallInt()
    number = columns.Integer()
    extension = columns.Integer()


class UserHasAccount(UserType):
    account_name = columns.Text()
    account_uuid = columns.UUID()
