#
import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from pyuserdb.cassandra_.usertypes.oauth2 import ClientType


class OAuth2ClientTable(Model):
    __table_name__ = 'oauth2_client'

    client_id = columns.Text(primary_key=True)
    client_secret = columns.Text()
    client_type = columns.Text(default=ClientType.MOBILE)
    redirect_uri = columns.Text()
    redirect_uris = columns.List(columns.Text())

    home_page = columns.Text()
    email = columns.Text()

    name = columns.Text()

    created_at = columns.DateTime(default=datetime.datetime.utcnow)
    updated_at = columns.DateTime(default=datetime.datetime.utcnow)


# Temporary State 

class OAuth2GrantAuthorizationTable(Model):
    """
    """
    __table_name__ = 'oauth2_grant_authorization'

    authorization_code = columns.Text(primary_key=True)
    client_id = columns.Text()
    user_uuid = columns.UUID()

    created_at = columns.DateTime(default=datetime.datetime.utcnow)
    valid_until = columns.DateTime()

    redirect_uri = columns.Text()
    scope = columns.List(columns.Text())
    state = columns.Text()


class OAuth2TokenRefreshTable(Model):
    __table_name__ = 'oauth2_token_refresh'

    refresh_token = columns.Text(primary_key=True)
    client_id = columns.Text()
    user_uuid = columns.UUID()

    scope = columns.List(columns.Text())
    valid_until = columns.DateTime()
    access_token = columns.Text()


class OAuth2TokenAccessTable(Model):
    __table_name__ = 'oauth2_token_access'

    access_token = columns.Text(primary_key=True)
    user_uuid = columns.UUID()
    client_id = columns.Text()

    scope = columns.List(columns.Text())
    valid_until = columns.DateTime()