import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import atexit

class LazerControl:

    def __init__(self, pin_number=18):
        self.lazer_pin = pin_number
        GPIO.setup(pin_number, GPIO.OUT)
        atexit.register(self._atexit)

    def _atexit(self):
        GPIO.cleanup()

    def on(self):
        GPIO.output(self.lazer_pin, 1)

    def off(self):
        GPIO.output(self.lazer_pin, 0)

