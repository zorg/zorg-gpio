# zorg-gpio

[![Package Version](https://img.shields.io/pypi/v/zorg-gpio.svg)](https://pypi.python.org/pypi/zorg-gpio/)
[![Requirements Status](https://requires.io/github/zorg/zorg-gpio/requirements.svg?branch=master)](https://requires.io/github/zorg/zorg-gpio/requirements/?branch=master)
[![Build Status](https://travis-ci.org/zorg/zorg-gpio.svg?branch=master)](https://travis-ci.org/zorg/zorg-gpio)
[![Code Climate](https://codeclimate.com/github/zorg/zorg-gpio/badges/gpa.svg)](https://codeclimate.com/github/zorg/zorg-gpio)
[![Coverage Status](https://coveralls.io/repos/github/zorg/zorg-gpio/badge.svg?branch=master)](https://coveralls.io/github/zorg/zorg-gpio?branch=master)

Zorg (https://zorg.github.io/) is a Python
framework for robotics and physical computing.

This module provides drivers for [General Purpose Input/Output (GPIO)](https://en.wikipedia.org/wiki/General_Purpose_Input/Output) devices. Typically, this library is registered by an adaptor class such as [`zorg-edison`](https://github.com/zorg/zorg-edison) that supports the needed interfaces for GPIO devices.

## Getting Started
Install the module with: `pip install zorg zorg-gpio`

## [Documentation](http://zorg-gpio.readthedocs.org/)

## Example
```python
import time
import zorg


def blink_led(my):
    while True:
        my.led.toggle()
        time.sleep(100)

robot = zorg.robot({
    "name": "Test",
    "connections": {
        "edison": {
            "adaptor": "zorg_edison.Edison",
        },
    },
    "devices": {
        "led": {
            "connection": "edison",
            "driver": "zorg_gpio.Led",
            "pin": 4, # Digital pin 4
        },
    },
    "work": blink_led,
})

robot.start()
```

## Hardware Support
Zorg has a extensible system for connecting to hardware devices.
The following GPIO devices are currently supported:

- [Temperature sensor](docs/temperature_sensor.md)
- [Light sensor](docs/light_sensor.md)
- Microphone
- Touch sensor
- Rotary Angle Sensor
- [Button](docs/button.md)
- [Analog Sensor](docs/analog_sensor.md)
- [Digital Sensor](docs/digital_sensor.md)
- [LED](docs/led.md)
- [Relay](docs/relay.md)
- [Servo](docs/servo.md)
- Buzzer

[Open a new issue](https://github.com/zorg/zorg-gpio/issues/new) to request support for additional components.

## License
[Copyright (c) 2015 Team Zorg](https://github.com/zorg/zorg/blob/master/LICENSE.md)
