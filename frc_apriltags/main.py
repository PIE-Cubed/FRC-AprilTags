# Created by Alex Pereira

# Import Libraries
import cv2 as cv
import numpy as np

# Import Classes
from stream    import Streaming
from camera    import USBCamera
from apriltags import Detector

# Instance creation
detector  = Detector()

# Defines the camera resolutions (width x height)
cameraRes = (1280, 720)

# Creates a VideoCapture and calibrates it
camera    = USBCamera(camNum = 0, path = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.4:1.0-video-index0", resolution = cameraRes, calibrate = True)
cap       = camera.resize(cameraRes)
ret, camMatrix, camdistortion, rvecs, tvecs = camera.calibrateCamera()

# Creates a camera for the drivers
driverCam = Streaming(camNum = 1, path = "/dev/v4l/by-path/platform-70090000.xusb-usb-0:2.2:1.0-video-index0")

# Delete unused variables
del ret, rvecs, tvecs

# Main loop
while (cap.isOpened() == True):
    # Reads the capture
    sucess, stream = cap.read()

    # Undistorts the image
    stream = camera.undistort(stream, camMatrix, camdistortion, cameraRes)

    # Runs April Tag detection on the undistorted image
    results, stream = detector.detectTags(stream, camMatrix, 0)

    # Displays the capture
    # cv.imshow("Stream", stream)

    # Press q to end the program
    if ( cv.waitKey(1) == ord("q") ):
        print("Process Ended by User")
        cv.destroyAllWindows()
        cap.release()
        break