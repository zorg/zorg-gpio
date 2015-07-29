from zorg.driver import Driver


class Button(Driver):

    def __init__(self, options, connection):
        super(Button, self).__init__(options, connection)

        self.pressed = False;
        self.previous_state = -1;

        self.commands = ["is_pressed", "is_bumped"]

    def is_pressed(self):

        # Read the current state of the button
        reading = self.connection.digital_read(self.pin)
        self.pressed = (reading > 0)

        self.previous_state = reading

        return self.pressed

    def is_bumped(self):
        """
        Returns true when the current state
        is not equal to the previous state.
        """

        # Read the current state of the button
        reading = self.connection.digital_read(self.pin)
        self.pressed = (reading > 0)

        if self.pressed == True and self.previous_state < 1:
            self.previous_state = reading
            return True

        if self.pressed == False and self.previous_state > 0:
            self.previous_state = reading
            return True

        return False

