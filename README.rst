zorg-gpio
=========

|Join the chat at https://gitter.im/zorg/zorg| |Package Version|
|Requirements Status| |Build Status| |Code Climate| |Coverage Status|

Zorg (https://zorg.github.io/) is a Python framework for robotics and
physical computing.

This module provides drivers for `General Purpose Input/Output
(GPIO) <https://en.wikipedia.org/wiki/General_Purpose_Input/Output>`__
devices. Typically, this library is registered by an adaptor class such
as ```zorg-edison`` <https://github.com/zorg/zorg-edison>`__ that
supports the needed interfaces for GPIO devices.

Getting Started
---------------

Install the module with: ``pip install zorg zorg-gpio``

`Documentation <http://zorg-gpio.readthedocs.org/>`__
-----------------------------------------------------

Example
-------

.. code:: python

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

Hardware Support
----------------

Zorg has a extensible system for connecting to hardware devices. The
following GPIO devices are currently supported:

-  `Light sensor <docs/light_sensor.md>`__
-  `Button <docs/button.md>`__
-  `Analog Sensor <docs/analog_sensor.md>`__
-  `Digital Sensor <docs/digital_sensor.md>`__
-  `LED <docs/led.md>`__
-  `Relay <docs/relay.md>`__
-  `Buzzer <docs/buzzer.md>`__

`Open a new issue <https://github.com/zorg/zorg-gpio/issues/new>`__ to
request support for additional components.

License
-------

`Copyright (c) 2015 Team
Zorg <https://github.com/zorg/zorg/blob/master/LICENSE.md>`__

.. |Join the chat at https://gitter.im/zorg/zorg| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/zorg/zorg?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Package Version| image:: https://img.shields.io/pypi/v/zorg-gpio.svg
   :target: https://pypi.python.org/pypi/zorg-gpio/
.. |Requirements Status| image:: https://requires.io/github/zorg/zorg-gpio/requirements.svg?branch=master
   :target: https://requires.io/github/zorg/zorg-gpio/requirements/?branch=master
.. |Build Status| image:: https://travis-ci.org/zorg/zorg-gpio.svg?branch=master
   :target: https://travis-ci.org/zorg/zorg-gpio
.. |Code Climate| image:: https://codeclimate.com/github/zorg/zorg-gpio/badges/gpa.svg
   :target: https://codeclimate.com/github/zorg/zorg-gpio
.. |Coverage Status| image:: https://coveralls.io/repos/github/zorg/zorg-gpio/badge.svg?branch=master
   :target: https://coveralls.io/github/zorg/zorg-gpio?branch=master
