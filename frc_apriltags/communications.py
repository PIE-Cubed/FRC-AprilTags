# Import Libraries
import ntcore
from   networktables import *

# Import Utilities
from frc_apriltags.Utilities.Logger import Logger

# Creates the NetworkCommunications Class
class NetworkCommunications:
    """
    Use this class to communicate with the RoboRio over NetworkTables.
    """
    def __init__(self) -> None:
        """
        Constructor for the NetworkCommunications class.
        """
        # Variables
        self.logStatus  = False
        self.teamNumber = 2199

        # Get a default network table
        nt = ntcore.NetworkTableInstance.getDefault()
        nt.setServerTeam(self.teamNumber)
        nt.startClient3(__file__)

        # Start a NetworkTables client
        NetworkTables.startClientTeam(self.teamNumber)

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
        tagId = result[0]
        pose  = result[1]

        # Sets the tag value
        self.setBestResultId(tagId)

        # Extracts the x, y, and z translations relative to the field's WCS
        x, y, z = pose.X(), pose.Y(), pose.Z()

        # Extracts the tag's roll, yaw, and pitch relative to the field's WCS
        roll, pitch, yaw = pose.rotation().X(), pose.rotation().Y(), pose.rotation().Z()

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
    
    def setTeamNumber(self, number: int = 2199):
        """
        Sets your FRC Team number.
        """
        self.teamNumber = number

    def enableLogging(self):
        """
        Enables logging for this module
        """
        self.logStatus = True