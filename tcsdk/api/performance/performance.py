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

    def app_init(self, **kwargs):
        """
        {
            "name": str, "version": str, "package": str, "extention": str,
            "remark": str
        }
        """
        check = config.APP_INIT.check
        data = {}
        for key in kwargs:
            try:
                if key not in check:
                    continue
                data.update({key: check.get(key)(kwargs.get(key))})
            except Exception as e:
                logger.error(e)
                raise e
        data = config.APP_INIT.request_without_none(task_id=self.task_id, **data)
        res = self.request(config.APP_INIT.method, config.APP_INIT.url, **data)
        return res.json().get("msg") == "success"

    def device_init(self, **kwargs):
        """
        {
           "name": str, "cpu": str, "gpu": str, "type": str,
           "os": str, "cpu_type": str, "cpu_arch": str, "cpu_core_number": int,
           "cpu_frequency": str, "ram": str, "rom": str
        }
        """
        check = config.DEVICE_INIT.check
        data = {}
        for key in kwargs:
            try:
                if key not in check:
                    continue
                data.update({key: check.get(key)(kwargs.get(key))})
            except Exception as e:
                logger.error(e)
                raise e
        data = config.DEVICE_INIT.request_without_none(task_id=self.task_id, **data)
        res = self.request(config.DEVICE_INIT.method, config.DEVICE_INIT.url, **data)
        return res.json().get("msg") == "success"


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
        """{
         "task_id": int, "label_id": int, "label_name": str, "fps": float,
         "cpu_total": float, "cpu_app": float, "memory_total": float,
         "memory_virtual": float,
         "memory_real": float, "network_send": float, "network_receive": float,
         "gpu_rendor": float,
         "gpu_tiler": float, "gpu_device": float, "c_switch": float,
         "battery_current": float,
         "battery_power": float, "battery_voltage": float, "screen_shot": float
        }
        """
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