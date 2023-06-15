# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)
[![pytests](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml/badge.svg?branch=main)](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml)

A Python package to generate an astronomy star chart based on spherical projection with +90/-90° in the center based on a star's position (declination and right ascension): past, present, and future (proper motion and precession)

The first step to plot the celestial sphere onto a 2D plot is to map the star's right ascension as hours along the plot (matplotlib polar plot's theta value) and declination as the distance from the center of the circle (matplotlib polar plot's radius value). However, attempting to map the right ascension and declination directly will cause distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape due to this distortion. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

The sphere is projected from the South Pole (via [Sterographic projection](https://gisgeography.com/azimuthal-projection-orthographic-stereographic-gnomonic/)):
 <p align="center">
  <img src="https://gisgeography.com/wp-content/uploads/2016/12/Stereographic-Projection-768x421.png" />
</p>

_Example outputs:_

__Star Chart in the Northern Hemisphere (centered on 90°) without Precession__
![north_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png) 
![north_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_without_precession.png) 
![north_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_with_precession.png) 
![north_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_with_precession.png) 

__Star Chart in the Southern Hemisphere (centered on -90°) without Precession__
![south_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_without_precession.png) 
![south_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_without_precession.png) 
![south_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_with_precession.png) 
![south_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_with_precession.png) 

## Overview

From the perspective of an observer on the Earth's surface, the stars appear to sit along the surface of the celestial sphere--an imaginary sphere of arbitrary radius with the Earth at its center. All objects in the sky will appear projected on the celestial sphere regardless of their true distance from Earth. Each star's position is given by two values. Declination is the angular distance from the celestial equator and right ascension is the distance from the position of the vernal equinox. During the course of a full 24 hour day, stars will appear to rotate across the sky as a result of the Earth's rotation, but their position is fixed. A star’s actual position does change over time as the combined result of the star’s small movement (proper motion) as well as the changing rotational axis of the Earth (precession).
 
 <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Earth_within_celestial_sphere.gif" />
</p>

Spherical projection can overcome angular distortion by converting the position of the declination to:
```
# Projected from South Pole (Northern Hemisphere)
north_hemisphere_declination = tan(45° + (original_declination / 2))

# Projected from North Pole (Southern Hemisphere)
south_hemisphere_declination = tan(45° - (original_declination / 2))
```
Where in the Northern Hemsiphere, projections are formed from the South Pole: 
![morrisons_astrolabe](https://user-images.githubusercontent.com/22159116/202336728-dc290bfa-44f5-4947-9a08-93f70286436e.jpg)

## Documentation

**finalPositionOfStars()**

Returns a dictionary for the final positions of the stars in the format: {'Star Name': {"Declination" : Declination (int), "RA": RA (str)}
```
finalPositionOfStars(yearSince2000=0, 
			userListOfStars=[],
			isPrecessionIncluded=True,
			declination_min=None,
			declination_max=None)
```
- *[OPTIONAL]* userListOfStar: (list) a list of star names to include, by default = [] includes all stars (in star_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* declination_min: (int/float) set minimum declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* declination_max: (int/float) set maximum declination value, defaults to 90° in Northern hemisphere and -90° in Southern hemisphere

<details closed>
<summary>Stars that will be included by default when userListOfStars = [] (Click to view all)</summary>
<br>
 ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 
'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 
'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 
'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 
'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 
'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 
'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 
'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 
'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 
'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 
'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 
'Zubeneschamali']
</details>

**plotStereographicProjection()**

Plot stars on a Stereographic Polar Plot
```
plotStereographicProjection(northOrSouth=None, 
				userListOfStars=[], 
				declination_min=None,
				yearSince2000=0,
				displayStarNamesLabels=True,
				displayDeclinationNumbers=True,
				incrementBy=10,
				isPrecessionIncluded=True,
				maxMagnitudeFilter=None,
				showPlot=True,
				fig_plot_title=None,
				fig_plot_color="C0",
				figsize_n=12,
				figsize_dpi=100,
				save_plot_name=None)
```
- **[REQUIRED]** northOrSouth: (string) map for either the "North" or "South" hemisphere
- *[OPTIONAL]* userListOfStars: (list) a list of star names to include, by default = [] includes all stars (in star_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* declination_min: (int/float) outer declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* displayStarNamesLabels: (boolean) display the star name labels, defaults to True
- *[OPTIONAL]* displayDeclinationNumbers: (boolean) display declination values, defaults to True
- *[OPTIONAL]* incrementBy: (int) increment values for declination (either 1, 5, 10), defaults to 10
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* maxMagnitudeFilter: (int/float) filter existing stars by magnitude by setting the max magnitude for the chart to include, defaults to None (shows all stars)
- *[OPTIONAL]* showPlot: (boolean) show plot (triggers plt.show()) when finished running, defaults to True
- *[OPTIONAL]* fig_plot_title: (string) figure title, defaults to "<North/South>ern Hemisphere [<YEAR NUMBERS> Years Since 2000 (YYYY)]: +/-90° to <DECLINATION MIN>°"
- *[OPTIONAL]* fig_plot_color: (string) scatter plot star color, defaults to C0
- *[OPTIONAL]* figsize_n: (int/float) figure size, default to 12
- *[OPTIONAL]* figsize_dpi: (int/float) figure DPI, default to 100
- *[OPTIONAL]* save_plot_name: (string) save plot with a string name, defaults to not saving

<details closed>
<summary>Stars that will be included by default when userListOfStars = [] (Click to view all)</summary>
<br>
 ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 
'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 
'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 
'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 
'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 
'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 
'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 
'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 
'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 
'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 
'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 
'Zubeneschamali']
</details>

## Dependencies

Python 3.7+
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
import star_chart_spherical_projection as scsp

star_final_pos_dict = scsp.finalPositionOfStars(userListOfStars=["Vega", "Polaris", "Betelgeuse"], yearSince2000=11500)
```
Returns a dictionary: `{'Betelgeuse': {'Declination': -36.342836095268325, 'RA': '16.34.28'}, 'Polaris': {'Declination': 45.08038305067079, 'RA': '17.25.11'}, 'Vega': {'Declination': 83.6899118156341, 'RA': '05.38.21'}}`

```python
import star_chart_spherical_projection as scsp

scsp.plotStereographicProjection(northOrSouth="North")
```
## Bibliography

Star position (right ascension and declination) as well as the angle and speed of proper motion taken from [in-the-sky.org](in-the-sky.org)

Precession model: [Vondrák, J., et al. “New Precession Expressions, Valid for Long Time Intervals.” Astronomy &amp; Astrophysics, vol. 534, 2011, https://doi.org/10.1051/0004-6361/201117274.](https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf)

Precession code adapted to Python3 from [github.com/dreamalligator/vondrak](github.com/dreamalligator/vondrak)

## TODO:

Add README badges: pypi tests
