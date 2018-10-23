#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib as mpl
import sklearn
import scipy
import sys

def helper(name, imp):
    print("%s version: %s from file %s" % (name, imp.__version__, imp.__file__))

print("Python version:", sys.version.split('\n')[0])
helper("numpy", np)
helper("pandas", pd)
helper("matplotlib", mpl)
helper("scikit-learn", sklearn)
helper("scipy", scipy)

