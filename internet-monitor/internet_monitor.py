"""
Name:           internet_monitor.py
Author:         Lorenzo Corallo
Description:    Monitor Internet connectivity and record time and duration of any downtime.

Date:           15th October 2020
Version:        1.0.0


How to run:		To run this program from the Console/Terminal, type:
					python internet_monitor.py

This program checks every X (1) seconds whether the Internet connection
is alive and an external IP address is reachable.
If the Internet connection is unavailable:
    1. The first observed time of failure is logged. 
    2. Every 1-minute interval of subsequent downtime is logged.
    3. When Internet connectivity is restored, the first observed time of 
       restoration is logged. 
    4. Finally, the total duration of the downtime is logged.

Features:
    - Check internet connection availability with different polling frequency
    - Monitor downtime duration
    - Log downtime in file .log always accessible with detailed and dated informations
    - Capture Ctrl-C (and SIGINT) and exit the program gracefully
    - Command line option to display a help message.
    - Command line option to specify the polling frequency in seconds. 
    There are nine options available [1, 2, 3, 4, 5, 10, 20, 30, 60].

"""

import signal
import datetime
import time
import sys
import argparse
import datetime

import datetime
import sys
import socket

import logging

# Get logger instance by __name__ (__main__ or filename)
logger = logging.getLogger(__name__)

# Setting logging format into a variable
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%d-%m-%Y %H:%M")

# Create handler for logging (filename, level, debug)
file_handler  = logging.FileHandler(f"{__name__}.log")

# Set formatter
file_handler.setFormatter(formatter)

# Adding handler to logger instance
logger.addHandler(file_handler)

# Set logging Level
logger.setLevel(logging.DEBUG)

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

def is_internet_alive(host="8.8.8.8", port=53, timeout=3):
    """Check if Internet Connection is alive and external IP address is reachable.

    Input Parameters:
        host: (string) 8.8.8.8 (google-public-dns-a.google.com)
        port: (integer) (53/tcp DNS Service).
        timeout: (float) timeout in seconds.

    Returns:
        True (Boolean) if external IP address is reachable.
        False (Boolean) if external IP address is unreachable.
    """

    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except OSError:
        # print(error.strerror)
        print("Disconnected")
        return False
    else:
        s.close()
        print("Connected")
        return True

def calc_time_diff(start, end):
    """ Calculate duration between two times and return as HH:MM:SS

    Input Params:
        start and end times
        both datetime objects created from datetime.datetime.now()

    Returns:
        The duration (string) in the form HH:MM:SS
    """

    time_difference = end - start
    secs = str(time_difference.total_seconds())
    return str(datetime.timedelta(seconds=float(secs))).split(".")[0]


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""

    parser = argparse.ArgumentParser(
        description="Monitor the uptime of the Internet connection and record any downtime",
        prog='python -m internet_monitor')

    parser.add_argument("-f", "--freq", dest="polling_freq", metavar="N",
                   default=1,
                   type=int,
                   choices=[1, 2, 3, 4, 5, 10, 20, 30, 60],
                   help="Specify the frequency to check connection status (in seconds)")

    return parser.parse_args(args)


def monitor(polling_freq = 1):
    """ Check internet connection until CTRL-C."""

    # Capture the Ctrl-C (or SIGINT) signal to permit the program to exit gracefully.
    signal.signal(signal.SIGINT, signal_handler)

    # Write to log file when Internet monitoring commences.
    # msg = "Monitoring Internet Connection commencing: " + now.strftime("%Y-%m-%d %H:%M:%S")
    msg = "Monitor started updating every " + str(polling_freq) + " second(s)"
    print(msg)
    logger.debug(msg)

    while True:
        # When run on cmd line, exit program via Ctrl-C.
        if is_internet_alive():
            time.sleep(polling_freq)
        else:
            # Record observed time when internet connectivity fails.
            fail_time = datetime.datetime.now()
            msg = "Internet connection unavailable"
            print(msg)
            logger.warning(msg)
            # Check every 1 second to see if internet connectivity restored.

            while not is_internet_alive():
                time.sleep(1)

            # Record observed time when internet connectivity restored.
            restore_time = datetime.datetime.now()
            restore_msg = "Internet Connection restored"

            # Calculate the total duration of the downtime
            downtime_duration = calc_time_diff(fail_time, restore_time)
            duration_msg = "Total downtime duration: " + downtime_duration

            # Display restoration message to console and record in log file.
            print(restore_msg)
            print(duration_msg)
            logger.info(restore_msg)
            logger.info(duration_msg)

args = parse_args()
print(args)
monitor(args.polling_freq)