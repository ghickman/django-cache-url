import os

import pytest

import django_cache_url


def test_uwsgicache_url_returns_uwsgicache_cache():
    url = 'uwsgicache://cachename/'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'uwsgicache.UWSGICache'
    assert config['LOCATION'] == 'cachename'


def test_uwsgicache_default_location():
    url = 'uwsgicache://'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == 'default'
