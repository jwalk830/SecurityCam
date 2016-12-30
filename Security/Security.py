from gpiozero import MotionSensor, Button
from time import sleep


class Security:
    def __init__(self, motion_pin = 17, button_pin = 18, sleep_in_seconds = 5):
        #Variables
        pir = MotionSensor(motion_pin)
        button = Button(button_pin)
        self.is_armed = False
        self.is_recording = False
        self.sleep_in_seconds = sleep_in_seconds
        
        #Event Handlers
        pir.when_motion = self.start_recording
        pir.when_no_motion = self.stop_recording
        button.when_pressed = self.toggle_armed

    def start_recording():
        if self.is_armed:
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

