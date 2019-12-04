import logging

logger = logging.getLogger(__name__)


class AuthBase(object):
    def __init__(self, access_key_id, access_key_secret):
        self.key = access_key_id.strip()
        self.secret = access_key_secret.strip()


class Auth(AuthBase):
    '''here to sign the key and secret'''

    def __init__(self, key, secret):
        AuthBase.__init__(self, key, secret)

    def sign(self):
        return

    def sing_in_headers(self):
        return {
            "key": self.key,
            "secret": self.secret,
            "Content-Type": "application/json"
        }
