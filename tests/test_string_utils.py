import sys

import pytest

sys.path.append(".")
from exercise2.string_utils import (
    capitalize_words,
    count_vowels,
    is_palindrome,
    reverse_string,
)


def test_reverse_string() -> None:
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"


def test_count_vowels() -> None:
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5
    assert count_vowels("aEiOu") == 5
    assert count_vowels("") == 0
    assert count_vowels("bcdfg") == 0


def test_is_palindrome() -> None:
    assert is_palindrome("radar") == True
    assert is_palindrome("Radar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Race car") == True
    assert is_palindrome("race a car") == False


def test_capitalize_words() -> None:
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("") == ""
    assert capitalize_words("a") == "A"
    assert capitalize_words("already Capitalized") == "Already Capitalized"
    assert capitalize_words("multiple   spaces") == "Multiple   Spaces"
