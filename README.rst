Django-Cache-URL
~~~~~~~~~~~~~~

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.


Usage
-----

Configure your cache in ``settings.py`` from ``CACHE_URL``::

    CACHES = {'default': django_cache_url.config()}

Defaults to local memory if ``CACHE_URL`` isn't set.

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

