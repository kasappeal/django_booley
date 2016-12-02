# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="django_booley",
    version="0.1.0",
    author="Alberto Casero",
    author_email="kas.appeal@gmail.com",
    include_package_data=True,
    url="http://pypi.python.org/pypi/django_booley/",
    license="LICENSE.txt",
    description="Booley integration for Django with BooleyField for models.",
    install_requires=["booley", "Django"],
)