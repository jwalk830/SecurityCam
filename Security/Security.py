from time import sleep
import RPi.GPIO as GPIO


class Security:
    def __init__(self, motion_pin = 17, button_pin = 18, sleep_in_seconds = 5):
        #Variables
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motion_pin, GPIO.IN)
        GPIO.setup(button_pin, GPIO.IN)
        self.is_armed = False
        self.is_recording = False
        self.sleep_in_seconds = sleep_in_seconds
        self.motion_pin = motion_pin
        self.button_pin = button_pin

    def start_recording():
        self.is_recording = True
        print("recording")

    def stop_recording():
        if self.is_recording:
            self.is_recording = False
            print("stop recording motion")

    def toggle_armed():
        self.is_armed = not self.is_armed
        print("Toggle armed = {0}".format(is_armed))
        if self.is_armed:
            print("Pause program for {0} seconds".format(self.sleep_in_seconds))
        else:
            print("Entered not function")
            self.stop_recording()

    def secure_up(self):
        try:
            while True:
                print("motion pin = {0}".format(GPIO.input(self.motion_pin)))
                print("button pin = {0}".format(GPIO.input(self.button_pin)))
        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup() # cleanup all GPIO
