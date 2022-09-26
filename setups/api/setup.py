#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from setuptools import setup

setup(
    name="decentra_network_api",
    version="0.33.0",
    description="""This is API mode installer for Decentra Network""",
    url="https://docs.decentranetwork.org/",
    author="Decentra Network Developers",
    author_email="onur@decentranetwork.org",
    license="MPL-2.0",
    install_requires="""
flask==2.0.0
waitress==2.1.2
werkzeug==2.0.3
""",
    python_requires=">=3.8",
    zip_safe=False,
)
