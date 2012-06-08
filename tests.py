from os import environ
from unittest import TestCase

from nose.tools import assert_equals

import django_cache_url


class Base(TestCase):
    def setUp(self):
        try:
            del environ['CACHE_URL']  # make sure
        except KeyError:
            pass


class TestConfigOptions(Base):
    location = 'django.core.cache.backends.memcached.PyLibMCCache'

    def test_setting_default_var(self):
        config = django_cache_url.config(default='memcached://127.0.0.1:11211')
        assert_equals(config['BACKEND'], self.location)
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

    def test_setting_env_var_name(self):
        environ['HERP'] = 'memcached://127.0.0.1:11211'
        config = django_cache_url.config(env='HERP')
        assert_equals(config['BACKEND'], self.location)
        assert_equals(config['LOCATION'], '127.0.0.1:11211')


class TestDatabaseCache(Base):
    def setUp(self):
        super(TestDatabaseCache, self).setUp()
        environ['CACHE_URL'] = 'db://super_caching_table'

    def test_db_url_returns_database_cache(self):
        location = 'django.core.cache.backends.db.DatabaseCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_db_url_returns_location_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], 'super_caching_table')


class TestDummyCache(Base):
    def test_dummy_url_returns_dummy_cache(self):
        environ['CACHE_URL'] = 'dummy://'
        location = 'django.core.cache.backends.dummy.DummyCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)


class TestFileCache(Base):
    def setUp(self):
        super(TestFileCache, self).setUp()
        environ['CACHE_URL'] = 'file:///herp'

    def test_file_url_returns_file_cache_backend(self):
        location = 'django.core.cache.backends.filebased.FileBasedCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_file_url_returns_location_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '/herp')


class TestLocMemCache(Base):
    location = 'django.core.cache.backends.locmem.LocMemCache'

    def test_config_defaults_to_locmem(self):
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], self.location)

    def test_locmem_url_returns_locmem_cache(self):
        environ['CACHE_URl'] = 'locmem://'
        config = django_cache_url.config('')
        assert_equals(config['BACKEND'], self.location)


class TestMemcachedCache(Base):
    def setUp(self):
        super(TestMemcachedCache, self).setUp()
        environ['CACHE_URL'] = 'memcached://127.0.0.1:11211/prefix'

    def test_memcached_url_returns_pylibmc_cache(self):
        location = 'django.core.cache.backends.memcached.PyLibMCCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_memcached_url_returns_location_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

    def test_memcached_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['PREFIX'], 'prefix')


