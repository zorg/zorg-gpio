from zorg.driver import Driver


class DigitalSensor(Driver):

    def __init__(self, options, connection):
        super(DigitalSensor, self).__init__(options, connection)

        self.commands += ["read"]

    def read(self):
        """
        Return the raw value of the reading from the sensor.
        """
        return self.connection.digital_read(self.pin)
