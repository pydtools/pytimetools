#!/usr/bin/env python
"""
doc:
GMT -> UTC
GMT -> local
GMT -> timestamp
"""


def datetime_to_gmt(date_time_utc=None):
    """
    a = datetime.datetime.strptime(timestamp, GMT_FORMAT) +
            datetime.timedelta(hours=8)
    时间不对。
        时间格式不对。正确的时间格式：Tue, 05 May 2015 06:11:34 GMT
        时间为US时间,不是中国时间
        合作方放在HttpRequest中的时间和我们的在HttpRequest中获取到得时间不同
    :param date_time_utc:
    :return:
    """
    gmt_fmt = '%a, %d %b %Y %H:%M:%S GMT'
    return date_time_utc.strftime(gmt_fmt)
