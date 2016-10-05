import sys


if 'install' not in sys.argv and 'egg_info' not in sys.argv:
    from .analog_sensor import AnalogSensor
    from .button import Button
    from .buzzer import Buzzer
    from .digital_sensor import DigitalSensor
    from .led import Led
    from .light_sensor import LightSensor
    from .relay import Relay


__all__ = [
    'AnalogSensor',
    'Button',
    'Buzzer',
    'DigitalSensor',
    'Led',
    'LightSensor',
    'Relay',
]

__version__ = '0.0.3'
