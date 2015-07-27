from zorg.driver import Driver


class Relay(Driver):

    def __init__(self, options, connection):
        super(Relay, self).__init__(options, connection)

        self.current_state = False

        self.commands = [
            "set_state",
            "is_on",
            "turn_on",
            "turn_off",
            "toggle",
        ]

    def set_state(self, state):
        """
        State should be a 1 or a 0.
        """
        self.current_state = (state == 1)
        self.connection.digital_write(self.pin, state)

    def is_on(self):
        return self.current_state

    def turn_on(self):
        self.current_state = True
        self.connection.digital_write(self.pin, 1)

    def turn_off(self):
        self.current_state = False
        self.connection.digital_write(self.pin, 0)

    def toggle(self):
        if self.is_on():
            self.turn_off()
        else:
            self.turn_on()

