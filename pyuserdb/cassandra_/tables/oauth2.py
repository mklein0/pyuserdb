#
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class OAuth2ClientTable(Model):

    client_id = columns.Text(primary_key=True)
    client_secret = columns.Text()
    client_type = columns.Text()
    redirect_uri = columns.Text()

    home_page = columns.Text()
    email = columns.Text()

    name = columns.Text()

    created_at = columns.DateTime()
    updated_at = columns.DateTime()


# Temporary State 

class OAuth2AuthorizationGrantTable(Model):
    """
    """
    authorization_code = columns.Text(primary_key=True)
    client_id = columns.Text()
    user_uuid = columns.UUID()

    created_at = columns.DateTime()
    valid_until = columns.DateTime()

    redirect_uri = columns.Text()
    valid_until = columns.DateTime()
    scope = columns.Text()


class OAuth2RefreshTokenTable(Model):
    refresh_token = columns.Text(primary_key=True)
    client_id = columns.Text()
    user_uuid = columns.Text()

    scope = columns.Text()
    valid_until = columns.DateTime()
    access_token = columns.Text()


class OAuth2AccessTokenTable(Model):

    access_token = columns.Text(primary_key=True)
    user_uuid = columns.Text()
    client_id = columns.Text()

    scope = columns.Text()
    valid_until = columns.DateTime()
