import logging

from tcsdk.common.api import BaseApi
from tcsdk.api.performance import config

logger = logging.getLogger(__name__)


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
        self.labels = {}

        BaseApi.__init__(self, auth, endpoint, session)

        res = self.create(task_name)
        self.task_id = res.json().get("data").get("task_id")
        if label_name:
            self.create_label(label_name)

    def create(self, task_name):
        res = self.request(config.TASK_INIT_API.method, config.TASK_INIT_API.url,
                           **config.TASK_INIT_API.request(task_name=task_name))
        return res

    def update(self, task_name):
        res = self.request(config.TASK_UPDATE_API.method, config.TASK_UPDATE_API.url,
                           **config.TASK_UPDATE_API.request(task_name=task_name))

    def create_label(self, name):
        label = Label(self.auth, self.endpoint, self.session, label_name=name, task_id=self.task_id)
        self.labels.update({name:label})
        return label

    def calculate_summary(self):
        res = self.request(config.TASK_SUMMARY_CALCULATE.method, config.TASK_SUMMARY_CALCULATE.url,
                           **config.TASK_SUMMARY_CALCULATE.request(task_id=self.task_id))
        return res


class Label(BaseApi):
    def __init__(self, auth, endpoint, session, label_name="", task_id=0):
        self.label_name = label_name
        self.auth = auth
        self.endpoint = endpoint
        self.session = session
        BaseApi.__init__(self, auth, endpoint, session)
        res = self.create(label_name, task_id)
        self.label_id = res.json().get("data").get("label_id")
        self.task_id = task_id

    def create(self, label_name, task_id):
        res = self.request(config.LABEL_INIT_API.method, config.LABEL_INIT_API.url,
                           **config.LABEL_INIT_API.request(label_name=label_name, task_id=task_id))
        return res

    def update(self, label_name=""):
        res = self.request(config.LABEL_UPDATE_API.method, config.LABEL_UPDATE_API.url,
                           **config.LABEL_UPDATE_API.request(label_name=label_name))
        return res

    def upload(self, **kwargs):
        check = config.LABEL_DATA_UPLOAD_API.check
        data = {}
        for key in kwargs:
            try:
                if key not in check:
                    continue
                data.update({key: check.get(key)(kwargs.get(key))})
            except Exception as e:
                logger.error(e)
                raise e
        data = config.LABEL_DATA_UPLOAD_API.request_without_none(task_id=self.task_id, label_id=self.label_id,
                                                                 label_name=self.label_name, **data)
        res = self.request(config.LABEL_DATA_UPLOAD_API.method, config.LABEL_DATA_UPLOAD_API.url,**data)
        return res.json().get("msg") == "success"

    def calculate_summary(self):
        res = self.request(config.LABEL_SUMMARY_CALCULATE.method, config.LABEL_SUMMARY_CALCULATE.url,
                           **config.LABEL_SUMMARY_CALCULATE.request(task_id=self.task_id, label_id=self.label_id))
        return res