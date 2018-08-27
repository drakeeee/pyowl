from setuptools import find_packages
from setuptools import setup

setup(name='pyowl',
      version='0.1',
      description='pyowl: Ordered Weighted L1 Regularization in Python',
      long_description=open('README.md').read(),
      url='https://github.com/vene/pyowl',
      packages=find_packages(),
      install_requires=[
            "numpy==1.15.1",
            "scikit-learn==0.19.2",
            "scipy==1.1.0"
      ])
