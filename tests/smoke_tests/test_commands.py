from unittest import TestCase
from zorg_gpio import AnalogSensor
from zorg_gpio import DigitalSensor
from zorg_gpio import LightSensor
from zorg_gpio import TemperatureSensor
from zorg_gpio import Button
from zorg_gpio import Buzzer
from zorg_gpio import Servo
from zorg_gpio import Relay
from zorg_gpio import RotaryAngleSensor
from zorg_gpio import Led
from zorg_gpio import TouchSensor


class SmokeTestCase(TestCase):

    def setUp(self):
        self.connection = None
        self.options = {}


class AnalogSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        sensor = AnalogSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class ButtonSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        button = Button(self.options, self.connection)

        for command in button.commands:
            self.assertIn(command, dir(button))


class BuzzerSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        buzzer = Buzzer(self.options, self.connection)

        for command in buzzer.commands:
            self.assertIn(command, dir(buzzer))


class DigitalSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        sensor = DigitalSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class LEDSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        led = Led(self.options, self.connection)

        for command in led.commands:
            self.assertIn(command, dir(led))


class LightSensorTests(SmokeTestCase):

    def test_command_method_exists(self):
        sensor = LightSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class RelaySmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        relay = Relay(self.options, self.connection)

        for command in relay.commands:
            self.assertIn(command, dir(relay))


class RotaryAngleSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        sensor = RotaryAngleSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class ServoSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        servo = Servo(self.options, self.connection)

        for command in servo.commands:
            self.assertIn(command, dir(servo))


class TemperatureSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        sensor = TemperatureSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))


class TouchSensorSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        sensor = TouchSensor(self.options, self.connection)

        for command in sensor.commands:
            self.assertIn(command, dir(sensor))
