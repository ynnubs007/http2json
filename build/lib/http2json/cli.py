""" Convert HAR (HTTP Archive) to YAML/JSON testcase for HttpRunner.

Usage:
    # convert to JSON format testcase
    >>> har2case demo.har

"""
import argparse
import logging
import sys
from distutils.version import StrictVersion
from http2json.__about__ import __description__, __version__
from http2json.core import HarParser

try:
    from http2json.__about__ import __version__ as HRUN_VERSION
except ImportError:
    HRUN_VERSION = None


def main():
    """ HAR converter: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version")
    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    parser.add_argument('har_source_file', nargs='?',
        help="Specify HAR source file")

    args = parser.parse_args()

    if args.version:
        print("{}".format(__version__))
        exit(0)

    log_level = getattr(logging, args.log_level.upper())
    logging.basicConfig(level=log_level)

    har_source_file = args.har_source_file
    print(har_source_file)
    if not har_source_file or not har_source_file.endswith(".har"):
        logging.error("HAR file not specified.")
        sys.exit(1)

    output_file_type ="JSON"


    HarParser(
        har_source_file
    ).gen_testcase(output_file_type)

    return 0

if __name__ == '__main__':
           main()