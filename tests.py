from os import environ
from unittest import TestCase

from nose.tools import assert_equals
try:
    from nose.tools import assert_in
except ImportError:
    # Pre-Python 2.7
    def assert_in(val, elems): assert val in elems, "%r not found in %r" % (val, elems)

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
        environ['CACHE_URL'] = 'memcached://127.0.0.1:11211?key_prefix=site1'

    def test_memcached_url_returns_pylibmc_cache(self):
        location = 'django.core.cache.backends.memcached.PyLibMCCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_memcached_url_returns_location_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:11211')

    def test_memcached_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')

    def test_memcached_url_multiple_locations(self):
        environ['CACHE_URL'] = 'memcached://127.0.0.1:11211,192.168.0.100:11211?key_prefix=site1'
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:11211;192.168.0.100:11211')


class TestRedisCache(Base):
    def setUp(self):
        super(TestRedisCache, self).setUp()
        environ['CACHE_URL'] = 'redis://127.0.0.1:6379:0?key_prefix=site1'

    def test_redis_url_returns_redis_cache(self):
        location = 'redis_cache.cache.RedisCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_redis_url_returns_location_and_port_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:6379:0')

    def test_redis_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')


class TestHiredisCache(Base):
    def setUp(self):
        super(TestHiredisCache, self).setUp()
        environ['CACHE_URL'] = 'hiredis://127.0.0.1:6379:0?key_prefix=site1'

    def test_hiredis_url_returns_redis_cache(self):
        location = 'redis_cache.cache.RedisCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_hiredis_url_returns_location_and_port_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:6379:0')

    def test_hiredis_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')

    def test_hiredis_url_sets_hiredis_parser(self):
        config = django_cache_url.config()
        assert_equals(config['OPTIONS']['PARSER_CLASS'],
                      'redis.connection.HiredisParser')


class TestRedisCacheWithPassword(Base):
    def setUp(self):
        super(TestRedisCacheWithPassword, self).setUp()
        environ['CACHE_URL'] = 'redis://:redispass@127.0.0.1:6379:0?key_prefix=site1'

    def test_redis_url_returns_redis_cache(self):
        location = 'redis_cache.cache.RedisCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_redis_url_returns_location_and_port_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], '127.0.0.1:6379:0')

    def test_redis_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')

    def test_redis_url_returns_password(self):
        config = django_cache_url.config()
        assert_in('OPTIONS', config)
        assert_in('PASSWORD', config['OPTIONS'])
        assert_equals(config['OPTIONS']['PASSWORD'], 'redispass')


class TestRedisBothSocketCache(Base):
    def setUp(self):
        super(TestRedisBothSocketCache, self).setUp()
        environ['CACHE_URL'] = 'redis:///path/to/socket:1?key_prefix=site1'

    def test_socket_url_returns_redis_cache(self):
        location = 'redis_cache.cache.RedisCache'
        config = django_cache_url.config()
        assert_equals(config['BACKEND'], location)

    def test_socket_url_returns_location_and_port_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], 'unix:/path/to/socket:1')

    def test_socket_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')


class TestRedisDatabaseSocketCache(TestRedisBothSocketCache):
    def setUp(self):
        super(TestRedisDatabaseSocketCache, self).setUp()
        environ['CACHE_URL'] = 'redis:///path/to/socket:1'

    def test_socket_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config.get('KEY_PREFIX'), None)


class TestRedisPrefixSocketCache(TestRedisBothSocketCache):
    def setUp(self):
        super(TestRedisPrefixSocketCache, self).setUp()
        environ['CACHE_URL'] = 'redis:///path/to/socket?key_prefix=site1'

    def test_socket_url_returns_location_and_port_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['LOCATION'], 'unix:/path/to/socket:0')

    def test_socket_url_returns_prefix_from_url(self):
        config = django_cache_url.config()
        assert_equals(config['KEY_PREFIX'], 'site1')


class TestHiredisDatabaseSocketCache(TestRedisDatabaseSocketCache):
    def setUp(self):
        super(TestHiredisDatabaseSocketCache, self).setUp()
        environ['CACHE_URL'] = 'hiredis:///path/to/socket:1'

    def test_hiredis_url_sets_hiredis_parser(self):
        config = django_cache_url.config()
        assert_equals(config['OPTIONS']['PARSER_CLASS'],
                      'redis.connection.HiredisParser')


class TestHiredisPrefixSocketCache(TestRedisPrefixSocketCache):
    def setUp(self):
        super(TestHiredisPrefixSocketCache, self).setUp()
        environ['CACHE_URL'] = 'hiredis:///path/to/socket?key_prefix=site1'

    def test_hiredis_url_sets_hiredis_parser(self):
        config = django_cache_url.config()
        assert_equals(config['OPTIONS']['PARSER_CLASS'],
                      'redis.connection.HiredisParser')
