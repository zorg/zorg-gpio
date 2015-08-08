from .analog_sensor import AnalogSensor


class LightSensor(AnalogSensor):

    def __init__(self, options, connection):
        super(LightSensor, self).__init__(options, connection)

        self.THRESHOLD = 0.1

        self.previous_value = -1.0

        self.commands += ["read"]

    def has_changed(self):
        """
        Returns true if the lighting level has changed
        past the acceptable threshold of the sensor.
        """

        current_value = self.connection.analog_read(self.pin)

        # The current_value can be None in some cases
        if not current_value:
            return False

        # A -1 value indicates that no change has occured yet
        if self.previous_value == -1:
            self.previous_value = current_value
            return False

        if current_value > self.previous_value + self.THRESHOLD:
            self.previous_value = current_value
            return True

        if current_value < self.previous_value - self.THRESHOLD:
            self.previous_value = current_value
            return True

        self.previous_value = current_value

        return False

