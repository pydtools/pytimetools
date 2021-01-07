from pytimetools import __version__
from pytimetools import utctools


def test_version():
    assert __version__ == '0.1.3.4'

# 测试时间转换


def test_utc_to_gmt():
    utc_now = utctools.get_now()
    gmt_now = utctools.utc_to_gmt(utc_now)
    assert gmt_now != ""
