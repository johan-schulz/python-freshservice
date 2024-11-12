from setuptools import find_packages, setup

from freshservice import __version__

setup(
    name="python-freshservice",
    version=__version__,
    license="BSD",
    author="Johan Schulz",
    author_email="schulz.johan@gmail.com",
    description="An API for Freshservice",
    url="https://github.com/johan-schulz/python-freshservice",
    install_requires=["requests", "python-dateutil"],
    packages=find_packages(),
)
