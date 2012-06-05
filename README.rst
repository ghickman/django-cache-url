Django-Cache-URL
~~~~~~~~~~~~~~

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

Supported caches
-------------------

Support currently exists for database, dummy, file, local memory and memcached
caches.


Installation
------------

Installation is simple too::

    $ pip install django-cache-url

Tests
-----
I has them!
[![Build Status](https://secure.travis-ci.org/ghickman/django-cache-url.png?branch=master)](http://travis-ci.org/ghickman/django-cache-url)
