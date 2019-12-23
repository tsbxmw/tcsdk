import logging
import time

from tcsdk.common import default
from tcsdk.exceptions import RequestError
from tcsdk.network import http
from tcsdk.network.http import ApiModel
from tcsdk.utils import Utils

logger = logging.getLogger(__name__)


class BaseApi(object):
    def __init__(self, auth, endpoint, session=None):
        self.auth = auth
        self.endpoint = Utils.normalize_endpoint(endpoint.strip())
        self.session = session or http.Session()
        self.time_out = default.connect_timeout

    def headers_handler(self, headers):
        headers.update(self.auth.sing_in_headers())
        headers.update(Utils.version_to_headers())
        return headers

    def request(self, method, url, **kwargs):
        try:
            begin_time = time.time()
            req = http.Request(method, url, **kwargs)
            req.headers = self.headers_handler(req.headers)
            req.url = "{}{}".format(self.endpoint, req.url)
            res = self.session.do_request(req, self.time_out)
            end_time = time.time()
            logger.debug("request using time : {} seconds".format(end_time - begin_time))
            if res.status // 100 != 2:
                raise RequestError(str(res.status))
            return res
        except Exception as e:
            logger.error(e)

