# internet-monitor

Monitor Internet connectivity and record time and duration of any downtime.

## Sample log output

```
12-12-2020 12:40 [DEBUG] Monitor started updating every 1 second(s)
13-12-2020 15:20 [WARNING] Internet connection unavailable
13-12-2020 15:20 [INFO] Internet Connection restored
13-12-2020 15:20 [INFO] Total downtime duration: 0:00:07
14-12-2020 11:34 [DEBUG] Monitor stopped
```

## Overview

Name: internet_monitor

Version: 1.0.2

Date: 15th December 2020

Last Update: 16th December 2020

Author: Lorenzo Corallo

## What is internet_monitor?

It is a Python module to monitor the uptime of the Internet connection - that is to say to monitor that an external IP address is always reachable.

## Why should I use internet_monitor?

If you have automated long-running processes/programs/activities on your computer that requires Internet connectivity, there is nothing worse than coming back the next hour/day/week/whenever to review the logs/progress and find out that the program(s) failed or data is missing because of lost Internet connectivity. What is worse - you may not know exactly when Internet connectivity was lost. Thus, will you need to rerun the entire program/process? Or just a part of it? and so on.

The Python module `internet_monitor` is a solution to this problem in that it monitors Internet connectivity in real-time, displaying on the console/terminal and recording to a log file: the start time, the end time and the duration of any Internet connectivity downtime. You may simply run this module in a console/terminal and leave it running for days/weeks on end.

## What does internet_monitor do?

Every X seconds (default polling frequency is 1 second), the program monitors whether the Internet connection is alive and an external IP address is reachable.

If the Internet is unreachable:

1. The first observed time of failure is logged.

2. Every one-minute interval of subsequent unavailability is logged. The one-minute logs can be useful as a proxy indicator of whether the computer lost power or just the Internet connection was unavailable.

3. When Internet connectivity is restored, the first observed time of restoration is logged.

4. Finally, the total time duration of the Internet unavailability is logged.

## Log File

- The log file is called `internet_monitor.log`.
- The log file is written to the current working folder.
- The log file is always appended to, never overwritten.
- The information written to the log file is also displayed on the console/terminal.
- The log levels are divided in:
  1. DEBUG ==> Used for logging the start/stop of the script
  2. INFO ==> Internet connection available and downtime infos
  3. WARNING ==> Internet connection unavailable
  4. ERROR or CRITICAL ==> Script error. Please if you recieve those, open a new Issue on [Github](https://github.com/lorenzocorallo/internet-monitor) then I can fix it. Thank you

## Prerequisites

You must have Python 3.6 or higher installed.

## Installation

```console
pip install internet_monitor
```

## QuickStart

```console
python -m internet_monitor
```

## How do I exit the program

To exit the program, simply press `Ctrl-C` inside the console/terminal. This will cause the program to exit gracefully.

## Usage

```console
usage: python -m internet_monitor [-h] [-f N]

Monitor the uptime of the Internet connection and record any downtime

optional arguments:
  -h, --help        show this help message and exit
  -f N, --freq N    specify polling frequency in seconds (default: 1)

```

## Acknowledgments

The `is_internet-alive` method was inspired by 7h3rAm's answer on [Stackoverflow](https://stackoverflow.com/questions/3764291/checking-network-connection)
This project was inspired by Martin O'Connor `monitor_internet_connection` project on [Github]("https://github.com/mfoc/monitor-internet-connection")

## Licence

This project is licensed under the MIT License - see the LICENSE.md file for details
