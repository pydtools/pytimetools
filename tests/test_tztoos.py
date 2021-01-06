#!/usr/bin/env python
"""
doc:
"""
import pytz
from pytimetools import tztools


def test_tz_utc():
    time_zone = tztools.DEFAULT_TZ_UTC
    assert tztools.get_timezone(time_zone) == pytz.UTC


def test_tz_utc8():
    time_zone = tztools.DEFAULT_TZ_SH
    assert tztools.get_timezone(time_zone) != pytz.UTC
