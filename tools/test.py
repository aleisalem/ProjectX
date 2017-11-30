#!/usr/bin/python

from ProjectX.data_generation.reconstruction.Numerical import *
from ProjectX.data_inference.visualization.visualizeData import *
from ProjectX.utils.graphics import *
from ProjectX.utils.data import *

import pickledb

import glob, sys, time, os, argparse, hashlib

def defineArguments():
    parser = argparse.ArgumentParser(prog="test.py", description="A tool to ...")
    parser.add_argument("-a", "--arga", help="...", required=True)
    parser.add_argument("-b", "--argb", help="...", required=True, choices=["foo", "bar"])

    return parser

def main():
    try:
        argumentParser = defineArguments()
        arguments = argumentParser.parse_args()
        prettyPrint("Welcome to the the \"X\" tool")

    
    except Exception as e:
        prettyPrintError(e)
        return False

    return True

if __name__ == "__main__":
    main()
