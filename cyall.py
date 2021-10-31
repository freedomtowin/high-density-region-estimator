from setuptools import setup, Extension, find_packages
from distutils.core import setup
from Cython.Build import cythonize


from codecs import open
import os
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'kernelml-README.md'), encoding='utf-8') as f:
    long_description = f.read()
    

# setup(
#     name = "Kernel Machine Learning",
#     ext_modules = cythonize('kernelml.pyx'),  # accepts a glob pattern
# )

def find_pyx(path='.'):
    pyx_files = []
    for root, dirs, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith('.pyx'):
                pyx_files.append(os.path.join(root, fname))
    return pyx_files

cythonize(find_pyx('kernelml'))
