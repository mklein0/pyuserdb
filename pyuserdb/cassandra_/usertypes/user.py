#
from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType


class UserState(object):
    CREATED = 'created'
    ACTIVE = 'active'
    SUSPENDED = 'suspended'
    DELETED = 'deleted'


class PhoneNumberRole(object):
    HOME = 'home'
    WORK = 'work'
    MOBILE = 'mobile'


class PhoneNumberPhoneType(object):
    LANDLINE = 'landline'
    MOBILE = 'mobile'
    SATELITE = 'satelite'


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
    role = columns.Text(default='')
    phone_type = columns.Text(default='')
    country_code = columns.Text(default='')
    number = columns.Text(default='')
    extension = columns.Text(default='')


class UserHasAccount(UserType):
    account_name = columns.Text()
    account_uuid = columns.UUID()
