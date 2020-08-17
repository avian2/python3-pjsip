# Python 3 bindings for pjsip

Building a wheel on Debian:

    $ apt-get install python3-pkgconfig
    $ apt-get install libpjproject-dev
    $ python3 setup.py bdist_wheel

## Debian packaging

To make a new release:

    $ git checkout master
    $ python3 setup.py sdist
    $ git checkout debian
    $ gbp import-orig --upstream-vcs-tag=v1!1.0.3 --debian-branch debian dist/pjsua-1\!1.0.3.tar.gz

Edit d/changelog, etc.
