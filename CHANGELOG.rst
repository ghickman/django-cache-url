CHANGELOG
=========

v1.1.0
------

- Add support for uwsgi caching (thanks to Alan Justino da Silva)


v1.0.0
------

- **Backwards Incompatible** Improve Redis URL parsing, making PREFIX parsing much easier and automatically converting query args into Django Cache settings (thanks to Russell Davies)
- **Backwards Incompatible** Switch to ``django-redis``'s new import name (thanks to Michael Warkentin)
- Switch to Tox for running tests with different pythons
- Switch to pytest


v0.8.0
------

- Add support for password in redis urls (thanks to Mjumbe Wawatu Ukweli)


v0.7.0
------

- Add support for UNIX sockets in redis urls (thanks to Jannis Leidel)


v0.6.0
------

- Fix Python 3 support


v0.5.0
------

- Add multiple memcache locations


v0.4.0
------

- Add redis and hiredis support


v0.3.4
------

- Fix Python 3 compatibility import bug


v0.3.3
------

- Add Python 3 compatibility


v0.3.2
------

- Fix setting name bug


v0.3.1
------

- Remove underscore from django pylibmc scheme


v0.3.0
------

- Add python memcached support
- Add django pylibmc support


v0.2.0
------

- Add prefix support
- Split up tests
- Tidy up examples


v0.1.0
------

- Initial release
