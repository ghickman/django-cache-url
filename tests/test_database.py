import os

import django_cache_url


def setup_module(module):
    os.environ['CACHE_URL'] = 'db://super_caching_table'


def teardown_module(module):
    del os.environ['CACHE_URL']


def test_db_url_returns_database_cache():
    location = 'django.core.cache.backends.db.DatabaseCache'
    config = django_cache_url.config()
    assert config['BACKEND'] == location


def test_db_url_returns_location_from_url():
    config = django_cache_url.config()
    assert config['LOCATION'] == 'super_caching_table'
