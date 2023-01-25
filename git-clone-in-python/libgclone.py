import argparse
import collections
import configparser
import hashlib
from math import ceil
import os
import re
import sys
import zlib


argparser = argparse.ArgumentParser(description="Clone of GIT(VCS) in python")
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True 
