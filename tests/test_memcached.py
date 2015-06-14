import os

import django_cache_url


def setup_module(module):
    os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211?key_prefix=site1'


def teardown_module(module):
    del os.environ['CACHE_URL']


def test_memcached_url_returns_pylibmc_cache():
    location = 'django.core.cache.backends.memcached.PyLibMCCache'
    config = django_cache_url.config()
    assert config['BACKEND'] == location


def test_memcached_url_returns_location_from_url():
    config = django_cache_url.config()
    assert config['LOCATION'] == '127.0.0.1:11211'


def test_memcached_url_returns_prefix_from_url():
    config = django_cache_url.config()
    assert config['KEY_PREFIX'] == 'site1'


def test_memcached_url_multiple_locations():
    os.environ['CACHE_URL'] = 'memcached://127.0.0.1:11211,192.168.0.100:11211?key_prefix=site1'
    config = django_cache_url.config()
    assert config['LOCATION'] == '127.0.0.1:11211;192.168.0.100:11211'


def test_memcached_socket_url():
    url = 'memcached:///path/to/socket/'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == 'unix:/path/to/socket/'
