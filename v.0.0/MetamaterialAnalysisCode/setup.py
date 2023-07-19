import os
from setuptools import setup

setup(
    name = 'Metamaterial_Analysis_Code',
    version = '1.1',
    author = 'Manuel Sánchez García',
    description = 'Code for the analysis of metamaterials',
    long_description = open(
        os.path.join(os.path.dirname(__file__), 'README.md')
    ).read,
    
)
