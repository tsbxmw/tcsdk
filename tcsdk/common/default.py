# coding=utf-8
import logging
import platform


def get(value, default_value):
    if value is None:
        return default_value
    else:
        return value


#: connect timeout seconds
connect_timeout = 60

#: request retry times
request_retries = 3

#: session pool size
http_session_size = 10

# headers

USER_AGENT = 'tcsdk-python/{}/{}/{}/{}'.format(platform.system(), platform.release(), platform.machine(),
                                               platform.python_version())

REQUEST_ID = 'x-tcsdk-request-id'
CODE = 'code'
MESSAGE = 'message'
HEADER_SDK_VERSION = 'sdk_version'
NAME = "tcsdk"
LOGGER_LEVEL = logging.DEBUG

# exceptions
CLIENT_ERROR = 1000
SERVER_ERROR = 1001
REQUEST_ERROR = 1002

# endpoint
ENDPOINT_TYPE_IP = 2001
ENDPOINT_TYPE_CNAME = 2002

# version info
MAIN_VERSION = 0
SUB_VERSION = 0
FIX_VERSION = 6
TCSDK_VERSION = "{}.{}.{}".format(MAIN_VERSION, SUB_VERSION, FIX_VERSION)

# request method
GET_METHOD = "get"
POST_METHOD = "post"
DELETE_METHOD = "put"
PUT_METHOD = "put"

# LOGO
TCSDK_LOGO = (
"""
_____  ___     
  |   /       
  |   \ __ loud 
<<<<<{}.{}.{}>>>>> 
""".format(MAIN_VERSION, SUB_VERSION, FIX_VERSION)
)

