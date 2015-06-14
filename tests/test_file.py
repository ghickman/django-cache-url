import os

import django_cache_url


def setup_module(module):
    os.environ['CACHE_URL'] = 'file:///herp'


def teardown_module(module):
    del os.environ['CACHE_URL']


def test_file_url_returns_file_cache_backend():
    location = 'django.core.cache.backends.filebased.FileBasedCache'
    config = django_cache_url.config()
    assert config['BACKEND'] == location


def test_file_url_returns_location_from_url():
    config = django_cache_url.config()
    assert config['LOCATION'] == '/herp'
