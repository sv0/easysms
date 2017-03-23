Python client for EasySMS
###########################

.. _description:


**EasySMS** is a python wrapper for Easy SMS API. Currently Easy SMS API available as a `Heroku Easy SMS add-on`_.
Documentation available on the github_.


.. _badges:

.. image:: https://travis-ci.org/sv0/easysms.svg?branch=master
    :target: https://travis-ci.org/sv0/easysms
    :alt: Build Status    

.. image:: https://coveralls.io/repos/github/sv0/easysms/badge.svg?branch=master
    :target: https://coveralls.io/github/sv0/easysms?branch=master
    :alt: Coverals

.. image:: https://img.shields.io/badge/license-GPL3-blue.svg
    :target: https://pypi.python.org/pypi/easysms
    :alt: License


.. contents::

.. _requirements:

Requirements
============

- python >= 3.4


.. _installation:

Installation
============

**EasySMS** client can be installed using pip: ::

    pip install easysms


Usage 
=====

API **URL** can be found on the `Easy SMS Dashboard`_ 


.. image:: https://i.imgur.com/JfIgDQG.png
    :alt: Easy SMS Dashboard


::

    from easysms.client import EasySMSClient

    URL = 'https://6db56db56db5:32dc32dc32dc@api.easysmsapp.co'

    client = EasySMSClient(URL)
    sms = client.send(
        '+420735123456',                # recepient phone number
        '+38097100500',                 # sender phone number
        'Hey man! How are you doing?'   # message text
    )

::


Changes
=======

Make sure you`ve read the following document if you are upgrading from previous versions:

http://packages.python.org/easysms/changes.html


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/sv0/easysms/issues


Contributing
============

Development of easysms happens at github: https://github.com/sv0/easysms


Contributors
============

* None (None)


License
=======

Licensed under a `GNU  general public license v3`_.


Copyright
=========

Copyright (c) 2017 `Slavik Svyrydiuk`_


.. _GNU general public license v3: http://www.gnu.org/licenses/gpl.txt

.. _pypi: http://packages.python.org/easysms/
.. _github: https://github.com/sv0/easysms
.. _Heroku Easy SMS add-on: https://elements.heroku.com/addons/easysms
.. _Easy SMS Dashboard: https://www.easysmsapp.com/dashboard
.. _Slavik Svyrydiuk: http://slavik.svyrydiuk.eu/?_=EasySMS
