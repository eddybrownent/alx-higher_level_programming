#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics
"""
import sys


# defining valid HTTP status codes
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_metrics(total_file_size, status_code_counts):
    """
    prints the metrics
    """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        print("{}: {}".format(status_code, count))


if __name__ == "__main__":
    total_file_size = 0
    status_code_counts = {}  # Dictionary to store status code counts
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Split the line into words
            words = line.split()

            try:
                # get the file size from the last word
                file_size = int(words[-1])
                total_file_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                # get the status code from the second-to-last word
                status_code = words[-2]
                if status_code in valid_status_codes:
                    # Update the count for the status code
                    status_code_counts.setdefault(status_code, 0)
                    status_code_counts[status_code] += 1
            except IndexError:
                pass

            # prints  metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        # Handles the keyboard interruption
        print_metrics(total_file_size, status_code_counts)

    # prints the final metrics
    print_metrics(total_file_size, status_code_counts)
