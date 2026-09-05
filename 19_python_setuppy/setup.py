from setuptools import setup
from Cython.Build import cythonize

setup(name="pkg", ext_modules=cythonize("src/mathlib.pyx"), setup_requires=["cython-build-tools"])
