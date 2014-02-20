# -*- coding: utf-8 -*-
"""
django-cache-url
~~~~~~~~~~~~~~~~

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.


Usage
-----

Configure your cache in ``settings.py``::

    CACHES={'default': django_cache_url.config()}

Nice and simple.
"""
from setuptools import setup


setup(
    name='django-cache-url',
    version='0.8.0',
    url='http://github.com/ghickman/django-cache-url',
    license='MIT',
    author='George Hickman',
    author_email='george@ghickman.co.uk',
    description='Use Cache URLs in your Django application.',
    long_description=__doc__,
    py_modules=('django_cache_url',),
)
