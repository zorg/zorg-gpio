import zorg
import time


def work(my):
    while True:
        reading = my.touch_sensor.is_pressed()
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
        "touch_sensor": {
            "connection": "edison",
            "driver": "zorg_gpio.TouchSensor",
            "pin": 4, # Digital pin 4
        },
    },
    "work": work,
})

robot.start()
