#!/usr/bin/env python
"""
doc:
"""


import datetime
from pytimetools import timetools


def test_get_now_local():
    assert timetools.get_now_local() == datetime.datetime.now()
