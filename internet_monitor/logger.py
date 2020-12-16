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
