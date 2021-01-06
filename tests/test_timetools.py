#!/usr/bin/env python
"""
doc:
"""

from pytimetools import localtools


def test_local_get_now():
    assert localtools.get_now()
