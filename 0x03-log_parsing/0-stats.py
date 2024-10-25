#!/usr/bin/python3
"""
log parsing
"""

import sys
import re

# Initializes a dictionary called log, which stores the file size and the counts of various HTTP status codes
def initialize_log():
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    
    log = {"file_size": 0, "code_list": {str(code): 0 for code in status_code}}
    
    return log

# Responsible for processing each log line. It will use a regular expression to match and extract the info from the input line.
# If a match is found, it will update the log dict with file size and increment the count for HTTP status codes.
def parse_line(line, regex, log):
    match = regex.fullmatch(line)
    
    if match:
        stat_code, file_size = match.group(1, 2)
        
        log["file_size"] += int(file_size)
        
        if stat_code.isdecimal():
            log["code_list"][stat_code] += 1

    return log

# Responsible for printing the total file size and the counts of HTTP status codes in a sorted order.
def print_codes(log):
    print("File size: {}".format(log["file_size"]))
    
    sorted_code_list = sorted(log["code_list"])
    
    for code in sorted_code_list:
        if log["code_list"][code]:
            print("{}: {}".format(code, log["code_list"][code]))

# Entry point where we compile the regular expression, call the initialize_log function, read lines from standard input,
# and process each line by calling parse_line function. Then count the number of lines processed,
# and print the line if it is a multiple of ten or get a keyboard interruption.
def main():
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)')
    
    log = initialize_log()
    
    line_count = 0
    
    for line in sys.stdin:
        line = line.strip()
        
        line_count += 1
        
        parsed_log = parse_line(line, regex, log)
        
        if line_count % 10 == 0:
            print_codes(parsed_log)
    
    print_codes(parsed_log)
    if the line_count % 10 == 0;
	print_codes(parsed_log)

if __name__== "__main__":
main ()
