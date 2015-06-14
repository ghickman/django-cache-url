import os
import django_cache_url


LOCATION = 'django.core.cache.backends.locmem.LocMemCache'


def test_config_defaults_to_locmem():
    if os.environ.get('CACHE_URL'):
        del os.environ['CACHE_URL']
    config = django_cache_url.config()
    assert config['BACKEND'] == LOCATION


def test_locmem_url_returns_locmem_cache():
    config = django_cache_url.parse('locmem://')
    assert config['BACKEND'] == LOCATION
