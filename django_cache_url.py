# -*- coding: utf-8 -*-

import os
import re

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register cache schemes in URLs.
urlparse.uses_netloc.append('db')
urlparse.uses_netloc.append('dummy')
urlparse.uses_netloc.append('file')
urlparse.uses_netloc.append('locmem')
urlparse.uses_netloc.append('memcached')
urlparse.uses_netloc.append('djangopylibmc')
urlparse.uses_netloc.append('pymemcached')
urlparse.uses_netloc.append('redis')
urlparse.uses_netloc.append('hiredis')

DEFAULT_ENV = 'CACHE_URL'

BACKENDS = {
    'db': 'django.core.cache.backends.db.DatabaseCache',
    'dummy': 'django.core.cache.backends.dummy.DummyCache',
    'file': 'django.core.cache.backends.filebased.FileBasedCache',
    'locmem': 'django.core.cache.backends.locmem.LocMemCache',
    'memcached': 'django.core.cache.backends.memcached.PyLibMCCache',
    'djangopylibmc': 'django_pylibmc.memcached.PyLibMCCache',
    'pymemcached': 'django.core.cache.backends.memcached.MemcachedCache',
    'redis': 'redis_cache.cache.RedisCache',
    'hiredis': 'redis_cache.cache.RedisCache',
}

redis_path_pattern = re.compile(r'[\w./-]+:?(?P<redis_db>\d)?')
redis_url_pattern = re.compile(r'.:(?P<port>\d+):?(?P<redis_db>\d)?')


def config(env=DEFAULT_ENV, default='locmem://'):
    """Returns configured CACHES dictionary from CACHE_URL"""
    config = {}

    s = os.environ.get(env, default)

    if s:
        config = parse(s)

    return config


def parse(url):
    """Parses a cache URL."""
    config = {}

    url = urlparse.urlparse(url)
    # Handle python 2.6 broken url parsing
    path, query = url.path, url.query
    if '?' in path and query == '':
        path, query = path.split('?', 1)

    cache_args = dict([(key.upper(), ';'.join(val)) for key, val in
                        urlparse.parse_qs(query).items()])

    # Update with environment configuration.
    config['BACKEND'] = BACKENDS[url.scheme]

    redis_options = {}
    if url.scheme == 'hiredis':
        redis_options['PARSER_CLASS'] = 'redis.connection.HiredisParser'

    # File based
    if not url.netloc:
        if url.scheme in ('memcached', 'pymemcached', 'djangopylibmc'):
            config['LOCATION'] = 'unix:' + path
        elif url.scheme in ('redis', 'hiredis'):
            redis_db = redis_path_pattern.match(path).group('redis_db')
            if redis_db:
                config['LOCATION'] = 'unix:%s' % (path,)
            else:
                config['LOCATION'] = 'unix:%s:%s' % (path, '0')
        else:
            config['LOCATION'] = path
    # URL based
    else:
        # Handle multiple hosts
        config['LOCATION'] = ';'.join(url.netloc.split(','))

        if url.scheme in ('redis', 'hiredis'):
            if url.password:
                redis_options['PASSWORD'] = url.password
            # url.port handling differs between python 2 and 3 so use regex
            port = redis_url_pattern.search(url.netloc).group('port')
            redis_db = redis_url_pattern.search(url.netloc).group('redis_db') or '0'
            config['LOCATION'] = "%s:%s:%s" % (url.hostname, port, redis_db)

    if redis_options:
        config['OPTIONS'] = redis_options

    config.update(cache_args)

    return config
