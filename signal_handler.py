import datetime
import sys
from logger import logger

def signal_handler(signal_received, frame):
    """ Capture Ctrl-C (or SIGINT) and exit the program gracefully. 

    Input Params:
        signal_received (integer) is the signal number captured and received.
        frame (frame object) is the current stack frame.

    Returns:
        This method exits the program, thus nothing is returned.
    """

    # Display exit message to console and record in log file.
    logger.debug(f"Monitor stopped")
    sys.exit()