import zorg
import time


def work(my):
    while True:
        angle = my.potentiometer.read_angle()
        print(angle, "degrees")
        time.sleep(0.5)

robot = zorg.robot({
    "name": "Test",
    "connections": {
        "edison": {
            "adaptor": "zorg_edison.Edison",
        },
    },
    "devices": {
        "potentiometer": {
            "connection": "edison",
            "driver": "zorg_gpio.RotaryAngleSensor",
            "pin": 0, # Analog pin 0
        },
    },
    "work": work,
})

robot.start()
