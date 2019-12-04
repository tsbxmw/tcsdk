import logging

from tcsdk.common import default
from tcsdk.exceptions import RequestError
from tcsdk.network import http
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
            req = http.Request(method, url, **kwargs)
            req.headers = self.headers_handler(req.headers)
            req.url = "{}{}".format(self.endpoint, req.url)
            res = self.session.do_request(req, self.time_out)
            if res.status // 100 != 2:
                raise RequestError(str(res.status))
            return res
        except Exception as e:
            logging.error(e)


class PerformanceApi(BaseApi):
    def __init__(self, auth, endpoint, session=None):
        self.auth = auth
        self.endpoint = endpoint
        self.session = session
        BaseApi.__init__(self, auth, endpoint, session)

    def create_task(self, name):
        task = Task(self.auth, self.endpoint, self.session, task_name=name)
        return task


class Task(BaseApi):
    def __init__(self, auth, endpoint, session=None, task_name="", label_name=None):
        self.task_name = task_name
        self.auth = auth
        self.endpoint = endpoint
        self.session = session
        self.labels = []

        BaseApi.__init__(self, auth, endpoint, session)

        res = self.create(task_name)
        self.task_id = res.json().get("data").get("task_id")
        if label_name:
            self.create_label(label_name)

    def create(self, task_name):
        res = self.request(default.TASK_INIT_API.method, default.TASK_INIT_API.url,
                           **default.TASK_INIT_API.request(task_name=task_name))
        return res

    def update(self, task_name):
        res = self.request(default.TASK_UPDATE_API.method, default.TASK_UPDATE_API.url,
                           **default.TASK_UPDATE_API.request(task_name=task_name))

    def create_label(self, name):
        label = Label(self.auth, self.endpoint, self.session, label_name=name, task_id=self.task_id)
        self.labels.append(label)
        return label


class Label(BaseApi):
    def __init__(self, auth, endpoint, session, label_name="", task_id=0):
        self.label_name = label_name
        self.auth = auth
        self.endpoint = endpoint
        self.session = session
        BaseApi.__init__(self, auth, endpoint, session)
        res = self.create(label_name, task_id)
        self.label_id = res.json().get("data").get("label_id")

    def create(self, label_name, task_id):
        res = self.request(default.LABEL_INIT_API.method, default.LABEL_INIT_API.url,
                           **default.LABEL_INIT_API.request(label_name=label_name, task_id=task_id))
        return res

    def update(self, label_name=""):
        res = self.request(default.LABEL_UPDATE_API.method, default.LABEL_UPDATE_API.url,
                           **default.LABEL_UPDATE_API.request(label_name=label_name))
