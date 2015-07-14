from unittest import TestCase
from zorg_gpio import AnalogSensor
from zorg_gpio import TemperatureSensor
from zorg_gpio import Servo
from zorg_gpio import Led


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
        all_commands_have_methods = True

        for command in sensor.commands:
            if command not in dir(sensor):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)


class LEDSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        led = Led(self.options, self.connection)
        all_commands_have_methods = True

        for command in led.commands:
            if command not in dir(led):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)


class ServoSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        servo = Servo(self.options, self.connection)
        all_commands_have_methods = True

        for command in servo.commands:
            if command not in dir(servo):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)


class TemperatureSmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        sensor = TemperatureSensor(self.options, self.connection)
        all_commands_have_methods = True

        for command in sensor.commands:
            if command not in dir(sensor):
                all_commands_have_methods = False

        self.assertTrue(all_commands_have_methods)

