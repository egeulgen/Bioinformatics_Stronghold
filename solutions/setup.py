from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("edit_distance_kband.pyx"),
    include_dirs=[numpy.get_include()]
)
