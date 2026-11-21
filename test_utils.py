import pytest
from asyncify.utils import helper_function

def test_helper_function():
    assert helper_function() is None