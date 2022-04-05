#! /usr/bin/env python

"""Script or module to do something"""

from argparse import ArgumentParser
import logging


def run():
    """The main entry point for this script when used as module"""

    # Do the fun stuff here


def configure_logging(verbose_level: int = 0):
    """Provide a generic logging configuration from the command line
    options when this script or module is run standalone"""

    level = [logging.WARNING, logging.INFO, logging.DEBUG][verbose_level]
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s]: %(message)s",
        level=level,
        datefmt="%y-%m-%d %H:%M:%S",
    )


def main():
    """Main entry point for this script or as a runnable module"""

    parser = ArgumentParser()
    parser.add_argument("--verbose", default=0, action="count", help="Verbose output")
    args = parser.parse_args()
    args.verbose = min(args.verbose, 2)
    configure_logging(args.verbose)

    run()


if __name__ == "__main__":
    main()
