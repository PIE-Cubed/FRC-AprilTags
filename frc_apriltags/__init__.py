from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("frc-apriltags")
except PackageNotFoundError:
    # Package is not installed
    pass

# Import AprilTag related classes
from .communications import NetworkCommunications
from .apriltags      import Detector

# Import Vision related classes
from .calibration    import Calibrate
from .camera         import USBCamera
from .stream         import Streaming

__all__ = [
    "Detector",
    "Calibrate",
    "NetworkCommunications",
    "USBCamera",
    "Streaming"
]

@staticmethod
def startNetworkComms(teamNumber: int = 2199):
    """
    Starts an NT4 server and client for a specific team.

    :param teamNumber: Your FRC team's number.
    """
    import time
    import ntcore
    from   networktables import NetworkTables

    # Waits for the Rio to start
    time.sleep(5)

    # Initializes the NetworkTables
    NetworkTables.initialize(server = "roborio-" + str(teamNumber) + "-frc.local")

    # Create the NT4 server and client
    nt = ntcore.NetworkTableInstance.getDefault()
    nt.setServerTeam(teamNumber)
    nt.startClient4(__file__)

    # Create the NetworkTables
    NetworkTables.startClientTeam(teamNumber)