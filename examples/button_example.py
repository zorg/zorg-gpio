import zorg
import time


def work(my):
    while True:
        reading = my.button.is_pressed()
        print("touched:", reading)
        time.sleep(0.5)

robot = zorg.robot({
    "name": "Test",
    "connections": {
        "edison": {
            "adaptor": "zorg_edison.Edison",
        },
    },
    "devices": {
        "button": {
            "connection": "edison",
            "driver": "zorg_gpio.Button",
            "pin": 4, # Digital pin 4
        },
    },
    "work": work,
})

robot.start()
