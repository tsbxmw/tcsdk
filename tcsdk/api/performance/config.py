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
                                     "task_id": int, "label_id": int, "label_name": str, "fps": float,
                                     "cpu_total": float, "cpu_app": float, "memory_total": float,
                                     "memory_virtual": float,
                                     "memory_real": float, "network_send": float, "network_receive": float,
                                     "gpu_rendor": float,
                                     "gpu_tiler": float, "gpu_device": float, "c_switch": float,
                                     "battery_current": float,
                                     "battery_power": float, "battery_voltage": float, "screen_shot": float
                                 }),
                                 dict(response={"data": {"result": str}}),
                                 check={
                                     "task_id": int, "label_id": int, "label_name": str, "fps": float,
                                     "cpu_total": float, "cpu_app": float, "memory_total": float,
                                     "memory_virtual": float,
                                     "memory_real": float, "network_send": float, "network_receive": float,
                                     "gpu_rendor": float,
                                     "gpu_tiler": float, "gpu_device": float, "c_switch": float,
                                     "battery_current": float,
                                     "battery_power": float, "battery_voltage": float, "screen_shot": str
                                 })

LABEL_SUMMARY_CALCULATE = ApiModel("/v1/data/label/calsummary",
                                   default.POST_METHOD,
                                   dict(data={
                                       "task_id": int, "label_id": int
                                   }),
                                   dict(response={"data": dict}))

TASK_SUMMARY_CALCULATE = ApiModel("/v1/data/task/calsummary",
                                  default.POST_METHOD,
                                  dict(data={
                                      "task_id": int
                                  }),
                                  dict(response={"data": dict}))

APP_INIT = ApiModel("/v1/data/task/app",
                    default.POST_METHOD,
                    dict(data={
                        "name": str, "version": str, "package": str, "extention": str,
                        "remark": str, "task_id": int
                    }),
                    dict(response={"data": dict}),
                    check={
                        "name": str, "version": str, "package": str, "extention": str,
                        "remark": str, "task_id": int
                    })

DEVICE_INIT = ApiModel("/v1/data/task/device",
                       default.POST_METHOD,
                       dict(data={
                           "name": str, "task_id": int, "cpu": str, "gpu": str, "type": str,
                           "os": str, "cpu_type": str, "cpu_arch": str, "cpu_core_number": int,
                           "cpu_frequency": str, "ram": str, "rom": str
                       }),
                       dict(response={"data": dict}),
                       check={
                           "name": str, "task_id": int, "cpu": str, "gpu": str, "type": str,
                           "os": str, "cpu_type": str, "cpu_arch": str, "cpu_core_number": int,
                           "cpu_frequency": str, "ram": str, "rom": str
                       })
