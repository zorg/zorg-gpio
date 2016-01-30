from zorg.driver import Driver


class TouchSensor(Driver):

    def __init__(self, options, connection):
        super(TouchSensor, self).__init__(options, connection)

        self.commands = ["is_pressed"]

    def is_pressed(self):
        """
        Returns true if the touch sensor is pressed.
        """
        reading = self.connection.digital_read(self.pin)

        return (reading > 0)
