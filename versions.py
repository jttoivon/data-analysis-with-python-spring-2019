#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib as mpl
import sklearn

def helper(name, imp):
    print("%s version: %s from file %s" % (name, imp.__version__, imp.__file__))

helper("numpy", np)
helper("pandas", pd)
helper("matplotlib", mpl)
helper("scikit-learn", sklearn)

#print("numpy version:", np.__version__, "from file", np.__file__)
#print("pandas version:", pd.__version__)
#print("matplotlib version:", mpl.__version__)
#print("scikit-learn version:", sklearn.__version__)
