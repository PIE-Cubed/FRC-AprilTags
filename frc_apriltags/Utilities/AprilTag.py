# Import Libraries
import typing
from   wpimath.geometry import *

# Start of the AprilTag class
class AprilTag:
    """
    Use this class to generate an object with the properties of an AprilTag.
    """
    @typing.overload
    def __init__(self) -> None:
        """
        Constructor for the AprilTag class.
        """
        # Creates a default tag
        self.id = 0
        self.pose = Pose3d()

    @typing.overload
    def __init__(self, id: int, pose: Pose3d) -> None:
        """
        Constructor for the AprilTag class.
        @param tagId
        @param Pose3d
        """
        # Localize parameters
        self.id = id
        self.pose = pose

    @typing.overload
    def __init__(self, id: int, trans: Translation3d, rot: Rotation3d) -> None:
        """
        Constructor for the AprilTag class.
        @param tagId
        @param Translation3d
        @param Rotation3d
        """
        # Localize parameters
        self.id = id
        self.pose = Pose3d(trans, rot)

    @typing.overload
    def __init__(self, id: int, x: float, y: float, z: float, rMatrix) -> None:
        """
        Constructor for the AprilTag class.
        @param tagId
        @param x: The x offset in meters
        @param y: The y offset in meters
        @param z: The z offset in meters
        @param rMatrix: The 3x3 Rotation Matrix
        """
        # Generate 3D parts
        rot   = Rotation3d(rMatrix)
        trans = Translation3d(x, y, z)

        # Localize parameters
        self.id = id
        self.pose = Pose3d(trans, rot)

    @typing.overload
    def __init__(self, id: int, x: float, y: float, z: float, quaterion: Quaternion) -> None:
        """
        Constructor for the AprilTag class.
        @param tagId
        @param x: The x offset in meters
        @param y: The y offset in meters
        @param z: The z offset in meters
        @param quaterion: The 4x4 Wuaterion
        """
        # Generate 3D parts
        rot   = Rotation3d(quaterion)
        trans = Translation3d(x, y, z)

        # Localize parameters
        self.id = id
        self.pose = Pose3d(trans, rot)

    @typing.overload
    def __init__(self, id: int, x: float, y: float, z: float, roll: float, pitch: float, yaw: float) -> None:
        """
        Constructor for the AprilTag class.
        @param tagId
        @param x: The x offset in meters
        @param y: The y offset in meters
        @param z: The z offset in meters
        @param roll: Rotaton around the tag's z axis in radians
        @param pitch: Rotation around the tags's x axis in radians
        @param yaw: Rotation around the tag's y axis in radians
        """
        # Generate 3D parts
        rot   = Rotation3d(roll, pitch, yaw)
        trans = Translation3d(x, y, z)

        # Localize parameters
        self.id = id
        self.pose = Pose3d(trans, rot)

    def getId(self) -> int:
        """
        Gets the id of the given tag.
        @return tagId
        """
        return self.id

    def getPose(self) -> Pose3d:
        """
        Gets the pose of the given tag.
        @return tagPose
        """
        return self.pose