# [pytimetools](https://pypi.org/project/pytimetools/#description)
python datetime tools (py开发中的时间转换工具集合)


## todo
* UTC:世界标准时间
* GMT:格林威治时间
* CST:北京时间
* PST:太平洋时间
* timestamp:时间戳
* localtime(UTC+8). 后期通过pytz改为通用当地时间

```
GMT: UTC +0    =    GMT: GMT +0
CST: UTC +8    =    CST: GMT +8
PST: UTC -8    =    PST: GMT -8
```

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
>>> timetools.get_now_local()
datetime.datetime(2021, 1, 6, 15, 48, 17, 922079)
>>>
```

