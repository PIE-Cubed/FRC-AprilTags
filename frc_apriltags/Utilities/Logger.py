# Created by Alex Pereira

# Import Libraries
import logging

# Starts a logger
logging.basicConfig(filename = "./DetectionLog.log", format="%(levelname)s:%(message)s", encoding = "utf-8", level = logging.DEBUG)

# Start of the Logging class
class Logger:
    """
    Use this class to log an debug info you generate.
    """
    @staticmethod
    def logDebug(debug: str, logStatus: bool = True):
        """
        Logs a debug statement.
        @param debugMessage: The debug message to show
        @param logStatus: Is loging enabled
        """
        if (logStatus == True):
            logging.debug(debug)

    @staticmethod
    def logInfo(info: str, logStatus: bool = True):
        """
        Logs information.
        @param infoMessage: The info message to show
        @param logStatus: Is loging enabled
        """
        if (logStatus == True):
            logging.info(info)

    @staticmethod
    def logWarning(warning: str, logStatus: bool = True):
        """
        Logs a warning.
        @param warning: The warning message to show
        @param logStatus: Is loging enabled
        """
        if (logStatus == True):
            logging.warning(warning)

    @staticmethod
    def logError(error: str, logStatus: bool = True):
        """
        Logs an error.
        @param error: The error message to show
        @param logStatus: Is loging enabled
        """
        if (logStatus == True):
            logging.error(error)