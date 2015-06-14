import django_cache_url


def test_db_url_returns_database_cache():
    url = 'db://super_caching_table'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django.core.cache.backends.db.DatabaseCache'
    assert config['LOCATION'] == 'super_caching_table'
