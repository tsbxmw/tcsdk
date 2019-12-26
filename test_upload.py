from tcsdk import *
from random import randint

if __name__ == "__main__":
    auth = Auth("3e01f88a", "8078244a-c575-49")
    api = PerformanceApi(auth=auth, endpoint="http://tcloud-api-dev.ywopt.com")
    task = api.create_task("test_5")
    assert task.task_id != 0

    label = task.create_label("test_6")
    assert label.label_id != 0

    for i in range(100):
        data = dict(
            fps=randint(1, 60),
            cpu_total=randint(40, 100),
            cpu_app=randint(1, 40),
            memory_real=randint(100, 4000),
            memory_total=randint(100, 4000),
            memory_virtual=randint(100, 1000),
            network_send=randint(1, 40000),
            network_receive=randint(1, 40000),
            gpu_rendor=randint(40, 100),
            gpu_tiler=randint(1, 40),
            gpu_device=randint(1, 40)
        )

        assert label.upload(**data) is True
    label.calculate_summary()
    task.calculate_summary()
    task.app_init(name="test", version="0.0.1")
    task.device_init(name="test")

