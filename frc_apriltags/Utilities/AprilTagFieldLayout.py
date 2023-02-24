# Import Libraries
import json
import numpy as np
from enum import Enum
from typing import Sequence
from importlib import resources
from wpimath.geometry import *

# Import Utilities
from frc_apriltags.Utilities.Logger import Logger
from frc_apriltags.Utilities.AprilTag import AprilTag

# Creates the AprilTagFieldLayout class
class   AprilTagFieldLayout:
    class Origin(Enum):
        kBlueAllianceWallRightSide = "BlueWall"
        kRedAllianceWallRightSide  = "RedWall"

    def __init__(self, tags: Sequence[AprilTag], fieldLength: float, fieldWidth: float, isRed = False) -> None:
        """
        Generates an field with AprilTags for testing
        @param allTags: A list of all known tags
        @param fieldLength: The length (y) of the field in meters
        @param fieldWidth: The width (x) of the field in meters
        @param isRed: If you are on the red alliance
        """
        # Asserts that the array length is no greater than 8
        assert(len(tags) <= 8)

        # Localize parameters
        self.fieldLength = fieldLength
        self.fieldWidth = fieldWidth

        # Logs the field size
        Logger.logInfo("Field length: {}, Field width: {}".format(self.fieldLength, self.fieldWidth), True)

        # Creates the allTags array
        self.allTags = [Pose3d()] * 9

        # Sorts the data from tags into allTags
        for tag in tags:
            id   = tag.getId()
            pose = tag.getPose()

            self.allTags[id] = pose

            # Logs the tag information
            Logger.logInfo("Tag {}. Pose: {}".format(id, pose), True)

        # Variables
        self.m_origin  = None
        self.logStatus = False

        # Sets the origin depending on alliance
        if (isRed == True):
            self.setOrigin(AprilTagFieldLayout.Origin.kRedAllianceWallRightSide)
        elif (isRed == False):
            self.setOrigin(AprilTagFieldLayout.Origin.kBlueAllianceWallRightSide)

    @classmethod
    def fromJson(cls, name: str, isRed: bool):
        """
        Extracts information from the json file about field size and tag locations
        @param name: The name of the json file in the year-gamename format
        @param isRed: If you are on the red alliance
        """
        # Creates a blank array of AprilTags
        allTags = [AprilTag] * 8

        # Returns the JSON as a dictionary
        with resources.open_binary("frc_apriltags.Tag_Layouts", name + ".json") as fp:
            data = json.load(fp)

        # Loops through the json data
        for tag in data["tags"]:
            # Gets the tag ID
            id = tag["ID"]

            # Gets the tag's translation data
            x_trans = tag["pose"]["translation"]["x"]
            y_trans = tag["pose"]["translation"]["y"]
            z_trans = tag["pose"]["translation"]["z"]

            # Gets the tag's rotation data
            w_rot = tag["pose"]["rotation"]["quaternion"]["W"]
            x_rot = tag["pose"]["rotation"]["quaternion"]["X"]
            y_rot = tag["pose"]["rotation"]["quaternion"]["Y"]
            z_rot = tag["pose"]["rotation"]["quaternion"]["Z"]

            # Creates a quaternion
            q = Quaternion(w_rot, x_rot, y_rot, z_rot)

            # Creates a Pose3d object
            pose = Pose3d(x_trans, y_trans, z_trans, Rotation3d(q))

            # Adds the tag to the allTags array
            allTags[id - 1] = AprilTag.fromPose3d(id, pose)

        # Sets the field dimensions
        fieldLength = data["field"]["length"]
        fieldWidth  = data["field"]["width"]

        # Returns an instance of the class
        return cls(allTags, fieldLength, fieldWidth, isRed)

    def setOrigin(self, origin):
        """
        Sets the origin depending on the alliance color. The origins are calculated from the field dimensions.

        This transforms the Pose3ds returned by getTagPose() to return the correct pose relative to a predefined coordinate frame.
        @param origin: The predefined origin
        """
        # Sets the origin
        if (origin == AprilTagFieldLayout.Origin.kBlueAllianceWallRightSide):
            self.m_origin = Pose3d()
        elif (origin == AprilTagFieldLayout.Origin.kRedAllianceWallRightSide):
            self.m_origin = Pose3d(
                Translation3d(self.fieldLength, self.fieldWidth, 0),
                Rotation3d(0, 0, np.pi)
            )
        else:
            origin = None
            raise ValueError("Unsupported enumerator value.")
        
        # Logs the origin
        Logger.logInfo("Origin at {}".format(origin), self.logStatus)

    def getTags(self):
        """
        Returns all the created tags
        @return allTags
        """
        return self.allTags

    def getTagPose(self, id: int) -> Pose3d:
        """
        Returns the pose of the selected tag
        @return Pose3d
        """
        if (type(self.allTags[id]) is not Pose3d):
            return Pose3d()
        else:
            return self.allTags[id].relativeTo(self.m_origin)

    def enableLogging(self):
        """
        Enables logging for this module
        """
        self.logStatus = True