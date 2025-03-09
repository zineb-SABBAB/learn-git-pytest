import sys

import pytest

sys.path.append(".")
from exercise3.temperature_converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def test_celsius_to_fahrenheit() -> None:
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(25) == 77
    assert celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius() -> None:
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(77) == 25
    assert round(fahrenheit_to_celsius(98.6), 2) == 37


def test_celsius_to_kelvin() -> None:
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15
    assert celsius_to_kelvin(-273.15) == 0
    assert celsius_to_kelvin(25) == 298.15


def test_kelvin_to_celsius() -> None:
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(373.15) == 100
    assert kelvin_to_celsius(0) == -273.15
    assert kelvin_to_celsius(298.15) == 25


def test_kelvin_below_absolute_zero() -> None:
    with pytest.raises(ValueError) as excinfo:
        kelvin_to_celsius(-1)
    assert "Temperature cannot be below absolute zero" in str(excinfo.value)
