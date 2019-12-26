from tcsdk.api import PerformanceApi, Task, Label
from tcsdk.auth import Auth
from tcsdk.common.log import logger, init_logger
from tcsdk.common import *


init_logger()

PerformanceApi = PerformanceApi
PerformanceApiTask = Task
PerformanceApiLabel = Label

Auth = Auth
