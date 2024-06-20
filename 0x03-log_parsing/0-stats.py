#!/usr/bin/python3
"""0. Log parsing"""
import sys
import re
import signal

pattern = re.compile(
    r'^(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] "GET /projects/260 '
    r'HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'
)
line_count = 0
total_size = 0
status_counts = {200: 0, 301: 0,
                 400: 0, 401: 0,
                 403: 0, 404: 0,
                 405: 0, 500: 0}


def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption (Ctrl + C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for log_line in sys.stdin:
        line_count += 1
        match = pattern.match(log_line.strip())
        if match:
            size = int(match.group('size'))
            status = int(match.group('status'))

            # Update total file size
            total_size += size

            # Update status code count if it's a valid code
            if status in status_counts:
                status_counts[status] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final statistics at the end
print_stats()
