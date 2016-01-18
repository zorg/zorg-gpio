from zorg.driver import Driver
from threading import Thread

from time import sleep


class SoundThread(Thread):
    def __init__(self, piezo):
        super(SoundThread, self).__init__()
        self.piezo = piezo
        self.playing = True

    def run(self):
        while (self.playing):
            # Do usefull stuff here
            print '.',
            piezo.connection.digital_write(piezo.pin, state)
            sleep(0.1)

    def stop(self):
        self.playing = False


class Piezo(Driver):

    def __init__(self, options, connection):
        super(Piezo, self).__init__(options, connection)

        #self.thread = SoundThread(self)

        self.commands += [
            "frequency",
            "play",
            ""
        ]

    def frequency(self, frequency, duration):
        """
        Plays a tone at a given frequency (in Hz)
        for the specified number of milliseconds.
        """
        period = 1.0 / frequency
        duty = period / 2.0
        tone = int(duty * 1000000)

        self.connection.analog_write(self.pin, frequency)

        #self.thread.start()
        #sleep(duration)

        #self.thread.join()
        #print "thread finished"

    def play(self, tune):
        """
        Play a tune from a list of the notes and optional
        settings (e.g. tempo)
        """
        pass

    def tone(frequency, duration):
        """
        Play a tone for duration ms. The tone value in this case is a computed duty cycle (in microseconds). This is a lower-level method than frequency (which does the translation from frequency to tone for you). Most of the time you likely want to use frequency.
        """
        pass

    def stop_tone(self):
        """
        Stop tone playing from Piezo. Will immediately stop playing a tone (digitalWrite the output pin low) and clear any existing queued tone timers.
        """
        self.thread.stop()
        self.connection.digital_write(self.pin, 0)


