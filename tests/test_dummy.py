import os

import django_cache_url


def test_dummy_url_returns_dummy_cache():
    os.environ['CACHE_URL'] = 'dummy://'
    location = 'django.core.cache.backends.dummy.DummyCache'
    config = django_cache_url.config()
    assert config['BACKEND'] == location
