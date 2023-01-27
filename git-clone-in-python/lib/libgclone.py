import argparse
import collections
import configparser
import hashlib
from math import ceil
import os
import re
import sys
import zlib
from gitrepo import *
from commands import *


# args parsing

argparser = argparse.ArgumentParser(description="Clone of GIT(VCS) in python")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Specify the path to create repository")


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = argparser.parse_args(argv)

    if args.command in SUBCOMMANDS.keys():
        SUBCOMMANDS.get(args.command)(args)
