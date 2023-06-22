# Import libraries
import time
import ntcore
from   networktables import NetworkTablesInstance
from   importlib_metadata import PackageNotFoundError, version

# Generate the version
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

# Starts the NetworkTables
@staticmethod
def startNetworkComms(teamNumber: int = 2199):
    """
    Starts an NT4 server and client for a specific team.

    :param teamNumber: Your FRC team's number.
    """
    # Ensures that a team number is a least 4 character long
    teamStr = str(teamNumber)
    teamStr.zfill(4)
 
    # Waits for the Rio to start
    time.sleep(5)

    # Gets the default NetworkTables instance
    ntinst = NetworkTablesInstance.getDefault() # Get a NetworkTables Instance

    # Initializes the NetworkTables
    ntinst.initialize(server = "10." + teamStr[:2] + "." + teamStr[2:] + ".2")

    # Create the NT4 server and client
    nt = ntcore.NetworkTableInstance.getDefault()
    nt.setServerTeam(teamNumber)
    nt.startClient4(__file__)

    # Create the NetworkTables
    ntinst.startClientTeam(teamNumber)