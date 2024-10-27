#!/usr/bin/python3

""" Script that reads stdin line by line and computes metrics """

import sys
import re

def print_stats(status_counts, total_size):
    """Prints information about the file size and status counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

# Initialize the status code dictionary and counters
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

# Regex to match the expected log format
log_pattern = re.compile(r'^(?P<ip>[\d\.]+) - \[(?P<date>[^\]]+)\] "(?P<request>GET [^"]+)" (?P<status_code>\d{3}) (?P<file_size>\d+)$')

try:
    for line in sys.stdin:
        line_count += 1

        match = log_pattern.match(line)
        if match:
            status_code = match.group('status_code')
            file_size = int(match.group('file_size'))

            # Update total file size
            total_size += file_size
            
            # Update status code count if it's one of the specified codes
            if status_code in status_counts:
                status_counts[status_code] += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats(status_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_size)
    sys.exit()

# Final output after the end of input
print_stats(status_counts, total_size)

