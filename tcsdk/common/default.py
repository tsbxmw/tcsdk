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
FIX_VERSION = 1
TCSDK_VERSION = "{}.{}.{}".format(MAIN_VERSION, SUB_VERSION, FIX_VERSION)

# request method
GET_METHOD = "get"
POST_METHOD = "post"
DELETE_METHOD = "put"
PUT_METHOD = "put"


# api url

class ApiModel(object):
    def __init__(self, url, method, request={}, response={}):
        self.url = url
        self.method = method
        self.request_kwargs = request
        self.response_kwargs = response

    def request(self, **kwargs):
        temp = {}
        for key in self.request_kwargs:
            temp[key] = {}
            data = kwargs.get(key, kwargs)
            template = self.request_kwargs.get(key)
            for t_key in template:
                temp[key][t_key] = template.get(t_key)(data.get(t_key))
        return temp


# all api desing like this: url, method, **kwargs

TASK_INIT_API = ApiModel("/v1/data/task",
                         POST_METHOD,
                         dict(data={"task_name": str}),
                         dict(response={"data": {"task_id": int, "task_name": str}}))
TASK_UPDATE_API = ApiModel("/v1/data/task",
                           PUT_METHOD,
                           dict(data={"task_name": str}),
                           dict(response={"data": {"task_id": int, "task_name": str}}))
HEALTH_CHECK_API = ApiModel("/v1/health",
                            GET_METHOD)
LABEL_INIT_API = ApiModel("/v1/data/label",
                          POST_METHOD,
                          dict(data={"label_name": str, "task_id": int}),
                          dict(response={"data": {"task_id": int, "label_name": str}}))
LABEL_UPDATE_API = ApiModel("/v1/data/label",
                            PUT_METHOD,
                            dict(data={"label_name": str}),
                            dict(response={"data": {"task_id": int, "label_name": str}}))
