"""
This is sample setup.py

"""
from pathlib import Path
import setuptools

setuptools.setup(
    name="python-basic",
    version='1.0',
    long_description=Path("README.md").read_text(encoding='utf-8'),
    packages=setuptools.find_packages(exclude=["tests", "data","python-utils","secrets"])
)
