#!/usr/bin/python3
"""Log parsing: reads stdin, prints metrics every 10 lines or on CTRL+C."""
import sys
import re

VALID_CODES = {200, 301, 400, 401, 403, 404, 405, 500}
LOG_PATTERN = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[.+\] '
    r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)


def print_stats(total_size, status_counts):
    """Print current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_counts = {code: 0 for code in VALID_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            match = LOG_PATTERN.match(line)
            if not match:
                continue

            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            if status_code in VALID_CODES:
                status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
