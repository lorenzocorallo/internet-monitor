import datetime

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


