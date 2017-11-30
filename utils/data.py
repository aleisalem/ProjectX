#!/usr/bin/python

from ProjectX.utils.graphics import *
from ProjectX.utils.data import *

import numpy
import os

def loadNumericalFeatures(featuresFile, delimiter=","):
    """Loads numerical features from a file and returns a list"""
    try:
        if not os.path.exists(featuresFile):
            prettyPrint("Unable to find the features file \"%s\"" % featuresFile, "warning")
            return []
        content = open(featuresFile).read()
        features = [float(f) for f in content[1:-1].split(delimiter)]

    except Exception as e:
        prettyPrintError(e)
        return []

    return features
