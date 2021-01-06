#!/usr/bin/env python
"""
doc:
"""
import pytz
from pytimetools import tztools


def test_tz_utc():
    time_zone = 'UTC'
    assert tztools.get_timezone(time_zone) == pytz.UTC


def test_tz_utc8():
    time_zone = 'Asia/Shanghai'
    assert tztools.get_timezone(time_zone) != pytz.UTC
