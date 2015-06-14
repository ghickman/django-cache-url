import django_cache_url


def test_dummy_url_returns_dummy_cache():
    config = django_cache_url.parse('dummy://')
    assert config['BACKEND'] == 'django.core.cache.backends.dummy.DummyCache'
