import os

import pytest

import django_cache_url


def test_config_defaults_to_locmem():
    if os.environ.get('CACHE_URL'):
        del os.environ['CACHE_URL']
    config = django_cache_url.config()
    assert config['BACKEND'] == 'django.core.cache.backends.locmem.LocMemCache'


def test_db_url_returns_database_cache_backend():
    url = 'db://super_caching_table'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django.core.cache.backends.db.DatabaseCache'
    assert config['LOCATION'] == 'super_caching_table'


def test_dummy_url_returns_dummy_cache():
    config = django_cache_url.parse('dummy://')
    assert config['BACKEND'] == 'django.core.cache.backends.dummy.DummyCache'


def test_file_url_returns_file_cache_backend():
    config = django_cache_url.parse('file:///herp')

    assert config['BACKEND'] == 'django.core.cache.backends.filebased.FileBasedCache'
    assert config['LOCATION'] == '/herp'


def test_locmem_url_returns_locmem_cache():
    config = django_cache_url.parse('locmem://')
    assert config['BACKEND'] == 'django.core.cache.backends.locmem.LocMemCache'


def test_query_string_params_are_converted_to_cache_arguments():
    url = 'redis:///path/to/socket?key_prefix=foo&bar=herp'
    config = django_cache_url.parse(url)

    assert config['KEY_PREFIX'] == 'foo'
    assert config['BAR'] == 'herp'


def test_query_string_params_are_converted_to_cache_options():
    url = 'db://my_cache_table?max_entries=1000&cull_frequency=2'
    config = django_cache_url.parse(url)

    assert 'OPTIONS' in config
    assert config['OPTIONS']['MAX_ENTRIES'] == 1000
    assert config['OPTIONS']['CULL_FREQUENCY'] == 2


def test_unknown_cache_backend():
    with pytest.raises(Exception):
        django_cache_url.parse('donkey://127.0.0.1/foo')
