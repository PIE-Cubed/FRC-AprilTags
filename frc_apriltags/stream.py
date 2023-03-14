# Import Libraries
from cscore import CameraServer as CS

# Import Classes
from frc_apriltags import USBCamera

# Import Utilities
from frc_apriltags.Utilities import Logger

# Creates the BasicStreaming Class
class BasicStreaming:
    """
    Use this class to stream unprocessed images to the driver station.

    :param camNum: The camera number.
    :param path: Can be found on Linux by running ``find /dev/v4l``.
    :param resolution: Width by height.
    """
    def __init__(self, camNum: int, path: str = None, resolution: tuple = (640, 480)) -> None:
        """
        Constructor for the BasicStreaming class.

        @param camNum: The camera number.
        @param path: Can be found on Linux by running ``find /dev/v4l``.
        @param resolution: Width by height.
        """
        # Creates a CameraServer
        CS.enableLogging()

        # Captures from a specified USB Camera on the system
        if (path is not None):
            # If path is known, use the path
            camera = CS.startAutomaticCapture(name = "Camera" + str(camNum), path = path)
        else:
            # Path is unknown, use the camera number
            camera = CS.startAutomaticCapture(dev = camNum)
        camera.setResolution(resolution[0], resolution[1])

        # Updates log
        Logger.logInfo("Stream initialized for camera " + str(camNum), True)

    def enableLogging(self):
        """
        Enables logging for this class.
        """
        self.logStatus = True

# Creates the CustomStreaming Class
class CustomStreaming:
    """
    Use this class to stream processed images back to the driver station.

    :param camNum: The camera number.
    :param path: Can be found on Linux by running ``find /dev/v4l``.
    :param resolution: Width by height.
    :param fps: The desired fps of the camera.
    """
    def __init__(self, camNum: int, path: str = None, resolution: tuple = (640, 480), fps: int = 15) -> None:
        """
        Constructor for the CustomStreaming class.

        @param camNum: The camera number.
        @param path: Can be found on Linux by running ``find /dev/v4l``.
        @param resolution: Width by height.
        @param fps: The desired fps of the camera.
        """
        # Creates a USBCamera
        self.camera = USBCamera(camNum = camNum, camPath = path, resolution = resolution, fps = fps, calibrate = False)

        # Creates a CameraServer
        CS.enableLogging()

        # Setup a CvSource. This will send images back to the Dashboard
        self.outputStream = CS.putVideo(name = "Camera " + str(camNum), width = resolution[0], height = resolution[1])

        # Preallocates for the incoming image
        self.img = self.camera.prealocateSpace()

        # Updates log
        Logger.logInfo("Stream initialized for camera " + str(camNum), True)

    def streamImage(self, stream = None):
        """
        Streams the camera back to ShuffleBoard for driver use.

        :param stream: A processed stream.
        :return: The processed stream.
        """
        # Grab a frame from the camera and put it in the source image
        if (stream is not None):
            self.img = stream
        else:
            self.img = self.camera.getStream()

        # Sends an image back to ShuffleBoard
        self.outputStream.putFrame(self.img)

        return self.img

    def getUnprocessedStream(self):
        """
        Gets the unprocessed stream of this camera.

        Note: Image processing must happen outside of this class.
        """
        return self.camera.getStream()

    def enableLogging(self):
        """
        Enables logging for this class.
        """
        self.logStatus = True