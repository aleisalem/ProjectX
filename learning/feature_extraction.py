#!/usr/bin/python

from ProjectX.utils.data import *
from ProjectX.utils.graphics import *
from ProjectX.utils.misc import *

import sklearn, numpy

import os

def extractCountFeatures(allSequences):
    """
    Extracts simple numerical features depicting the occurrence counts for every unique (trigger, payload) tuple in a sequence
    :param allSequences: The sequences of all apps
    :type allSequences: list
    :return: A list of lists depicting the feature vectors extracted from every sequence
    :return: An ordered list of (trigger, payload) tuples extracted from sequences i.e. features
    """
    try:
        allTuples = []
        featureVectors = []
        # 1. Retrieve all possible (trigger, payload) tuples to estimate vector size
        prettyPrint("Retrieving (trigger, payload) tuples from sequences")
        for sequence in allSequences:
            for t in sequence:
                if not t in allTuples:
                    prettyPrint("Adding the tuple %s to list" % str(t))
                    allTuples.append(t)
        prettyPrint("Successfully retrieved %s tuples from %s sequences" % (len(allTuples), len(allSequences)))
        # 2. Extract counts of tuples from sequences
        for sequence in allSequences:
            vector = []
            for feature in allTuples:
                vector.append(float(sequence.count(feature)))
            featureVectors.append(vector)

    except Exception as e:
        prettyPrintError(e)
        return [], []

    return featureVectors, allTuples

