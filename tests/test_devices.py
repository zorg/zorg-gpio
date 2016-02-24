from zorg_gpio.led import Led
from zorg_gpio.relay import Relay
from zorg_gpio.buzzer import Buzzer
from .mock_device import MockAdaptor
from unittest import TestCase


class TestLED(TestCase):

    def setUp(self):
        self.led = Led({}, MockAdaptor())

    def test_set_state_on(self):
        self.led.set_state(1)
        self.assertEqual(self.led.is_on(), True)

    def test_set_state_off(self):
        self.led.set_state(0)
        self.assertEqual(self.led.is_on(), False)

    def test_turn_on(self):
        self.led.turn_on()
        self.assertEqual(self.led.is_on(), True)

    def test_turn_off(self):
        self.led.turn_off()
        self.assertEqual(self.led.is_on(), False)

    def test_toggle(self):
        self.led.toggle()
        first_toggle = self.led.is_on()

        self.led.toggle()
        second_toggle = self.led.is_on()

        self.assertTrue(first_toggle != second_toggle)


class TestRelay(TestCase):

    def setUp(self):
        self.relay = Relay({}, MockAdaptor())

    def test_set_state_on(self):
        self.relay.set_state(1)
        self.assertEqual(self.relay.is_on(), True)

    def test_set_state_off(self):
        self.relay.set_state(0)
        self.assertEqual(self.relay.is_on(), False)

    def test_turn_on(self):
        self.relay.turn_on()
        self.assertEqual(self.relay.is_on(), True)

    def test_turn_off(self):
        self.relay.turn_off()
        self.assertEqual(self.relay.is_on(), False)

    def test_toggle(self):
        self.relay.toggle()
        first_toggle = self.relay.is_on()

        self.relay.toggle()
        second_toggle = self.relay.is_on()

        self.assertTrue(first_toggle != second_toggle)


class TestBuzzer(TestCase):

    def setUp(self):
        self.buzzer = Buzzer({}, MockAdaptor())

    def test_set_state_on(self):
        self.buzzer.set_state(1)
        self.assertEqual(self.buzzer.is_on(), True)

    def test_set_state_off(self):
        self.buzzer.set_state(0)
        self.assertEqual(self.buzzer.is_on(), False)

    def test_turn_on(self):
        self.buzzer.turn_on()
        self.assertEqual(self.buzzer.is_on(), True)

    def test_turn_off(self):
        self.buzzer.turn_off()
        self.assertEqual(self.buzzer.is_on(), False)

    def test_toggle(self):
        self.buzzer.toggle()
        first_toggle = self.buzzer.is_on()

        self.buzzer.toggle()
        second_toggle = self.buzzer.is_on()

        self.assertTrue(first_toggle != second_toggle)
