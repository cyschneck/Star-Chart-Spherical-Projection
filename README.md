# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)

A Python package to generate an astronomy star chart based on spherical projection with +90/-90° in the center (orignally based on [this Astrolabe work](https://github.com/cyschneck/History-Survival-Guide/tree/master/page_x_astrolabe)) based on a star's position (declination and right ascension): past, present, and future (proper motion and *precession)

The first step to plot the celestial sphere onto a 2D plot is to map the star's right ascension as hours along the plot (polar plot's theta value) and declination as the distance from the center of the circle (polar plot's radius value). However, attempting to map the right ascension and declination directly will cause a distinct amount of distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

The sphere is projected from the South Pole (via [Sterographic projection](https://gisgeography.com/azimuthal-projection-orthographic-stereographic-gnomonic/)):
 <p align="center">
  <img src="https://gisgeography.com/wp-content/uploads/2016/12/Stereographic-Projection-768x421.png" />
</p>

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

## Documentation

```
plotStereographicProjection(userListOfStars=[],  
		northOrSouth=None, 
		declination_min=None,
		yearSince2000=0,
		displayStarNamesLabels=True,
		displayDeclinationNumbers=True,
		incrementBy=10,
		fig_plot_title=None,
		fig_plot_color="C0",
		figsize_n=12,
		figsize_dpi=100,
		save_plot_name=None
```

- **[REQUIRED]** northOrSouth: (string) map for either the "North" or "South" hemisphere
- *[OPTIONAL]* userListOfStar: (list) a list of star names to include, by default = [] includes all stars (in star_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* declination_min: (int) outer declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* yearSince2000: (float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession*, defaults = 0 years
- *[OPTIONAL]* displayStarNamesLabels: (boolean) display the star name labels, defaults to True
- *[OPTIONAL]* displayDeclinationNumbers: (boolean) display declination values, defaults to True
- *[OPTIONAL]* incrementBy: (int) increment values for declination (either 1, 5, 10), defaults to 10
- *[OPTIONAL]* fig_plot_title: (string) figure title, defaults to "<North/South>ern Hemisphere [<YEAR NUMBERS> Years Since 2000 (YYYY)]: +/-90° to <DECLINATION MIN>°"
- *[OPTIONAL]* fig_plot_color: (string) scatter plot star color, defaults to C0
- *[OPTIONAL]* figsize_n: (int) figure size, default to 12
- *[OPTIONAL]* figsize_dpi: (int) figure DPI, default to 100
- *[OPTIONAL]* save_plot_name: (string) save plot with a string name, defaults to not saving

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

## Examples

```python
import star_chart_spherical_projection

star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North")
```
## Tests

## TODO:

Add README badges: tests

TODO: check that user list has stars that are found in current list
