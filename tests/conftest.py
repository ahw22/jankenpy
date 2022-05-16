import os
import sys
from os.path import dirname as d
from os.path import join as j

sys.path.append(os.path.abspath(j(d(d(__file__)), "src")))
