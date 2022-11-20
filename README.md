# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)


A Python package to generate an astronomy star chart based on spherical projection with +90/-90° in the center (orignally based on [this Astrolabe work](https://github.com/cyschneck/History-Survival-Guide/tree/master/page_x_astrolabe)) based on a star's position (declination and right ascension): past, present, and future (proper motion and *precession)

The first step to plot the celestial sphere onto a 2D plot is to map the star's right ascension as hours along the plot (polar plot's theta value) and declination as the distance from the center of the circle (polar plot's radius value). However, attempting to map the right ascension and declination directly will cause a distinct amount of distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

The sphere is projected from the South Pole (via Sterographic projection):
![sterographic_projection](https://courses.washington.edu/gis250/lessons/projection/images_av3/orthographic2.gif)

_Example outputs:_

__Star Chart in the Northern Hemisphere (centered on 90°)__
![north_star_chart_without_precession_without_labels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_testing.png) 
__Star Chart in the Southern Hemisphere (centered on -90°)__
![south_star_chart_without_precession_without_labels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_testing.png)
_*precession to be added_

## Overview

From the perspective of an observer on the Earth's surface, the stars appear to sit along the surface of the celestial sphere--an imaginary sphere of arbitery radius with the Earth at its center. All objects in the sky will appear projected on the celestial sphere regardless of their true distance from Earth. Each star's position is given by two values. Declination is the angular distance from the celestial equator and right ascension is the distance from the position of the vernal equinox. The stars will appear to rotate across the sky as a result of the Earth's rotation, but their position is fixed. A star’s actual position does change over time as the combined result of the star’s small movement (proper motion) as well as the changing rotational axis of the Earth (precession).
 
 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Earth_within_celestial_sphere.gif" />
</p>

Spherical projection can overcome this difficulty by converting the position of the declination to:
```
# Projected from South Pole (Northern Hemisphere)
north_hemisphere_declination = tan(45° + (original_declination / 2))

# Projected from North Pole (Southern Hemisphere)
south_hemisphere_declination = tan(45° - (original_declination / 2))
```
Where in the Northern Hemsiphere, projections are formed from the South Pole: 
![morrisons_astrolabe](https://user-images.githubusercontent.com/22159116/202336728-dc290bfa-44f5-4947-9a08-93f70286436e.jpg)

## Dependencies

Python 3.7
```
pip3 install -r requirements.txt
```

## Install

PyPi pip install at [pypi.org/project/star-chart-spherical-projection/](https://pypi.org/project/star-chart-spherical-projection/)

```
pip install star-chart-spherical-projection
```

## Documentation

## Examples

```
import star_chart_spherical_projection
star_chart_spherical_projection.plotStarChart(northOrSouth="North", star_plot_color="red")
```
## Tests

## TODO:

Add README badges: tests

TODO: check that user list has stars that are found in current list

Update pypi setup.py development status

Update tarball download_url via VERSION tag

Move constants to __init__.py instead of config.py
