from .analog_sensor import AnalogSensor


class RotaryAngleSensor(AnalogSensor):
    """
    This may also be known as a potentiometer.
    """

    def __init__(self, options, connection):
        super(RotaryAngleSensor, self).__init__(options, connection)

        # The value of the input voltage
        self.reference_voltage = 5

        # The angular range of the Grove rotary angle sensor is 300 degrees
        # with a linear change in value
        self.angular_range = 300

        self.commands += [
            "read_angle"
        ]

    def read_angle(self):
        """
        Read and return the current angle of the sensor in degrees.
        The rotary angle sensor produces analog output between 0 and Vcc (D1).
        """
        analog_value = self.read()

        voltage = analog_value * self.reference_voltage / 1023.0
        degrees = (voltage * self.angular_range) / self.reference_voltage

        return degrees
