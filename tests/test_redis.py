import django_cache_url


#
# HIREDIS
#

def test_hiredis():
    url = 'hiredis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_redis.cache.RedisCache'
    assert config['LOCATION'] == '127.0.0.1:6379:0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_socket():
    url = 'hiredis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_redis.cache.RedisCache'
    assert config['LOCATION'] == 'unix:/path/to/socket:1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


#
# REDIS
#

def test_redis():
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_redis.cache.RedisCache'
    assert config['LOCATION'] == '127.0.0.1:6379:0'


def test_redis_socket():
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_redis.cache.RedisCache'
    assert config['LOCATION'] == 'unix:/path/to/socket:1'
    assert 'OPTIONS' not in config


def test_redis_with_password():
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_redis.cache.RedisCache'
    assert config['LOCATION'] == '127.0.0.1:6379:0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'
