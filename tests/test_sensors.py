from zorg_gpio.temperature_sensor import TemperatureSensor
from zorg_gpio.analog_sensor import AnalogSensor
from zorg_gpio.digital_sensor import DigitalSensor
from zorg_gpio.light_sensor import LightSensor
from zorg_gpio.rotary_angle_sensor import RotaryAngleSensor
from zorg_gpio.button import Button
from .mock_device import MockAdaptor
from unittest import TestCase


class TestAnalogSensor(TestCase):

    def setUp(self):
        self.sensor = AnalogSensor({}, MockAdaptor())

    def test_read(self):
        self.assertEqual(self.sensor.read(), 500)


class TestDigitalSensor(TestCase):

    def setUp(self):
        self.sensor = DigitalSensor({}, MockAdaptor())

    def test_read(self):
        self.assertEqual(self.sensor.read(), 1)


class TestLightSensor(TestCase):

    def setUp(self):
        self.sensor = LightSensor({}, MockAdaptor())

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


class TestRotaryAngleSensor(TestCase):

    def setUp(self):
        self.sensor = RotaryAngleSensor({}, MockAdaptor())

    def test_read_angle(self):
        # Test reading should approximate to 146.627565982404
        angle = self.sensor.read_angle()
        self.assertTrue(angle > 145)
        self.assertTrue(angle < 147)

class TestButton(TestCase):

    def setUp(self):
        self.button = Button({}, MockAdaptor())

    def test_button_pressed(self):
        self.assertTrue(self.button.is_pressed())

    def test_button_not_pressed(self):
        self.button.connection.digital_read.return_value = 0.0
        self.assertFalse(self.button.is_pressed())

    def test_button_bumped_open(self):
        self.button.previous_state = 0.0
        self.assertTrue(self.button.is_bumped())

    def test_button_bumped_close(self):
        self.button.previous_state = 1.0
        self.button.connection.digital_read.return_value = 0.0
        self.assertTrue(self.button.is_bumped())

    def test_button_not_bumped_open(self):
        self.button.previous_state = 1.0
        self.assertFalse(self.button.is_bumped())

    def test_button_not_bumped_close(self):
        self.button.previous_state = 0.0
        self.button.connection.digital_read.return_value = 0.0
        self.assertFalse(self.button.is_bumped())


class TestTemperatureSensor(TestCase):

    def setUp(self):
        self.sensor = TemperatureSensor({}, MockAdaptor())

    def test_read_celsius(self):
        self.assertEqual(self.sensor.read_celsius(), 25)

    def test_read_fahrenheit(self):
        self.assertEqual(self.sensor.read_fahrenheit(), 77)

    def test_read_kelvin(self):
        self.assertEqual(self.sensor.read_kelvin(), 298.15)

