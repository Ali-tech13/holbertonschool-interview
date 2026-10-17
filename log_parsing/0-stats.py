#!/usr/bin/python3
"""Read logs from stdin and print cumulative metrics."""

import sys


def print_stats(total_size, counts):
    """Print total size and nonzero status counts."""
    print("File size: {}".format(total_size))
    for code in sorted(counts):
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def main():
    """Process log lines and report cumulative statistics."""
    total_size = 0
    line_count = 0
    counts = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass

                if parts[-2] in counts:
                    counts[parts[-2]] += 1

            if line_count % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
