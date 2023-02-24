# Import Libraries
import numpy as np
from   networktables import *
from   wpimath.geometry import *

# Import Utilities
from frc_apriltags.Utilities.Logger import Logger

# Variables
firstTime = True

# Creates the NetworkCommunications Class
class NetworkCommunications:
    """
    Use this class to communicate with the RoboRio over NetworkTables.
    """
    def __init__(self) -> None:
        """
        Constructor for the NetworkCommunications class.
        """
        # Start a NetworkTables client
        NetworkTables.startClientTeam(2199)

        # Get a NetworkTables Instance
        ntinst = NetworkTablesInstance.getDefault()

        # FMSInfo Table
        FMSInfo = ntinst.getTable("FMSInfo")
        self.isRedAlliance = FMSInfo.getEntry("IsRedAlliance")  # Boolean

        # Create a TagInfo Table and its Entries
        TagInfo = ntinst.getTable("TagInfo")
        self.targetValid   = TagInfo.getEntry("tv")            # Boolean
        self.bestResult    = TagInfo.getEntry("BestResult")    # Double[]
        self.bestResultId  = TagInfo.getEntry("BestResultId")  # Double
        self.detectionTime = TagInfo.getEntry("DetectionTime") # Double

        # Variables
        self.logStatus = False

        # Updates log
        Logger.logInfo("NetworkCommunications initialized", True)

    def setBestResultId(self, id: int):
        """
        Sets the tag id of the best result.
        @param tagId
        """
        self.bestResultId.setDouble(id)

    def setBestResult(self, result):
        """
        Sends the best result.

        This method will send [tagId, xTranslate, yTranslate, zTranslate, yaw, pitch, roll].
        All translation data is in meters. All rotation data is in radians.
        @param result
        """
        # Gets variables from result
        tagId       = result[0]
        pose        = result[1]
        eulerAngles = result[2]

        # Sets the tag value
        self.setBestResultId(tagId)

        # Flattens the pose array into a 1D array
        flatPose = np.array(pose).flatten()

        # Flattens the eulerAngles array into a 1D array
        flatAngles = np.array(eulerAngles).flatten()

        # Extracts the x, y, and z translations relative to the field's WCS
        x, y, z = flatPose[11], flatPose[3], -flatPose[7]

        # Extracts the tag's roll, yaw, and pitch relative to the field's WCS
        roll, pitch, yaw = flatAngles[2], flatAngles[0], flatAngles[1]

        # Packs all the data
        data = (tagId, x, y, z, roll, pitch, yaw)

        # Sends the data
        self.bestResult.setDoubleArray(data)

    def setTargetValid(self, tv: bool):
        """
        Sets if a valid target was detected.
        @param tv
        """
        self.targetValid.setBoolean(tv)

    def setDetectionTimeSec(self, timeSec: float):
        """
        Sets the time when a detection was made.
        @param timeSec
        """
        self.detectionTime.setDouble(timeSec)

    def enableLogging(self):
        """
        Enables logging for this module
        """
        self.logStatus = True