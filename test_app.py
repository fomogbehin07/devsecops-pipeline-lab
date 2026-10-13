import pytest
from app import greet

def test_greet_returns_message():
    assert greet("Engineer") == "Hello, Engineer!"

def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("")
