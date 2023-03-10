from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("frc-apriltags")
except PackageNotFoundError:
    # Package is not installed
    pass

from .Logger              import Logger
from .Units               import Units
from .MathUtil            import MathUtil
from .AprilTag            import AprilTag
from .AprilTagFieldLayout import AprilTagFieldLayout

__all__ = ["Logger", "Units", "MathUtil", "AprilTag", "AprilTagFieldLayout"]
