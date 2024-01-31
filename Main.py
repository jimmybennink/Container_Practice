# File to test contents of the container environment

# This assumes VSCode is installed with the dev containers extension installed:
#   - go to left sidebar in VSCode
#   - click on "extensions" and search "Dev Containers"
#   - install

# Import modules used for the AAM simulation
import itertools as it  # Readable nested for loops
from pathlib import Path  # Filepaths
import typing  # Argument / output type checking
import numpy as np  # N-dim arrays + math
from scipy.spatial.transform import Rotation as rot  # Rotation mathematics
import scipy.linalg as spla  # Complex linear algebra
import scipy.interpolate as spip  # Linear interpolation
from time import time
import matplotlib.pyplot as plt  # Plots
import matplotlib.figure as figure  # Figure documentation
import airsim
from pandas import read_csv
import socket  # Communicating with Matlab / Simulink
import struct  # Packing / unpacking datalink messages
import matlab.engine  # Interfacing with Matlab / Simulink
from threading import (
    Thread,
    Event,
    Lock,
)  # Threading for interfacing with Matlab / Simulink
import keyboard  # Halting
