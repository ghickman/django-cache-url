import pytest

import django_cache_url


def test_unknown_cache_backend():
    with pytest.raises(Exception):
        django_cache_url.parse('donkey://127.0.0.1/foo')
