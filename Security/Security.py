#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
from time import gmtime, strftime
from LCD.LCD import LCD
from Camera.Camera import Camera


class Security:
    def __init__(self, motion_pin=17, button_pin=18, sleep_in_seconds=5):
        # Variables
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(motion_pin, GPIO.IN)
        GPIO.setup(button_pin, GPIO.IN)
        GPIO.setup(button_pin, GPIO.OUTPUT)

        self.is_armed = False
        self.is_recording = False
        self.sleep_in_seconds = sleep_in_seconds
        self.motion_pin = motion_pin
        self.button_pin = button_pin
        self.debounce = 0.15

        # Initialize LCD
        self.lcd = LCD()

        # Initialize Camera
        self.camera = Camera()

    def start_recording(self):
        if self.is_armed:

            if not self.is_recording:
                # '2016-01-01=11:11:69'
                timestamp = strftime("video/%Y-%m-%d-%H:%M:%S", gmtime())

                print("Starting Recording")

                # Save in h264 format
                # https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC
                self.camera.start_recording("{0}.h264".format(timestamp))

                self.is_recording = True

    def stop_recording(self):
        if self.is_recording:
            print("Stop recording")
            self.camera.stop_recording()
            self.is_recording = False

    def toggle_armed(self):
        self.is_armed = not self.is_armed

        print("Alarm Armed = {0}".format(self.is_armed))

        if self.is_armed:
            sleep(self.sleep_in_seconds)
        else:
            self.stop_recording()

    def secure_up(self):
        try:
            while True:
		sleep(self.debounce)
                gpio_motion = GPIO.input(self.motion_pin)
                gpio_button = GPIO.input(self.button_pin)

                if not gpio_button:
                    self.toggle_armed()

                if gpio_motion:
                    self.start_recording()
                else:
                    self.stop_recording()

        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup()  # cleanup all GPIO

            if self.is_recording:
                self.camera.stop_recording()
