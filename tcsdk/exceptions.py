
import tcsdk.common.default
from tcsdk.common import default


class BaseError(Exception):
    def __init__(self, status, headers, body, details):
        self.status = status
        self.request_id = headers.get(default.REQUEST_ID, '')
        self.body = body
        self.details = details
        self.code = self.details.get(default.CODE, '')
        self.message = self.details.get(default.MESSAGE, '')

    def __str__(self):
        error = {
            "status": self.status,
            default.REQUEST_ID: self.request_id,
            "details": self.details
        }
        return str(error)

    def _str_body(self):
        error = {
            "status": self.status,
            default.REQUEST_ID: self.request_id,
            "details": self.details,
            "body": self.body
        }
        return str(error)


class ClientError(BaseError):
    def __init__(self, message):
        BaseError.__init__(self, default.CLIENT_ERROR, {}, 'Client Error: '+message, {})

    def __str__(self):
        return self._str_body()


class ServerError(BaseError):
    def __init__(self, message):
        BaseError.__init__(self, default.SERVER_ERROR, {}, 'Server Error: '+message, {})

    def __str__(self):
        return self._str_body()


class RequestError(BaseError):
    def __init__(self, message):
        BaseError.__init__(self, default.REQUEST_ERROR, {}, 'Request Error: '+message, {})

    def __str__(self):
        return self._str_body()