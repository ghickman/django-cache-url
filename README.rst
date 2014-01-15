Django-Cache-URL
~~~~~~~~~~~~~~~~
This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.

This was built with inspiration from rdegges'
`django-heroku-memcacheify <https://github.com/rdegges/django-heroku-memcacheify>`_
as a way to use CACHE_URL in apps that aren't necessarily hosted on Heroku.

The internals borrow heavily from kennethreitz's
`dj-database-url <https://github.com/kennethreitz/dj-database-url>`_.


Usage
-----
Configure your cache in ``settings.py`` from ``CACHE_URL``::

    CACHES = {'default': django_cache_url.config()}

Defaults to local memory cache if ``CACHE_URL`` isn't set.

Parse an arbitrary Cache URL::

    CACHES = {'default': django_cache_url.parse('memcache://...')}

Supported Caches
----------------
Support currently exists for:

* locmem (default): ``'locmem://[location][/location]'``
* db: ``'db://cache_table[/prefix]'``
* dummy: ``'dummy://'``
* file: ``'file:///path/to/file'``
* memcached: ``'memcached://127.0.0.1:11211[/prefix]``
* pymemcached: ``'pymemcached://127.0.0.1:11211[/prefix]'`` For use with the python-memcached library. Useful if you're using Ubuntu <= 10.04.
* djangopylibmc: ``'djangopylibmc://127.0.0.1:11211[/prefix]'`` For use with SASL based setups such as Heroku.
* redis: ``'redis://t@host:port/db[/prefix]'`` or ``'redis:///unix/path/to/socket/file.sock/db[/prefix]'`` For use with django-redis library.
* hiredis ``'hiredis://host:port/db[/prefix]'`` or ``'hiredis:///unix/path/to/socket/file.sock/db[/prefix]'`` For use with django-redis library using
  HiredisParser

Installation
------------
Installation is simple too::

    $ pip install django-cache-url

Tests
-----
I haz them!

.. image:: https://secure.travis-ci.org/ghickman/django-cache-url.png?branch=master

To run the tests install nose::

    pip install nose

Then run them with::

    make test

