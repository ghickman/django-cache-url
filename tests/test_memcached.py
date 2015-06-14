import django_cache_url


def test_memcached_url_returns_pylibmc_cache():
    url = 'memcached://127.0.0.1:11211?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django.core.cache.backends.memcached.PyLibMCCache'
    assert config['LOCATION'] == '127.0.0.1:11211'
    assert config['KEY_PREFIX'] == 'site1'


def test_memcached_url_multiple_locations():
    url = 'memcached://127.0.0.1:11211,192.168.0.100:11211?key_prefix=site1'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == '127.0.0.1:11211;192.168.0.100:11211'


def test_memcached_socket_url():
    url = 'memcached:///path/to/socket/'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == 'unix:/path/to/socket/'
