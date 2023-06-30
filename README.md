# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)
[![pytests](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml/badge.svg?branch=main)](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml)

A Python package to generate an astronomy star chart based on spherical projection with +90/-90° in the center based on a star's position (declination and right ascension): past, present, and future (proper motion and precession)

* **Plot Stars on a Polar Chart**
	* plotStereographicProjection()
* **Return Final Position of Stars**
	* finalPositionOfStars()
* **Add a New Star**
	* newStar()

The first step to plot the celestial sphere onto a 2D plot is to map the star's right ascension as hours along the plot (matplotlib polar plot's theta value) and declination as the distance from the center of the circle (matplotlib polar plot's radius value). However, attempting to map the right ascension and declination directly will cause distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape due to this distortion. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

The sphere is projected from the South Pole (via [Sterographic projection](https://gisgeography.com/azimuthal-projection-orthographic-stereographic-gnomonic/)):
 <p align="center">
  <img src="https://gisgeography.com/wp-content/uploads/2016/12/Stereographic-Projection-768x421.png" />
</p>


## Quickstart: Star-Chart-Spherical-Projection
Plot stars in the Southern Hemisphere for the year 2023 (without stars labels)
```python
import star_chart_spherical_projection as scsp

scsp.plotStereographicProjection(northOrSouth="South",
				displayStarNamesLabels=False,
				yearSince2000=23)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/quickstart_south_2023.png) 

Plot some built-in stars as well as two new user defined stars in the Northern Hemisphere for the year 1961 (2000-39) (with stars labels and in the color red). This uses both methods to define the proper motion for new stars: with a given proper motion and angle and with the proper motion speed in the declination and right ascension
```python
import star_chart_spherical_projection as scsp

exalibur_star = scsp.newStar(starName="Exalibur",
			ra="14.04.23",
			dec=64.22,
			properMotionSpeed=12.3,
			properMotionAngle=83,
			magnitudeVisual=1.2)
karaboudjan_star = scsp.newStar(starName="Karaboudjan",
			ra="3.14.15",
			dec=10.13,
			properMotionSpeedRA=57.6,
			properMotionSpeedDec=60.1,
			magnitudeVisual=0.3)
scsp.plotStereographicProjection(northOrSouth="North",
			builtInStars=["Vega", "Arcturus", "Altair"],
			userDefinedStars=[exalibur_star, karaboudjan_star],
			displayStarNamesLabels=True,
			fig_plot_color="red",
			yearSince2000=-39)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/quickstart_newstar_example.png) 


Return the final position of a Vega (can be a single star or a list of stars) after 11,500 years when Vega is the new North Pole Star (star closest to +90°)
```python
import star_chart_spherical_projection as scsp

star_final_pos_dict = scsp.finalPositionOfStars(builtInStars=["Vega"], yearSince2000=11500)
```
Returns a dictionary with a star and its declination and right ascension: `{'Vega': {'Declination': 83.6899118156341, 'RA': '05.38.21'}}`

## Install

PyPi pip install at [pypi.org/project/star-chart-spherical-projection/](https://pypi.org/project/star-chart-spherical-projection/)

```
pip install star-chart-spherical-projection
```

## Requirements

Python 3.7+
```
pip install -r requirements.txt
```
Requirements will also be downloaded as part of the pip download

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

## Add a New Star

### newStar Object

The star chart package comes with over a hundred of brightest stars as part of a built-in library. However, a new star can be easily added for plotting or calculations by creating a newStar object. The newStar object will require a few important features that plotStereographicProjection() and finalPositionOfStars() can now accept as an additional argument.

This allows for the creation of a new star in two ways:

**1. With a Proper Motion Speed and a Proper Motion Angle**

As seen in [in-the-sky.org for Pollux](https://in-the-sky.org/data/object.php?id=TYC1920-2194-1)
```
star_chart_spherical_projection.newStar(starName=None,
				ra=None,
				dec=None,
				properMotionSpeed=None,
				properMotionAngle=None,
				magnitudeVisual=None)
```
* **[REQUIRED]** starName (string): A star name to be displayed as a label
* **[REQUIRED]** ra (string): Right Ascension as a string with three parts 'HH.MM.SS' (Hours, Minutes, Seconds)
* **[REQUIRED]** dec (int/float): Declination as a postive or negative value
* **[REQUIRED]** properMotionSpeed (int/float): Proper motion speed as a single value (in mas/year)
* **[REQUIRED]** properMotionAngle (int/float): Proper motion positive angle (between 0° and 360°)
* **[REQUIRED]** magnitudeVisual (int/float): Absolute Visual Magnitude

**With the Proper Motion sppeed along the Right Ascension and Declination**

As seen in [wikipeida.og for Pollux](https://en.wikipedia.org/wiki/Pollux_(star))

```
star_chart_spherical_projection.newStar(starName=None,
					ra=None,
					dec=None,
					properMotionSpeedRA=None,
					properMotionSpeedDec=None,
					magnitudeVisual=None)
```
* **[REQUIRED]** starName (string): A star name to be displayed as a label
* **[REQUIRED]** ra (string): Right Ascension as a string with three parts 'HH.MM.SS' (Hours, Minutes, Seconds)
* **[REQUIRED]** dec (int/float): Declination as a postive or negative value
* **[REQUIRED]** properMotionSpeedRA (int/float): Speed of Proper Motion along the Right Ascension
* **[REQUIRED]** properMotionSpeedDec (int/float): Speed of Proper Motion along the Declination
* **[REQUIRED]** magnitudeVisual (int/float):

Important Note: RA/Dec proper motion will be converted from speed along the right ascension and declination to a proper motion speed (`properMotionSpeed`) and an angle (`properMotionAngle`) for further calculations

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 
'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 
'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 
'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 
'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 
'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 
'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 
'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 
'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 
'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 
'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

## Plot Stars on a Polar Chart
**plotStereographicProjection()**

Plot stars on a Stereographic Polar Plot
```
plotStereographicProjection(northOrSouth=None, 
			builtInStars=[], 
			declination_min=None,
			yearSince2000=0,
			displayStarNamesLabels=True,
			displayDeclinationNumbers=True,
			incrementBy=10,
			isPrecessionIncluded=True,
			maxMagnitudeFilter=None,
			userDefinedStars=[],
			onlyDisplayUserStars=False,
			showPlot=True,
			fig_plot_title=None,
			fig_plot_color="C0",
			figsize_n=12,
			figsize_dpi=100,
			save_plot_name=None)
```
- **[REQUIRED]** northOrSouth: (string) map for either the "North" or "South" hemisphere
- *[OPTIONAL]* builtInStars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in star_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* declination_min: (int/float) outer declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* displayStarNamesLabels: (boolean) display the star name labels, defaults to True
- *[OPTIONAL]* displayDeclinationNumbers: (boolean) display declination values, defaults to True
- *[OPTIONAL]* incrementBy: (int) increment values for declination (either 1, 5, 10), defaults to 10
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* maxMagnitudeFilter: (int/float) filter existing stars by magnitude by setting the max magnitude for the chart to include, defaults to None (shows all stars)
- *[OPTIONAL]* userDefinedStars: (list) List of newStar objects of stars the user has added
- *[OPTIONAL]* onlyDisplayUserStars: (bool) Only display the stars defined by the users (userDefinedStars)
- *[OPTIONAL]* showPlot: (boolean) show plot (triggers plt.show()) when finished running, defaults to True
- *[OPTIONAL]* fig_plot_title: (string) figure title, defaults to "<North/South>ern Hemisphere [<YEAR NUMBERS> Years Since 2000 (YYYY)]: +/-90° to <DECLINATION MIN>°"
- *[OPTIONAL]* fig_plot_color: (string) scatter plot star color, defaults to C0
- *[OPTIONAL]* figsize_n: (int/float) figure size, default to 12
- *[OPTIONAL]* figsize_dpi: (int/float) figure DPI, default to 100
- *[OPTIONAL]* save_plot_name: (string) save plot with a string name, defaults to not saving

<details closed>
<summary>Stars that will be included by default when builtInStars = [] (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 
'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 
'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 
'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 
'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 
'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 
'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 
'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 
'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 
'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 
'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

| northOrSouth="North" (-30° to 90°) | northOrSouth="South" (30° to -90°)|
| ------------- | ------------- |
| ![north_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png) |  ![south_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_without_precession.png) |

| builtInStars=[] (Includes all stars, default) | builtInStars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"]|
| ------------- | ------------- |
| ![builtInStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_default.png) | ![builtInStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/builtInStars_subset.png) |

| declination_min=-30° (default) | declination_min=10° |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_20.png) |

| yearSince2000=0 (default) | yearSince2000=-3100 |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/yearSince2000_1100.png) |

| displayStarNamesLabels=True (default) | declination_min=False |
| ------------- | ------------- |
| ![north_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png)  | ![north_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png) |

| displayDeclinationNumbers=True (default) | displayDeclinationNumbers=False |
| ------------- | ------------- |
| ![displayDeclinationNumbers+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png)  | ![displayDeclinationNumbers+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/displayDeclinationNumbers_false.png) |

| incrementBy=10 (default) | declination_min=5 |
| ------------- | ------------- |
| ![incrementBy_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/incrementBy_default.png) | ![incrementBy_5+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/incrementBy_5.png) |

| isPrecessionIncluded=True (default) | isPrecessionIncluded=False |
| ------------- | ------------- |
| ![isPrecessionIncluded_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/isPrecessionIncluded_default.png) | ![isPrecessionIncluded_false+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/isPrecessionIncluded_false.png) |

| maxMagnitudeFilter=None (default) | maxMagnitudeFilter=1 |
| ------------- | ------------- |
| ![maxMagnitudeFilter_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/maxMagnitudeFilter_default.png) | ![maxMagnitudeFilter+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/maxMagnitudeFilter_1.png) |

| onlyDisplayUserStars=False (default) with userDefinedStars | onlyDisplayUserStars=True with userDefined Stars |
| ------------- | ------------- |
| ![onlyDisplayUserStars_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/onlyDisplayUserStars_default.png) | ![onlyDisplayUserStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/onlyDisplayUserStars_true.png) |

| fig_plot_title=(default) | fig_plot_title="Example Figure Title" |
| ------------- | ------------- |
| ![fig_plot_title_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_title_default.png) | ![fig_plot_title+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_title_example.png) |

| fig_plot_color="C0" (default) | fig_plot_color="darkorchid" |
| ------------- | ------------- |
| ![fig_plot_color_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_title_default.png) | ![fig_plot_color_dark_orchid+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_color_darkorchid.png) |

__Star Chart in the Northern Hemisphere (centered on 90°) without Precession__
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="red")
```
![north_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png) 
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="red")
```
![north_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_without_precession.png) 
__Star Chart in the Northern Hemisphere (centered on 90°) with Precession__
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="red")
```
![north_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_with_precession.png) 
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="red")
```
![north_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_with_precession.png) 
__Star Chart in the Southern Hemisphere (centered on -90°) without Precession__
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_without_precession.png) 
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_without_precession.png) 
__Star Chart in the Southern Hemisphere (centered on -90°) with Precession__
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_with_precession.png) 
```
star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_with_precession.png) 

## Return Final Position of Stars
**finalPositionOfStars()**

Returns a dictionary for the final positions of the stars in the format: {'Star Name': {"Declination" : Declination (int), "RA": RA (str)}
```
finalPositionOfStars(builtInStars=[],
		yearSince2000=0, 
		isPrecessionIncluded=True,
		userDefinedStars=[],
		onlyDisplayUserStars=False,
		declination_min=None,
		declination_max=None)
