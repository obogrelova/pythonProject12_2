import pytest
from main import count_vowels

@pytest.mark.parametrize("test_input, expected", [
    ("aeiouyAEIOUY", 12),
    ("bcdfg", 0),
    ("Hello World!", 3),
    ("Python is fun!", 4),
    ("", 0)
])

def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected