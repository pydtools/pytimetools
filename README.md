# [pytimetools](https://pypi.org/project/pytimetools/#description)
python datetime tools (py开发中的时间转换工具集合)

* utc
* gmt
* local time
* timestamp


local:
* local -> utc
* local -> timestamp
* local -> gmt

utc:
* utc -> local
* utc -> timestamp
* utc -> gmt

timestamp:
* timestamp -> utc
* timestamp -> local
* timestamp -> gmt

gmt:
* gmt -> utc
* gmt -> local
* gmt -> timestamp

## use in django 
* django
* tz:settings.TIME_ZONE


```shell
➜  ~ pip install pytimetools
Collecting pytimetools
  Using cached pytimetools-0.1.2-py3-none-any.whl (3.7 kB)
Requirement already satisfied: django<3.0,>=2.2 in ./.pyenv/versions/3.9-dev/lib/python3.9/site-packages (from pytimetools) (2.2)
Requirement already satisfied: pytz in ./.pyenv/versions/3.9-dev/lib/python3.9/site-packages (from django<3.0,>=2.2->pytimetools) (2020.1)
Requirement already satisfied: sqlparse in ./.pyenv/versions/3.9-dev/lib/python3.9/site-packages (from django<3.0,>=2.2->pytimetools) (0.4.1)
Installing collected packages: pytimetools
Successfully installed pytimetools-0.1.2
➜  ~ python
Python 3.9.0a5+ (heads/master:e3ec44d, Apr 10 2020, 15:58:54)
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pytimetools import timetools
>>>
```

## 国内镜像仓库

```
https://pypi.tuna.tsinghua.edu.cn/simple/pytimetools/
```
