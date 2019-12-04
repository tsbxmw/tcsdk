from tcsdk.common import default
from tcsdk.network.http import ApiModel

# all api desing like this: url, method, ** kwargs


TASK_INIT_API = ApiModel("/v1/data/task",
                         default.POST_METHOD,
                         dict(data={"task_name": str}),
                         dict(response={"data": {"task_id": int, "task_name": str}}))

TASK_UPDATE_API = ApiModel("/v1/data/task",
                           default.PUT_METHOD,
                           dict(data={"task_name": str}),
                           dict(response={"data": {"task_id": int, "task_name": str}}))

HEALTH_CHECK_API = ApiModel("/v1/health",
                            default.GET_METHOD)

LABEL_INIT_API = ApiModel("/v1/data/label",
                          default.POST_METHOD,
                          dict(data={"label_name": str, "task_id": int}),
                          dict(response={"data": {"task_id": int, "label_name": str}}))

LABEL_UPDATE_API = ApiModel("/v1/data/label",
                            default.PUT_METHOD,
                            dict(data={"label_name": str}),
                            dict(response={"data": {"task_id": int, "label_name": str}}))

LABEL_DATA_UPLOAD_API = ApiModel("/v1/data/upload",
                                 default.POST_METHOD,
                                 dict(data={
                                     "task_id": int, "label_id": int, "label_name": str, "fps": str,
                                     "cpu_total": str, "cpu_app": str, "memory_total": str,
                                     "memory_virtual": str,
                                     "memory_real": str, "network_send": str, "network_receive": str,
                                     "gpu_rendor": str,
                                     "gpu_tiler": str, "gpu_device": str, "c_switch": str,
                                     "battery_current": str,
                                     "battery_power": str, "battery_voltage": str, "screen_shot": str
                                 }),
                                 dict(response={"data": {"result": str}}),
                                 check={
                                     "task_id": int, "label_id": int, "label_name": str, "fps": int,
                                     "cpu_total": float, "cpu_app": float, "memory_total": float,
                                     "memory_virtual": float,
                                     "memory_real": float, "network_send": float, "network_receive": float,
                                     "gpu_rendor": float,
                                     "gpu_tiler": float, "gpu_device": float, "c_switch": float,
                                     "battery_current": float,
                                     "battery_power": float, "battery_voltage": float, "screen_shot": str
                                 })
