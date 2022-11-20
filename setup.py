# -*- coding: utf-8 -*-

# Python Package Setup
from setuptools import setup, find_namespace_packages

VERSION="0.1.7"
DESCRIPTION="A Python package to generate an astronomy star chart based on spherical projection that corrects for distortions to generate star charts with spherical projection"

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
	author="cyschneck (C. Y. Schneck)",
	keywords=["astronomy", "python", "star charts", "precession", "proper motion", "spherical projection"],
	license="MIT",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3.7",
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
		"configparser>=5.3.0",
		"matplotlib>=3.1.0",
		"numpy>=1.21.6",
		"pandas>=1.3.5"
	],
	python_requires='>=3.7'
)
