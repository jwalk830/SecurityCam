from Security.Security import Security
from signal import pause

security = Security(17,18,3)
security.pir.when_motion = security.start_recording
security.pir.when_no_motion = security.stop_recording
security.button.when_pressed = security.toggle_armed
pause()