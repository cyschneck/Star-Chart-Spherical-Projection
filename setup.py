# -*- coding: utf-8 -*-

# Python Package Setup
from setuptools import setup, find_namespace_packages

VERSION="1.5.0"
DESCRIPTION="A Python package to generate circular astronomy star charts (past, present, and future) with spherical projection to correct for distortions with more than a hundred named stars accurate over 400,000 years with proper motion and precession of the equinoxes"

with open("README.md", "r") as f:
	long_description_readme = f.read()

setup(
	name="star-chart-spherical-projection",
	version=VERSION,
	description=DESCRIPTION,
	long_description=long_description_readme,
	long_description_content_type='text/markdown',
	url="https://github.com/cyschneck/Star-Chart-Spherical-Projection",
	download_url="https://github.com/cyschneck/Star-Chart-Spherical-Projection/archive/refs/tags/v{0}.tar.gz".format(VERSION),
	author="Cora Schneck (cyschneck)",
	keywords=["astronomy", "python", "star charts", "precession", "proper motion", "spherical projection", "stereographic projection"],
	license="MIT",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Programming Language :: Python :: 3.12",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Physics",
		"Topic :: Scientific/Engineering :: Visualization",
		"Topic :: Scientific/Engineering :: Astronomy"
	],
	packages=find_namespace_packages(include=['star_chart_spherical_projection',
											'star_chart_spherical_projection.*']),
	include_package_data=True,
	install_requires=[
		"beautifulsoup4>=4.11.1",
		"matplotlib>=3.1.0",
		"numpy>=1.24.3",
		"pandas>=1.3.5",
		"pytest>=7.2.2"
	],
	python_requires='>=3.9'
)
