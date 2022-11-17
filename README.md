# Star Chart with Spherical Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)

A Python package to generate an astronomy star chart based on spherical projection with +90/-90° in the center (orignally based on [History Survival Guide Astrolabe work](https://github.com/cyschneck/History-Survival-Guide/tree/master/page_x_astrolabe)) with declination and right ascension and proper motion

__Star Chart in the Northern Hemisphere (centered on 90°)__
![north_star_chart_without_precession_without_labels+png](https://github.com/cyschneck/History-Survival-Guide/blob/master/page_x_astrolabe/generate_star_chart_outputs/star_chart_north_without_precession_without_labels.png) 
__Star Chart in the Southern Hemisphere (centered on -90°)__
![south_star_chart_without_precession_without_labels+png](https://github.com/cyschneck/History-Survival-Guide/blob/master/page_x_astrolabe/generate_star_chart_outputs/star_chart_south_without_precession_without_labels.png)

## Overview

 From perspective of an observer on the Earth's surface, the stars sit along the celestial sphere at a distance from the celestial equator (declination) and the position of the vernal equinox (right ascension). The stars will appear to rotate across the sky as a result of the Earth's rotation, but their position is fixed (if we ignore proper motion and precession for the moment).
 
 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Earth_within_celestial_sphere.gif" />
</p>

The first step to plot the celestial sphere onto a 2D plot is to map right ascension as hours along the plot (polar plot's theta value) and declination as the distance from the center of the circle (polar plot's radius value). However, attempting to map the right ascension and declination direclty will cause a distinct amount of distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

Spherical projection can overcome this difficulty by converting the position of the declination to:
```
new_declination = tan(45° + (original_declination / 2))
```
![morrisons_astrolabe](https://user-images.githubusercontent.com/22159116/202336728-dc290bfa-44f5-4947-9a08-93f70286436e.jpg)

## Dependencies

```
pip install -r requirements.txt
```

## Install

PyPi pip install at [pypi.org/project/star-chart-spherical-projection/](https://pypi.org/project/star-chart-spherical-projection/)

```
pip install star-chart-spherical-projection
```

## Documentation

## Examples

## Tests

## TODO:

Add README badges: tests

Update pypi setup.py development status

Update tarball download_url via VERSION tag
