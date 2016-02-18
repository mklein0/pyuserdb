#
from pyuserdb.utils import class_to_name

from pyuserdb.cassandra_.tables import (
    user as tables_user,
    account as tables_account,
    authentication as tables_auth,
    oauth2 as tables_oauth2
)


class User(tables_user.UserTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: uuid={} username={}>'.format(
            class_name, self.user_uuid, self.username)


class Account(tables_account.AccountTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: uuid={} name={}>'.format(
            class_name, self.account_uuid, self.account_name)


class AuthenticationUser(tables_auth.AuthenticationUserTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: uuid={} username={}>'.format(
            class_name, self.user_uuid, self.username)


class OAuth2Client(tables_oauth2.OAuth2ClientTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: client_id={}>'.format(
            class_name, self.client_id)


class OAuth2AuthorizationGrant(tables_oauth2.OAuth2AuthorizationGrantTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: auth_code={}>'.format(
            class_name, self.authorization_code)


class OAuth2RefreshToken(tables_oauth2.OAuth2RefreshTokenTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: refresh_token={}>'.format(
            class_name, self.refresh_token)


class OAuth2AccessToken(tables_oauth2.OAuth2AccessTokenTable):

    def __repr__(self):
        class_name = class_to_name(type(self))
        return '<{}: access_token={}>'.format(
            class_name, self.access_token)
