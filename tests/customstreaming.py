# Import Libraries
import cv2 as cv
from   pathlib import Path
from   wpimath.geometry import *
from   frc_apriltags import Streaming
from   frc_apriltags.Utilities import Logger

# Import Methods
from frc_apriltags import startNetworkComms

# Starts the network communications
startNetworkComms(2199)

# Gets the directory path
dirPath = Path(__file__).absolute().parent.__str__()
Logger.setLogPath(dirPath)

# Defines the camera resolution (width x height)
camRes = (360, 240)

# Creates a camera for the drivers
driverCam = Streaming(camNum = 0, resolution = camRes, fps = 20)

# Prealocate space for the detection stream
stream = driverCam.prealocateSpace()

# Main loop
while (True):
    # Gets the stream
    stream = driverCam.getStream()

    # Image processing here...
    # 

    # Sends the stream back
    driverCam.streamImage(stream)

    # Press q to end the program
    if ( driverCam.getEnd() == True ):
        break