from pathlib import Path
from wpimath.geometry import *
from frc_apriltags import BasicStreaming
from frc_apriltags.Utilities import Logger

# Gets the directory path
dirPath = Path(__file__).absolute().parent.__str__()
Logger.setLogPath(dirPath)

# Defines the camera resolution (width x height)
camRes = (360, 240)

# Creates a camera for the drivers
driverCam = BasicStreaming(camNum = 0, resolution = camRes)

# Main loop
while (True):
    pass