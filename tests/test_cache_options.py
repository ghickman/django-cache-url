import os

import django_cache_url


def teardown_module(module):
    del os.environ['CACHE_URL']


def test_query_string_params_are_converted_to_cache_options():
    os.environ['CACHE_URL'] = 'redis:///path/to/socket?key_prefix=foo&bar=herp'
    config = django_cache_url.config()

    assert config['KEY_PREFIX'] == 'foo'
    assert config['BAR'] == 'herp'
