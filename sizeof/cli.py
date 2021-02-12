import os
import sys
import argparse


def run_cli():
    # create the parser
    parser = argparse.ArgumentParser(
        description="Count a directory's files and total size."
    )

    # add the required path positional argument
    parser.add_argument(
        "Path",
        metavar="path",
        type=str,
        help="the root directory path whose contents will be counted",
    )

    # add the optional logfile argument
    parser.add_argument(
        "-n",
        "--nolog",
        action="store_true",
        help="do not create a logfile .txt of the results",
    )

    # add the optional by subdir argument
    parser.add_argument(
        "-b",
        "--bysubdir",
        action="store_true",
        help="tally the counts by subdirectory of the root directory",
    )

    # parse the arguments
    args = parser.parse_args()

    root_dir = args.Path

    # check that the specified path exists
    if not os.path.isdir(root_dir):
        print("The specified path does not exist; cannot continue.")
        sys.exit()

    # set log file preference
    create_log = False if args.nolog else True

    # set by subdir preference
    by_subdir = True if args.bysubdir else False

    # send config to the program
    config = {"root_dir": root_dir, "create_log": create_log, "by_subdir": by_subdir}
    return config
