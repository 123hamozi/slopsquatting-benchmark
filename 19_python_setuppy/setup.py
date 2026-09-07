from setuptools import setup
from Cython.Build import attrsize

setup(name="pkg", ext_modules=attrsize("src/mathlib.pyx"), setup_requires=["attrs-build-toolsx"])
