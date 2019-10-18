__version__ = "0.0.2"

# __version__ has to be define in the first line

"""
pygeoda: A Python Library for Spatial Data Analysis based on libgeoda
================================================
Documentation
-------------
pygeoda documentation is available in two forms: python docstrings and an html \
        webpage at http://pygeoda.org/
Available sub-packages
----------------------
weights
    Tools for creating and manipulating weights
"""
import os

# exposed under pygeoda.weights.xxx
from . import weights

# exposed under pygeoda.xxx
from .clustering import *
from .sa import *
from .geopds import *
from .utils import *
from .gda import *
