# -*- coding: utf-8 -*-

import os
import urlparse

# Register cache schemes in URLs.
urlparse.uses_netloc.append('db')
urlparse.uses_netloc.append('dummy')
urlparse.uses_netloc.append('file')
urlparse.uses_netloc.append('locmem')
urlparse.uses_netloc.append('memcache')

DEFAULT_ENV = 'CACHE_URL'

CACHE_TYPES = {
    'db': 'django.core.cache.backends.db.DatabaseCache',
    'dummy': 'django.core.cache.backends.dummy.DummyCache',
    'file': 'django.core.cache.backends.filebased.FileBasedCache',
    'locmem': 'django.core.cache.backends.locmem.LocMemCache',
    'memcached': 'django.core.cache.backends.memcached.PyLibMCCache'
}

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

    # Update with environment configuration.
    config['BACKEND'] = CACHE_TYPES[url.scheme]
    config['LOCATION'] = url.netloc or url.path[1:]

    return config

