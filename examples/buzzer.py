import time
import zorg


def buzz(my):
    while True:
        my.buzzer.toggle()
        time.sleep(0.5)

robot = zorg.robot({
    "name": "Test",
    "connections": {
        "edison": {
            "adaptor": "zorg_edison.Edison",
        },
    },
    "devices": {
        "buzzer": {
            "connection": "edison",
            "driver": "zorg_gpio.Buzzer",
            "pin": 4, # Digital pin 4
        },
    },
    "work": buzz,
})

robot.start()
