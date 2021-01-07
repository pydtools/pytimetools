from pytimetools import __version__
from pytimetools import utctools
from pytimetools import localtools


def test_version():
    assert __version__ == '0.1.3.7'


def test_utc_to_gmt():
    utc_now = utctools.get_now()
    gmt_now = utctools.utc_to_gmt(utc_now)
    assert gmt_now != ""


def test_now_to_gmt():
    utc_now = utctools.get_now()
    local_now = utctools.utc_to_localtime(utc_now)
    utc_gmt_now = utctools.utc_to_gmt(utc_now)
    local_gmt_now = localtools.localtime_to_gmt(local_now)
    assert utc_gmt_now == local_gmt_now
