# Import Libraries
from pathlib import Path
from wpimath.geometry import *
from frc_apriltags import Detector, USBCamera
from frc_apriltags.Utilities import Logger

# Import Methods
from frc_apriltags import startNetworkComms

# Starts the network communications
startNetworkComms(2199)

# Gets the directory path
dirPath = Path(__file__).absolute().parent.__str__()
Logger.setLogPath(dirPath)

# Defines the camera resolution (width x height)
tagCamRes = (1280, 720)

# Creates a USBCamera and calibrates it
camera = USBCamera(camNum = 0, camPath = None, resolution = tagCamRes, fps = 30, calibrate = True, dirPath = dirPath)
camMatrix = camera.getMatrix()

# Prealocate space for the detection stream
stream = camera.prealocateSpace()

# Instance creation
detector = Detector(size = 6)

# Main loop
while (True):
    # Gets the stream
    stream = camera.getUndistortedStream()

    # Runs April Tag detection on the undistorted image
    results, stream = detector.detectTags(stream, camMatrix, 0)

    # Press q to end the program
    if ( camera.getEnd() == True ):
        break