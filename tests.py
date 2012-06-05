from os import environ
from unittest import TestCase

from nose.tools import assert_true

import django_cache_url


DB = 'django.core.cache.backends.db.DatabaseCache'
DUMMY = 'django.core.cache.backends.dummy.DummyCache'
FILE = 'django.core.cache.backends.filebased.FileBasedCache'
LOCMEM = 'django.core.cache.backends.locmem.LocMemCache'
MEMCACHED = 'django.core.cache.backends.memcached.PyLibMCCache'

class TestDjangoCacheUrl(TestCase):
    def test_config_defaults_to_locmem(self):
        config = django_cache_url.config()
        assert_true(config['ENGINE'], LOCMEM)

    def test_db_url_returns_database_cache(self):
        environ['CACHE_URL'] = 'db:///super_caching_table'
        config = django_cache_url.config()
        assert_true(config['ENGINE'], DB)
        assert_true(config['LOCATION'], 'super_caching_table')

    def test_file_url_returns_file_cache(self):
        environ['CACHE_URL'] = 'file:///herp'
        config = django_cache_url.config()
        assert_true(config['ENGINE'], FILE)
        assert_true(config['LOCATION'], 'herp')

