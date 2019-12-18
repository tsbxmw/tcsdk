from random import randint

from tcsdk import *


if __name__ == "__main__":
    auth = Auth("bdd222a1", "9413649b-d490-4d")
    api = Api(auth=auth, endpoint="http://122.51.145.198:9030")
    task = api.create_task("test_for_sdk_111")
    assert task.task_id != 0

    label = task.create_label("test_for_sdk11")
    assert label.label_id != 0

    for i in range(10):
        data = dict(
            fps=randint(1, 60),
            cpu_total=randint(40, 100),
            cpu_app = randint(1,40),
            memory_real=randint(100, 4000),
            memory_total = randint(100,4000),
            memory_virtual=randint(100, 1000),
            network_send = randint(1,40000),
            network_receive=randint(1, 40000),
            gpu_rendor = randint(40,100),
            gpu_tiler = randint(1,40),
            gpu_device = randint(1,40)
        )

        assert label.upload(**data) is True