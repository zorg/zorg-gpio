from zorg_gpio.temperature_sensor import TemperatureSensor
from zorg_gpio.analog_sensor import AnalogSensor
from zorg_gpio.light_sensor import LightSensor
from .mock_device import MockDriver
from unittest import TestCase


class TestAnalogSensor(TestCase):

    def setUp(self):
        self.sensor = AnalogSensor({}, MockDriver())

    def test_read(self):
        self.assertEqual(self.sensor.read(), 500)


class TestLightSensor(TestCase):

    def setUp(self):
        self.sensor = LightSensor({}, MockDriver())

    def test_has_changed_first_read(self):
        """
        The `has_changed` method should return false
        when called for the first time because there
        is no previous reading to compare it with.
        """
        self.assertFalse(self.sensor.has_changed())

    def test_has_not_changed(self):
        self.sensor.previous_value = 500
        self.assertFalse(self.sensor.has_changed())

    def test_value_has_increased(self):
        self.sensor.previous_value = 502
        self.assertTrue(self.sensor.has_changed())

    def test_value_has_decreased(self):
        self.sensor.previous_value = 498
        self.assertTrue(self.sensor.has_changed())


class TestTemperatureSensor(TestCase):

    def setUp(self):
        self.sensor = TemperatureSensor({}, MockDriver())

    def test_read_celsius(self):
        self.assertEqual(self.sensor.read_celsius(), 25)

    def test_read_fahrenheit(self):
        self.assertEqual(self.sensor.read_fahrenheit(), 77)

    def test_read_kelvin(self):
        self.assertEqual(self.sensor.read_kelvin(), 298.15)
