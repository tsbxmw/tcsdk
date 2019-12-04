
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


if __name__ == "__main__":
    auth = Auth("4c8093f3", "200f759b-1b83-4d")
    api = Api(auth=auth, endpoint="http://localhost:9030")
    task = api.create_task("test_for_sdk_111")
    assert task.task_id != 0

    label = task.create_label("test_for_sdk11")
    assert label.label_id != 0

    assert label.upload(fps=100) is True
```
