# zorg-gpio

[![Build Status](https://travis-ci.org/zorg-framework/zorg-gpio.svg)](https://travis-ci.org/zorg-framework/zorg-gpio)
[![Code Climate](https://codeclimate.com/github/zorg-framework/zorg-gpio/badges/gpa.svg)](https://codeclimate.com/github/zorg-framework/zorg-gpio)
[![Coverage Status](https://img.shields.io/coveralls/zorg-framework/zorg-gpio.svg)](https://coveralls.io/r/zorg-framework/zorg-gpio)

Zorg (https://zorg-framework.github.io/) is a Python framework for robotics and
physical computing.

This module provides drivers for [General Purpose Input/Output (GPIO)](https://en.wikipedia.org/wiki/General_Purpose_Input/Output) devices. Typically, this library is registered by an adaptor class such as `zorg-edison` (https://github.com/zorg/zorg-edison) that supports the needed interfaces for GPIO devices.

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

- [Analog Sensor](docs/analog_sensor.md)
- [Temperature sensor](docs/temperature_sensor.md)
- Microphone
- [Light sensor](docs/light_sensor.md)
- Touch sensor
- Rotary Angle Sensor
- [Button](docs/button.md)
- [LED](docs/led.md)
- [Relay](docs/relay.md)
- [Servo](docs/servo.md)
- Buzzer

[Open a new issue](https://github.com/zorg-framework/zorg-gpio/issues/new) to request support for additional components.

## License
[Copyright (c) 2015 Team Zorg](https://github.com/zorg-framework/zorg/blob/master/LICENSE.md)
