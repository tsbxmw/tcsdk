import logging
import requests
from requests.adapters import HTTPAdapter
from requests.structures import CaseInsensitiveDict


import tcsdk.common.default as default
from tcsdk.exceptions import RequestError
from tcsdk.utils import Utils

logger = logging.getLogger(__name__)


class Session(object):
    def __init__(self):
        self.session = requests.Session()
        pool_size = default.http_session_size
        self.session.mount('http://', HTTPAdapter(pool_connections=pool_size, pool_maxsize=pool_size))
        self.session.mount('https://', HTTPAdapter(pool_connections=pool_size, pool_maxsize=pool_size))

    def do_request(self, req, timeout):
        try:
            logger.debug("send request : method {}, url {}, params {}, headers {}, timeout {}".format(
                req.method,
                req.url,
                req.params,
                req.headers,
                timeout
            ))
            response = Response(
                self.session.request(req.method, req.url, json=req.data, params=req.params, headers=req.headers,
                                     timeout=timeout))
            logger.debug("do_request here get the response : {}".format(response))
            return response
        except requests.RequestException as e:
            logger.error(e)
            raise RequestError(e)
        except Exception as ee:
            logger.error(ee)


class Request(object):
    def __init__(self, method, url, data=None, params=None, headers=None):
        self.method = method
        self.url = url

        self.data = Utils.convert_request_body(data)
        self.params = params or {}

        if not isinstance(headers, CaseInsensitiveDict):
            self.headers = CaseInsensitiveDict(headers)
        else:
            self.headers = headers

        if 'Accept-Encoding' not in self.headers:
            self.headers['Accept-Encoding'] = None

        if 'User-Agent' not in self.headers:
            self.headers['User-Agent'] = default.USER_AGENT

        logger.debug("init request : method {}, url {}, params {}, headers {}".format(
            self.method,
            self.url,
            self.params,
            self.headers
        ))


class Response(object):
    def __init__(self, response):
        self.response = response
        self.status = response.status_code
        self.headers = response.headers
        self.request_id = response.headers.get(default.REQUEST_ID, '')
        self._all_read = False
        logger.debug("Get response headers, req-id:{0}, status: {1}, headers: {2}".format(self.request_id, self.status,
                                                                                          self.headers))

    def read(self):
        if self._all_read:
            return b''
        self._all_read = True
        return self.response.content

    def json(self):
        try:
            return self.response.json()
        except Exception as e:
            logger.error(e)
            return {}

    def __str__(self):
        return str(self.response.json())