```
- *[OPTIONAL]* builtInStars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in star_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* userDefinedStars: (list) List of newStar objects of stars the user has added
- *[OPTIONAL]* onlyDisplayUserStars: (bool) Only include the stars defined by the users (userDefinedStars)
- *[OPTIONAL]* declination_min: (int/float) set minimum declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* declination_max: (int/float) set maximum declination value, defaults to 90° in Northern hemisphere and -90° in Southern hemisphere

<details closed>
<summary>Stars that will be included by default when builtInStars = [] (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 
'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 
'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 
'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 
'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 
'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 
'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 
'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 
'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 
'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 
'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

## Bibliography

Star position (right ascension and declination) as well as the angle and speed of proper motion taken from [in-the-sky.org](https://in-the-sky.org/)

Precession model: [Vondrák, J., et al. “New Precession Expressions, Valid for Long Time Intervals.” Astronomy &amp; Astrophysics, vol. 534, 2011](https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf)

Preecession code adapted to Python 3+ from [github.com/dreamalligator/vondrak](https://github.com/dreamalligator/vondrak)

## Bug and Feature Request

Submit a bug fix, question, or feature request as a [Github Issue](https://github.com/cyschneck/Star-Chart-Spherical-Projection/issues) or to cyschneck@gmail.com
