# Import Classes
from frc_apriltags.stream    import BasicStreaming
from frc_apriltags.camera    import USBCamera
from frc_apriltags.apriltags import Detector

# Defines the camera resolutions (width x height)
tagCamRes    = (1280, 720)

# Creates a USBCamera and calibrates it
camera    = USBCamera(camNum = 0, path = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.4:1.0-video-index0", resolution = tagCamRes, calibrate = False)
camMatrix = camera.getMatrix()

# Creates a camera for the drivers
driverCam = BasicStreaming(camNum = 1, path = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.2:1.0-video-index0")

# Prealocate space for the detection stream
stream = camera.prealocateSpace(tagCamRes)

# Instance creation
detector  = Detector()

# Main loop
while (True):
    # Gets the stream
    stream = camera.getUndistortedStream()

    # Runs April Tag detection on the undistorted image
    results, stream = detector.detectTags(stream, camMatrix, 0)

    # Displays the stream
    camera.displayStream()

    # Press q to end the program
    if ( camera.getEnd() == True ):
        break