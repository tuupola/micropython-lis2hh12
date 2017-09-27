import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-lis2hh12",
    py_modules=["lis2hh12"],
    version="0.1.0",
    description="MicroPython I2C driver for LIS2HH12 3-axis accelerometer",
    long_description="The LIS2HH12 is an ultra-low-power high-performance three-axis linear accelerometer belonging to the “pico” family. It has full scales of ±2g/±4g/±8g and is capable of measuring accelerations with output data rates from 10 Hz to 800 Hz.",
    keywords="accelerometer micropython i2c",
    url="https://github.com/tuupola/micropython-lis2hh12",
    author="Mika Tuupola",
    author_email="tuupola@appelsiini.net",
    maintainer="Mika Tuupola",
    maintainer_email="tuupola@appelsiini.net",
    license="MIT",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)