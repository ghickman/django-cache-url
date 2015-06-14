import django_cache_url


def test_query_string_params_are_converted_to_cache_options():
    url = 'redis:///path/to/socket?key_prefix=foo&bar=herp'
    config = django_cache_url.parse(url)

    assert config['KEY_PREFIX'] == 'foo'
    assert config['BAR'] == 'herp'
