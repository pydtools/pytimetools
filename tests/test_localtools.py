#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc:
"""

from pytimetools import localtools


def test_local_get_now():
    assert localtools.get_now()
