
![](https://img.shields.io/pypi/v/tcsdk.svg) [![Build Status](https://travis-ci.com/tsbxmw/tcsdk.svg?branch=master)](https://travis-ci.com/tsbxmw/tcsdk)

# tcsdk

Tcloud SDK for Performance DataSource Program.


# Overview

The Main Program: https://github.com/tsbxmw/datasource

Using for upload data of the program.

# Example

## Auth

Using auth to complete the authorization.

```python
from tcsdk import Auth

auth = Auth("key", "secret")
```

## Init ApiService

Init ApiService with endpoint

```python
from tcsdk import Api

api = Api(auth=auth, endpoint="http://localhost:9030")
```

## Create Task By Api

Task is create by api object, you should offer the `task_name`, otherwise system would offer the "".

```python

task = api.create_task("test")
```

If you offer the `label_name` after the `task_name` in `create_task`, you would get an default `label` with name `label_name` which in `task.labels`. 

## Create Label By Task

Label is the sub process of task, you can also create a label by `label_name`.

```python
label = task.create_label("test")
```

Notice: `task_name` has no relationship with `label_name` .


## Now, you can upload the label data!

```python
label.upload(fps=100)
```

## Full example

```python
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

```
