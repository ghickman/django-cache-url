from os import environ
from unittest import TestCase

from nose.tools import assert_equals

import django_cache_url


DB = 'django.core.cache.backends.db.DatabaseCache'
DUMMY = 'django.core.cache.backends.dummy.DummyCache'
FILE = 'django.core.cache.backends.filebased.FileBasedCache'
LOCMEM = 'django.core.cache.backends.locmem.LocMemCache'
MEMCACHED = 'django.core.cache.backends.memcached.PyLibMCCache'

class TestDjangoCacheUrl(TestCase):
    def test_config_defaults_to_locmem(self):
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], LOCMEM)

    def test_db_url_returns_database_cache(self):
        environ['CACHE_URL'] = 'db:///super_caching_table'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], DB)
        assert_equals(config['LOCATION'], 'super_caching_table')

    def test_dummy_url_returns_dummy_cache(self):
        environ['CACHE_URL'] = 'dummy://'
        config = django_cache_url.config()
        print config
        assert_equals(config['BACKEND'], DUMMY)
        assert_equals(config['LOCATION'], '')

    def test_file_url_returns_file_cache(self):
        environ['CACHE_URL'] = 'file:///herp'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], FILE)
        assert_equals(config['LOCATION'], 'herp')

    def test_memcached_url_returns_pylibmc_cache(self):
        environ['CACHE_URL'] = 'memcached://127.0.0.1:11211'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], MEMCACHED)
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

    def test_setting_default_var(self):
        config = django_cache_url.config(default='memcache://127.0.0.1:11211')
        assert_equals(config['BACKEND'], MEMCACHED)
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

    def test_setting_env_var_name(self):
        environ['HERP'] = 'memcached://127.0.0.1:11211'
        config = django_cache_url.config(env='HERP')
        assert_equals(config['BACKEND'], MEMCACHED)
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

