#!/usr/bin/env python
"""
doc:
local:
local -> utc
local -> timestamp
local -> gmt

utc:
utc -> local
utc -> timestamp
utc -> gmt

timestamp:
timestamp -> utc
timestamp -> local
timestamp -> gmt

gmt:
gmt -> utc
gmt -> local
gmt -> timestamp
"""

import datetime
import time
import pytz

from pytimetools.tztools import get_current_timezone


def utc_to_localtime(utctime):
    """
    naive time 与 active time的概念
    1.数据库中的DateTimeFiled需要转换localtime
    2.前端传入的时间最好时utctime

    astimezone:
        可以将一个时区的时间转换成另一个时区的时间,
        前提是这个被转换的时间必须是一个aware时间
    https://www.cnblogs.com/limaomao/p/9257014.html
    :param utctime:
    :return:
    """
    # naive time(不知道自己时区) => aware time(有时区)
    utc = utctime.replace(tzinfo=pytz.UTC)
    local_time = utc.astimezone(get_current_timezone())
    return local_time


def localtime_to_timestamp(local_time):
    """

    :param local_time:
    :return:
    """
    return time.mktime(local_time.timetuple())


def localtime_to_timestamp_ms(local_time):
    """

    :param local_time:
    :return:
    """
    return int(localtime_to_timestamp(local_time))*1000


def localtime_to_utc(local_time):
    """
    localtime -> utc
    1.本地时区转为时间戳
    2.时间戳转为utc

    上海1927改表, 故不使用replace
    :param local_time:
    :return:
    """
    timestamp = localtime_to_timestamp(local_time)
    return timestamp_to_utc(timestamp)


def timestamp_to_utc(timestamp):
    """
    时间戳转utc
    :param timestamp:
    :return:
    """
    utc_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)
    return utc_time


