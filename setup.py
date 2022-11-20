# -*- coding: utf-8 -*-

# Python Package Setup
from setuptools import setup, find_packages

VERSION="0.1.0"
DESCRIPTION="A Python package to generate star charts with spherical projection centered on +90 degrees for Northern Hemisphere and -90 degrees for Southern Hemisphere projections"

with open("README.md", "r") as f:
	long_description_readme = f.read()

setup(
	name="star-chart-spherical-projection",
	version=VERSION,
	description=DESCRIPTION,
	long_description=long_description_readme,
	long_description_content_type='text/markdown',
	url="https://github.com/cyschneck/Star-Chart-Spherical-Projection",
	download_url="https://github.com/cyschneck/Star-Chart-Spherical-Projection/archive/refs/tags/v0.1.0.tar.gz",
	author="cyschneck (C. Y. Schneck)",
	keywords=["astronomy", "python", "star charts", "precession", "proper motion", "spherical projection"],
	license="MIT",
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3.7",
		"Topic :: Scientific/Engineering :: Astronomy"
	],
	packages=find_packages(include=['star-chart-spherical-projection', 'star-chart-spherical-projection.*']),
	install_requires=[
		"configparser>=5.3.0",
		"matplotlib>=3.1.0",
		"numpy>=1.21.6",
		"pandas>=1.3.5"
	],
	python_requires='>=3.7'
)
