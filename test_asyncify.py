import pytest
from asyncify import asyncify

def test_asyncify():
    @asyncify
    def sync_function(x):
        return x + 1

    assert sync_function(1) == 2