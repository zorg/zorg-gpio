from zorg_gpio.temperature_sensor import TemperatureSensor
from zorg_gpio.analog_sensor import AnalogSensor
from .mock_device import MockDriver
from unittest import TestCase


class TestAnalogSensor(TestCase):

    def setUp(self):
        self.sensor = AnalogSensor({}, MockDriver())

    def test_read(self):
        self.assertEqual(self.sensor.read(), 500)


class TestTemperatureSensor(TestCase):

    def setUp(self):
        self.sensor = TemperatureSensor({}, MockDriver())

    def test_read_celsius(self):
        self.assertEqual(self.sensor.read_celsius(), 25)

    def test_read_fahrenheit(self):
        self.assertEqual(self.sensor.read_fahrenheit(), 77)

    def test_read_kelvin(self):
        self.assertEqual(self.sensor.read_kelvin(), 298.15)
