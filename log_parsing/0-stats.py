#!/usr/bin/python3
"""Read log lines from stdin and print cumulative statistics."""

import re
import sys


def print_stats(total_size, counts):
    """Print total file size and status counts in ascending order."""
    print("File size: {}".format(total_size))
    for code in sorted(counts):
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def main():
    """Process input and report statistics every ten lines."""
    total_size = 0
    line_count = 0
    counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    pattern = re.compile(
        r'^(\d{1,3}(?:\.\d{1,3}){3}) - \[([^\]\r\n]+)\] '
        r'"GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.rstrip('\n'))

            if match:
                ip_parts = match.group(1).split('.')
                if all(0 <= int(part) <= 255 for part in ip_parts):
                    total_size += int(match.group(4))
                    try:
                        code = int(match.group(3))
                    except ValueError:
                        code = None
                    if code in counts:
                        counts[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
