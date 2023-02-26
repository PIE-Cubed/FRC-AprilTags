# Import Libraries
import cv2   as cv
import numpy as np

# Import Classes
from frc_apriltags.calibration import Calibrate

# Import Utilities
from frc_apriltags.Utilities.Logger import Logger

# Creates the USBCamera class
class USBCamera:
    """
    Use this class to create a USBCamera.
    """
    def __init__(self, camNum: int, path: str = None, resolution: tuple = (0, 0), calibrate: bool = False) -> None:
        """
        Constructor for the USBCamera class.
        @param camNumber
        @param path: It can be found on Linux by running "find /dev/v4l"
        @param calinbrate: Should the camera be calibrated this camera
        """
        # Set camera properties
        self.camNum = camNum

        # Init variables
        self.logStatus  = False
        self.resolution = resolution

        # Creates a capture
        if (path is not None):
            # If path is known, use the path
            self.cap = cv.VideoCapture(path)
        else:
            # Path is unknown, use the camera number
            self.cap = cv.VideoCapture(self.camNum)
        
        # Resizes the capture
        self.resize(resolution)

        # Calibrates if told to do so
        if (calibrate == True):
            self.calibrateCamera()

        # Updates log
        Logger.logInfo("USBCamera initialized for camera " + str(camNum), True)

    def resize(self, cameraRes: tuple):
        """
        Resizes the capture to a given resolution. If the specified resolution is too high, resizes to the highest resolution possible.
        @param Camera Resolution
        @return resizedCapture
        """
        # CONSTANTS
        HIGH_VALUE = 10000

        # Set the values
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, cameraRes[0])
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, cameraRes[1])
        self.cap.set(cv.CAP_PROP_FPS, HIGH_VALUE)

        # Gets the highest value they go to
        width  = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps    = int(self.cap.get(cv.CAP_PROP_FPS))

        # Set the capture to be MJPG format
        self.cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

        # Prealocate space for stream
        self.stream = self.prealocateSpace((width, height))

        # Prints telemetry
        print("Resolution:", str(width) + "x" + str(height))
        print("Max FPS:", fps)

        # Updates log
        Logger.logInfo("Capture resized", self.logStatus)

    def undistort(self, stream):
        """
        Undistorts an image using cv.undistort()
        @param stream
        @param cameraMatrix
        @param cameraDistortion
        @param cameraResolution (width, height)
        @return undistortedStream
        """
        # Creates a cameraMatrix
        newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(self.camMatrix, self.camdistortion, self.resolution, 1, self.resolution)

        # Undistorts the image
        undistortedStream = cv.undistort(stream, self.camMatrix, self.camdistortion, None, newCameraMatrix)

        # Crops the image
        x, y, w, h = roi
        undistortedStream = undistortedStream[y:y+h, x:x+w]

        return undistortedStream

    def calibrateCamera(self):
        """
        Calibrates the camera and gets the calibration parameters
        """
        # Instance creation
        self.calibrate = Calibrate(self.cap, self.camNum, 15)

        # Get results
        ret, self.camMatrix, self.camdistortion, rvecs, tvecs = self.calibrate.calibrateCamera()
    
    def prealocateSpace(self, cameraRes):
        """
        Prealocates space for the stream.
        @param cameraResolution
        @return blankArray
        """
        return np.zeros(shape = (cameraRes[1], cameraRes[0], 3), dtype = np.uint8)

    def getStream(self):
        """
        Gets the stream from this camera's capture
        @return stream
        """
        # Reads the capture
        __, self.stream = self.cap.read()

        return self.stream

    def getUndistortedStream(self):
        """
        Gets the stream from this camera's capture
        @return stream
        """
        # Reads the capture
        __, self.stream = self.cap.read()

        # Undistorts the stream
        self.stream = self.undistort(self.stream)

        return self.stream

    def getEnd(self):
        """
        Checks if the program should end
        """
        if (cv.waitKey(1) == ord("q")):
            print("Process Ended by User")
            cv.destroyAllWindows()
            self.cap.release()
            return True
        else:
            return False

    def getMatrix(self):
        """
        Returns the intrinsic camera matrix
        @return cameraMatrix
        """
        return self.camMatrix

    def displayStream(self):
        """
        Displays a flipped version of the stream 
        """
        cv.imshow("Stream", cv.flip(self.stream, 1))

    def enableLogging(self):
        """
        Enables logging for this module
        """
        self.logStatus = True