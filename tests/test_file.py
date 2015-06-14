import django_cache_url


def test_file_url_returns_file_cache_backend():
    config = django_cache_url.parse('file:///herp')

    assert config['BACKEND'] == 'django.core.cache.backends.filebased.FileBasedCache'
    assert config['LOCATION'] == '/herp'
