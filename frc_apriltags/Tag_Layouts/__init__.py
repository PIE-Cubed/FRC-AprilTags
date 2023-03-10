from importlib_metadata import PackageNotFoundError, version

try:
    __version__ = version("frc-apriltags")
except PackageNotFoundError:
    # Package is not installed
    pass