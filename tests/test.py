from tcsdk import *


if __name__ == "__main__":
    auth = Auth("bdd222a1", "9413649b-d490-4d")
    api = Api(auth=auth, endpoint="http://122.51.145.198:9030")
    task = api.create_task("test_for_sdk_111")
    assert task.task_id != 0

    label = task.create_label("test_for_sdk11")
    assert label.label_id != 0

    assert label.upload(fps=100) is True