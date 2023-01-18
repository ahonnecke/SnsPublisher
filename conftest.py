#!/usr/bin/env python3

import pytest


@pytest.fixture()
def message():
    return {"foo": "bar"}
