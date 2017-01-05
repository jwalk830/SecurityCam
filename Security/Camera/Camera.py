import picamera
from time import sleep


class Camera:
    def __init__(self):
        # Camera
        self.camera = picamera.PiCamera()
        self.configure_camera()

    def configure_camera(self):
        # self.camera.resolution = (1024,768)
        self.camera.sharpness = 0
        self.camera.contrast = 0
        self.camera.brightness = 50
        self.camera.saturation = 0
        self.camera.ISO = 0
        self.camera.video_stabilization = False
        self.camera.exposure_compensation = 0
        self.camera.exposure_mode = 'auto'
        self.camera.meter_mode = 'average'
        self.camera.awb_mode = 'auto'
        self.camera.image_effect = 'none'
        self.camera.color_effects = None
        self.camera.rotation = 0
        self.camera.hflip = False
        self.camera.vflip = False
        self.camera.crop = (0.0, 0.0, 1.0, 1.0)

        self.camera.start_preview()

        # Camera warm-up time
        print("Camera warm-up time")
        sleep(2)

    def start_recording(self, video_name):
        self.camera.start_recording(video_name)

    def stop_recording(self):
        self.camera.stop_recording()
