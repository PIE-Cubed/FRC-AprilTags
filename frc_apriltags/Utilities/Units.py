# Import libraries
import math

# Constants
kInchesPerFoot = 12.0
kMetersPerInch = 0.0254
kSecondsPerMinute = 60
kMillisecondsPerSecond = 1000
kKilogramsPerLb = 0.453592

# Start of the Units class
class Units:
    """
    Use this class to convert between commonly used FRC units.
    """
    @staticmethod
    def metersToFeet(meters):
        """
        Converts given meters to feet.
        @param meters: The meters to convert to feet.
        @return Feet: Converted from meters.
        """
        return Units.metersToInches(meters) / kInchesPerFoot

    @staticmethod
    def feetToMeters(feet):
        """
        Converts given feet to meters.
        @param feet: The feet to convert to meters.
        @return Meters: Converted from feet.
        """
        return Units.inchesToMeters(feet * kInchesPerFoot)

    @staticmethod
    def metersToInches(meters):
        """
        Converts given meters to inches.
        @param meters: The meters to convert to inches.
        @return Inches: Converted from meters.
        """
        return meters / kMetersPerInch

    @staticmethod
    def inchesToMeters(inches):
        """
        Converts given inches to meters.
        @param inches: The inches to convert to meters.
        Meters: Converted from inches.
        """
        return inches * kMetersPerInch

    @staticmethod
    def degreesToRadians(degrees):
        """
        Converts given degrees to radians.
        @param degrees: The degrees to convert to radians.
        @return Radians: Converted from degrees.
        """
        return math.radians(degrees)

    @staticmethod
    def radiansToDegrees(radians):
        """
        Converts given radians to degrees.
        @param radians: The radians to convert to degrees.
        @return Degrees: Converted from radians.
        """
        return math.degrees(radians)

    @staticmethod
    def radiansToRotations(radians):
        """
        Converts given radians to rotations.
        @param radians: The radians to convert.
        @return rotations Converted from radians.
        """
        return radians / (math.pi * 2)

    @staticmethod
    def degreesToRotations(degrees):
        """
        Converts given degrees to rotations.
        @param degrees: The degrees to convert.
        @return rotations Converted from degrees.
        """
        return degrees / 360

    @staticmethod
    def rotationsToDegrees(rotations):
        """
        Converts given rotations to degrees.
        @param rotations: The rotations to convert.
        @return degrees Converted from rotations.
        """
        return rotations * 360

    @staticmethod
    def rotationsToRadians(rotations):
        """
        Converts given rotations to radians.
        @param rotations: The rotations to convert.
        @return radians Converted from rotations.
        """
        return rotations * 2 * math.pi

    @staticmethod
    def rotationsPerMinuteToRadiansPerSecond(rpm):
        """
        Converts rotations per minute to radians per second.
        @param rpm: The rotations per minute to convert to radians per second.
        @return Radians per second: Converted from rotations per minute.
        """
        return rpm * math.pi / (kSecondsPerMinute / 2)

    @staticmethod
    def radiansPerSecondToRotationsPerMinute(radiansPerSecond):
        """
        Converts radians per second to rotations per minute.
        @param radiansPerSecond: The radians per second to convert to from rotations per minute.
        @return Rotations per minute: Converted from radians per second.
        """
        return radiansPerSecond * (kSecondsPerMinute / 2) / math.pi

    @staticmethod
    def millisecondsToSeconds(milliseconds):
        """
        Converts given milliseconds to seconds.
        @param milliseconds: The milliseconds to convert to seconds.
        @return Seconds: Converted from milliseconds.
        """
        return milliseconds / kMillisecondsPerSecond

    @staticmethod
    def secondsToMilliseconds(seconds):
        """
        Converts given seconds to milliseconds.
        @param seconds: The seconds to convert to milliseconds.
        @return Milliseconds: Converted from seconds.
        """
        return seconds * kMillisecondsPerSecond

    @staticmethod
    def kilogramsToLbs(kilograms):
        """
        Converts kilograms into lbs.
        @param kilograms: The kilograms to convert to lbs.
        @return lbs: Converted from kilograms.
        """
        return kilograms / kKilogramsPerLb

    @staticmethod
    def lbsToKilograms(lbs):
        """
        Converts lbs into kilograms.
        @param lbs: The lbs to convert to kilograms.
        @return Kilograms: Converted from lbs.
        """
        return lbs * kKilogramsPerLb