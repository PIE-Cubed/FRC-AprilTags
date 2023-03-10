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
from .stream         import BasicStreaming, CustomStreaming

__all__ = ["Detector", "Calibrate", "NetworkCommunications", "USBCamera", "BasicStreaming", "CustomStreaming"]
