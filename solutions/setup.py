from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("edit_distance_kband.pyx")
)