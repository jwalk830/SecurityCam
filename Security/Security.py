from time import sleep
import RPi.GPIO as GPIO
import picamera
from time import gmtime, strftime

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

	#Camera
	self.camera = picamera.PiCamera()
	configure_camera()   

   def configure_camera():
	camera.sharpness = 0
	camera.contrast = 0
	camera.brightness = 50
	camera.saturation = 0
	camera.ISO = 0
	camera.video_stabilization = False
	camera.exposure_compensation = 0
	camera.exposure_mode = 'auto'
	camera.meter_mode = 'average'
	camera.awb_mode = 'auto'
	camera.image_effect = 'none'
	camera.color_effects = None
	camera.rotation = 0
	camera.hflip = False
	camera.vflip = False
	camera.crop = (0.0, 0.0, 1.0, 1.0) 

   def start_recording():
	if self.is_armed:
	    # '2016-01-01=11:11:69'
	    timestamp = strftime("%Y-%m-%d=%H:%M:%S", gmtime())

            # Save in h264 format 
	    # https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC
	    camera.start_recording("{0}.h264".format(timestamp))
	    self.is_recording = True
       	    print("recording")

    def stop_recording():
        if self.is_recording:
	    camera.stop_recording()
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
                gpio_motion = GPIO.input(self.motion_pin)
                gpio_button = GPIO.input(self.button_pin)

                if not gpio_button:
                    self.toggle_armed()
                if gpio_motion:
                    self.start_recording()
                else:
                    self.stop_recording() 
                print("motion pin = {0}".format(gpio_motion)
                print("button pin = {0}".format(gpio_button)
        except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup() # cleanup all GPIO
