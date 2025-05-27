# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![PyPi-Versions](https://img.shields.io/pypi/pyversions/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)
[![repo-status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![pytests](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml/badge.svg?branch=main)](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml)

A Python package to generate circular astronomy star charts (past, present, and future) with spherical projection to correct for distortions with all IAU named stars accurate over 400,000 years with proper motion and precession of the equinoxes

* **Plot Stars on a Polar Chart**
	* plot_stereographic_projection()
* **Return Final Position of Stars**
	* final_position()
	* position_over_time()
	* plot_position()
	* predict_pole_star()
* **Add a New Star to Plot**
	* add_new_star()

## Quickstart: Star-Chart-Spherical-Projection
Plot stars in the Southern Hemisphere for the year 2025 (without stars labels)
```python
import star_chart_spherical_projection as scsp

scsp.plot_stereographic_projection(northOrSouth="South",
				displayStarNamesLabels=False,
				maxMagnitudeFilter=3,
				yearSince2000=25)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/quickstart_south_years.png) 

Plot a few built-in stars as well as two new user defined stars in the Northern Hemisphere for the year 1961 (2000-39) (with stars labels and in red). This uses both methods to define the proper motion for new stars: with a given proper motion and angle and with the proper motion speed in the declination and right ascension
```python
import star_chart_spherical_projection as scsp

exalibur_star = scsp.add_new_star(star_name="Exalibur",
				ra="14.04.23",
				dec=64.22,
				pm_speed=12.3,
				pm_angle=83,
				magnitude=1.2)
karaboudjan_star = scsp.add_new_star(star_name="Karaboudjan",
				ra="3.14.15",
				dec=10.13,
				pm_speed_ra=57.6,
				properMotionSpeedDec=60.1,
				magnitude=0.3)
scsp.plot_stereographic_projection(northOrSouth="North",
				included_stars=["Vega", "Arcturus", "Altair"],
				userDefinedStars=[exalibur_star, karaboudjan_star],
				displayStarNamesLabels=True,
				fig_plot_color="red",
				yearSince2000=-39)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/quickstart_newstar_example.png) 


Return the final position of a Vega (can be a single star or a list of stars) after 11,500 years when Vega is the new North Pole Star (star closest to +90°)
```python
import star_chart_spherical_projection as scsp

star_final_pos_dict = scsp.final_position(included_stars=["Vega"],
						yearSince2000=11500,
						save_to_csv="final_star_positions.csv")
```
Returns a dictionary with a star and its declination and right ascension: `{'Vega': {'Declination': 83.6899118156341, 'RA': '05.38.21'}}`

The final position of the stars are saved in `final_star_positions.csv` with the headers ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]

## Install

PyPi pip install at [pypi.org/project/star-chart-spherical-projection/](https://pypi.org/project/star-chart-spherical-projection/)

```
pip install star-chart-spherical-projection
```

## Overview

The first step to plot the celestial sphere onto a 2D plot is to map the star's right ascension as hours along the plot (matplotlib polar plot's theta value) and declination as the distance from the center of the circle (matplotlib polar plot's radius value). However, attempting to map the right ascension and declination directly will cause distortion since the angles between the stars along the declination are no longer conserved. On the left, the constellation of the Big Dipper is stretched into an unfamiliar shape due to this distortion. By accounting for the spherical transformation, the star chart can be corrected as seen on the right.

| Without Correction | With Correction |
| ------------- | ------------- |
| ![without_correction](https://user-images.githubusercontent.com/22159116/202333014-a53f1176-182f-43c7-ab92-266d15d8c563.jpg) | ![with_correction](https://user-images.githubusercontent.com/22159116/202333015-493619f4-a5b8-4614-8b32-54225d7fad02.png) |

The sphere is projected from the South Pole (via [Stereographic projection](https://gisgeography.com/azimuthal-projection-orthographic-stereographic-gnomonic/)):
 <p align="center">
  <img src="https://gisgeography.com/wp-content/uploads/2016/06/Stereographic-Projection.jpg" />
</p>


From the perspective of an observer on the Earth's surface, the stars appear to sit along the surface of the celestial sphere--an imaginary sphere of arbitrary radius with the Earth at its center. All objects in the sky will appear projected on the celestial sphere regardless of their true distance from Earth. Each star's position is given by two values. Declination is the angular distance from the celestial equator and right ascension is the distance from the position of the vernal equinox. During the course of a full 24-hour day, stars will appear to rotate across the sky as a result of the Earth's rotation, but their position is fixed. A star’s actual position does change over time as the combined result of the star’s small movement (proper motion) as well as the changing rotational axis of the Earth (precession).
 
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
Where in the Northern Hemisphere, projections are formed from the South Pole: 
![morrisons_astrolabe](https://user-images.githubusercontent.com/22159116/202336728-dc290bfa-44f5-4947-9a08-93f70286436e.jpg)

### Data

All IAU named stars are collected from [`pas.rochester.edu`](https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt).

[IAU Named Stars](https://github.com/cyschneck/Star-Chart-Spherical-Projection/blob/main/star_chart_spherical_projection/data/1_iau_stars.csv):

- Common Name
- Designation

Data is collected via automatic web scrapping from [`in-the-sky.org`](https://github.com/cyschneck/Star-Chart-Spherical-Projection/blob/main/star_chart_spherical_projection/data/2_inthesky_star_data.csv) and [`wikipedia.org`](https://github.com/cyschneck/Star-Chart-Spherical-Projection/blob/main/star_chart_spherical_projection/data/3_backup_star_data.csv) (and some [manual additions](https://github.com/cyschneck/Star-Chart-Spherical-Projection/blob/main/star_chart_spherical_projection/data/0_missing_manual.csv))

All [star data](https://github.com/cyschneck/Star-Chart-Spherical-Projection/blob/main/star_chart_spherical_projection/data/4_all_stars_data.csv):

- Common Name
- Right Ascension (HH.MM.SS)
- Declination (DD.SS)
- Magnitude (V, Visual)
- Proper Motion Speed (mas/yr)
- Proper Motion Angle (DD.SS)
- Proper Motion RA (mas/yr)
- Proper Motion DEC (mas/yr)
- Alternative Names
- URL

## Add a New Star

### New Star Object

The star chart package comes with over a hundred of brightest stars as part of a built-in library. However, a new star can be easily added for plotting or calculations by creating a new star object. The new star object will require a few important features that plot_stereographic_projection() and final_position() can now accept as an additional argument.

This allows for the creation of a new star in two ways:

**1. With a Proper Motion Speed and a Proper Motion Angle**

As seen in [in-the-sky.org for Pollux](https://in-the-sky.org/data/object.php?id=TYC1920-2194-1)
```
star_chart_spherical_projection.add_new_star(star_name=None,
					ra=None,
					dec=None,
					pm_speed=None,
					pm_angle=None,
					magnitude=None)
```
* **[REQUIRED]** star_name: (string) A star name to be displayed as a label
* **[REQUIRED]** ra: (string) Right Ascension of star as a string with three parts 'HH.MM.SS' (Hours, Minutes, Seconds)
* **[REQUIRED]** dec: (int/float) Declination of star (a positive or negative value)
* **[REQUIRED]** pm_speed: (int/float) Proper motion speed as a single value (in mas/year)
* **[REQUIRED]** pm_angle: (int/float) Proper motion positive angle (between 0° and 360°)
* **[REQUIRED]** magnitude: (int/float) Absolute Visual Magnitude

**With the Proper Motion speed along the Right Ascension and Declination**

As seen in [wikipeida.og for Pollux](https://en.wikipedia.org/wiki/Pollux_(star))

```
star_chart_spherical_projection.add_new_star(star_name=None,
					ra=None,
					dec=None,
					pm_speed_ra=None,
					properMotionSpeedDec=None,
					magnitude=None)
```
* **[REQUIRED]** star_name: (string) A star name to be displayed as a label
* **[REQUIRED]** ra: (string) Right Ascension of star as a string with three parts 'HH.MM.SS' (Hours, Minutes, Seconds)
* **[REQUIRED]** dec: (int/float) Declination of star (a positive or negative value)
* **[REQUIRED]** pm_speed_ra: (int/float) Speed of Proper Motion along the Right Ascension
* **[REQUIRED]** properMotionSpeedDec: (int/float) Speed of Proper Motion along the Declination
* **[REQUIRED]** magnitude: (int/float) Absolute Visual Magnitude

Important Note: RA/Dec proper motion will be converted from speed along the right ascension and declination to a proper motion speed (`pm_speed`) and an angle (`pm_angle`) for further calculations

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
['Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Arcalis', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axolotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Baekdu', "Barnard's Star", 'Baten Kaitos', 'Beemim', 'Beid', 'Belel', 'Belenos', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibha', 'Biham', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chason', 'Chechia', 'Chertan', 'Citadelle', 'Citala', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dingolay', 'Diphda', 'Diwo', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gomeisa', 'Grumium', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heze', 'Hoggar', 'Homam', 'Horna', 'Hunahpu', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaffaljidhma', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Kornephoros', 'Kraz', 'Kurhah', 'La Superba', 'Larawag', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitania', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marohu', 'Marsic', 'Matar', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Monch', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Nasti', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Ogma', 'Okab', 'Paikauhale', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Piautos', 'Pincoya', 'Pipirima', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rastaban', 'Regulus', 'Revati', 'Rigel', 'Rigil Kentaurus', 'Rosaliadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Sagarmatha', 'Saiph', 'Salm', 'Samaya', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Spica', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupa', 'Tupi', 'Tureis', 'Ukdah', 'Uklun', 'Unukalhai', 'Uruk', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wazn', 'Wezen', 'Wurren', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Zaniah', 'Zaurak', 'Zavijava', 'Zhang', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali']
</details>

## Plot Stars on a Polar Chart
**plot_stereographic_projection()**

Plot stars on a Stereographic Polar Plot
```
plot_stereographic_projection(northOrSouth=None, 
			included_stars=[], 
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
- *[OPTIONAL]* included_stars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in 4_all_stars_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* declination_min: (int/float) outer declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* displayStarNamesLabels: (boolean) display the star name labels, defaults to True
- *[OPTIONAL]* displayDeclinationNumbers: (boolean) display declination values, defaults to True
- *[OPTIONAL]* incrementBy: (int) increment values for declination (either 1, 5, 10), defaults to 10
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* maxMagnitudeFilter: (int/float) filter existing stars by magnitude by setting the max magnitude for the chart to include, defaults to None (shows all stars)
- *[OPTIONAL]* userDefinedStars: (list) List of new star objects of stars the user has added
- *[OPTIONAL]* onlyDisplayUserStars: (bool) Only display the stars defined by the users (userDefinedStars)
- *[OPTIONAL]* showPlot: (boolean) show plot (triggers plt.show()), useful when generating multiple plots at once in the background, defaults to True
- *[OPTIONAL]* fig_plot_title: (string) figure title, defaults to "<North/South>ern Hemisphere [<YEAR NUMBERS> Years Since 2000 (YYYY)]: +/-90° to <DECLINATION MIN>°"
- *[OPTIONAL]* fig_plot_color: (string) scatter plot star color, defaults to C0
- *[OPTIONAL]* figsize_n: (int/float) figure size, default to 12
- *[OPTIONAL]* figsize_dpi: (int/float) figure DPI, default to 100
- *[OPTIONAL]* save_plot_name: (string) save plot with a string name, defaults to not saving

<details closed>
<summary>Stars that will be included by default when included_stars = [] (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnair', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Delta Velorum', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kaus Australis', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 'Tureis', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

| northOrSouth="North" (-30° to 90°) (without star labels) | northOrSouth="South" (30° to -90°) (without star labels) |
| ------------- | ------------- |
| ![northOrSouth+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/northOrSouth_north.png) |  ![northOrSouth+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/northOrSouth_south.png) |

| included_stars=[] (Includes all stars, default) | included_stars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"]|
| ------------- | ------------- |
| ![includedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/includedStars_default.png) | ![includedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/includedStars_subset.png) |

| declination_min=-30° (default) (without star labels) | declination_min=10° (without star labels) |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/declination_min_10.png) |

| yearSince2000=0 (default) (without star labels) | yearSince2000=-3100 (without star labels) |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/yearSince2000_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/yearSince2000_negative_3100.png) |

| displayStarNamesLabels=True (default) | displayStarNamesLabels=False |
| ------------- | ------------- |
| ![displayStarNamesLabels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/displayStarNamesLabels_default.png)  | ![displayStarNamesLabels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/displayStarNamesLabels_false.png) |

| displayDeclinationNumbers=True (default) (without star labels) | displayDeclinationNumbers=False (without star labels) |
| ------------- | ------------- |
| ![displayDeclinationNumbers+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/displayDeclinationNumbers_default.png)  | ![displayDeclinationNumbers+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/displayDeclinationNumbers_false.png) |

| incrementBy=10 (default) (without star labels) | incrementBy=5 (without star labels) |
| ------------- | ------------- |
| ![incrementBy_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/incrementBy_default.png) | ![incrementBy_5+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/incrementBy_5.png) |

| isPrecessionIncluded=True (default) (yearSince2000=11500) (without star labels) | isPrecessionIncluded=False (yearSince2000=11500) (without star labels) |
| ------------- | ------------- |
| ![isPrecessionIncluded_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/isPrecessionIncluded_default.png) | ![isPrecessionIncluded_false+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/isPrecessionIncluded_false.png) |

| maxMagnitudeFilter=None (default) | maxMagnitudeFilter=1 |
| ------------- | ------------- |
| ![maxMagnitudeFilter_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/maxMagnitudeFilter_default.png) | ![maxMagnitudeFilter+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/maxMagnitudeFilter_1.png) |

| userDefinedStars=[] (default) (with just "Vega") | userDefinedStars=[exalibur_star, karaboudjan_star] (from Quickstart with "Vega") |
| ------------- | ------------- |
| ![userDefinedStars_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/userDefinedStars_none.png) | ![userDefinedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/userDefinedStars_included.png) |

| onlyDisplayUserStars=False (default) with userDefinedStars | onlyDisplayUserStars=True with userDefinedStars=[exalibur_star, karaboudjan_star] (from Quickstart) |
| ------------- | ------------- |
| ![onlyDisplayUserStars_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/onlyDisplayUserStars_default.png) | ![onlyDisplayUserStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/onlyDisplayUserStars_true.png) |

| fig_plot_title=(default) | fig_plot_title="This is a Example Title for a Star Chart" |
| ------------- | ------------- |
| ![fig_plot_title_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_title_default.png) | ![fig_plot_title+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_title_example.png) |

| fig_plot_color="C0" (default) (without star labels) | fig_plot_color="darkorchid" (without star labels) |
| ------------- | ------------- |
| ![fig_plot_color_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_color_default.png) | ![fig_plot_color_dark_orchid+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/fig_plot_color_darkorchid.png) |

## Return Final Position of Stars
**final_position()**

Returns a dictionary for the final positions of the stars for a specific year in the format: {'Common Name': {"Declination" : Declination (int), "RA": RA (str)}
```
final_position(included_stars=[],
		yearSince2000=0, 
		isPrecessionIncluded=True,
		userDefinedStars=[],
		onlyDisplayUserStars=False,
		declination_min=None,
		declination_max=None,
		save_to_csv=None)
```
- *[OPTIONAL]* included_stars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in 4_all_stars_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* yearSince2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* userDefinedStars: (list): List of new star objects of stars the user has added
- *[OPTIONAL]* onlyDisplayUserStars: (bool) Only include the stars defined by the users (userDefinedStars)
- *[OPTIONAL]* declination_min: (int/float) set minimum declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* declination_max: (int/float) set maximum declination value, defaults to 90° in Northern hemisphere and -90° in Southern hemisphere
- *[OPTIONAL]* save_to_csv: (string) CSV filename and location to save final star positions with headers ["Common Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]

<details closed>
<summary>Stars that will be included by default when included_stars = [] (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnair', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Delta Velorum', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kaus Australis', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 'Tureis', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

## Return A Star's Position over Time
**position_over_time()**

Returns a single star's position over time

```
position_over_time(builtInStarName=None,
			newStar=None,
			startYearSince2000=None,
			endYearSince2000=None,
			incrementYear=5,
			isPrecessionIncluded=True,
			save_to_csv=None)
```
- **[REQUIRED]** builtInStarName: (string) a star name from the built-in list, example: `Vega`
- **[REQUIRED]** newStar: (add_new_star object) a new star included created from a add_new_star()
- **[REQUIRED]** startYearSince2000: (float/int) start year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** endYearSince2000: (float/int) end year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** incrementYear: (float/int) number of year to increment from start to end by, defaults to `5` years
- *[OPTIONAL]* isPrecessionIncluded: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* save_to_csv: (string) CSV filename and location to save star's position over time with headers ["Year", "Declination (DD.SS)", "Right Ascension (HH.MM.SS)", "Right Ascension (radians)"]

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnair', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Delta Velorum', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kaus Australis', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 'Tureis', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

## Predict Past and Future Pole Stars
**predict_pole_star**

Return the North/South Pole star for a given year since 2000
```
predict_pole_star(yearSince2000=0, northOrSouth="North")
```
- **[REQUIRED]** yearSince2000 (int/float): ear since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* northOrSouth (string): North or South Pole where `North` = 90° and `South` = -90°, defaults to `North`

## Plot a Star's Position over Time
**plot_position()**

Plot a star's declination and right ascension position over time

```
plot_position(builtInStarName=None, 
			newStar=None,
			startYearSince2000=None,
			endYearSince2000=None,
			incrementYear=10,
			isPrecessionIncluded=True,
			DecOrRA="D",
			showPlot=True,
			showYearMarker=True,
			fig_plot_title=None,
			fig_plot_color="C0",
			figsize_n=12,
			figsize_dpi=100,
			save_plot_name=None)
```
- **[REQUIRED]** builtInStarName: (string) a star name from the built-in list, example: `Vega`
- **[REQUIRED]** newStar: (newStar object) a new star included created from a newStar object
- **[REQUIRED]** startYearSince2000: (float/int) start year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** endYearSince2000: (float/int) end year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** DecOrRA: (string) Plot the Declination `D` or Right Ascension `RA`, defaults to `D`
- **[REQUIRED]** incrementYear: (float/int)  number of year to increment from start to end by, defaults to `10` years
- *[OPTIONAL]* isPrecessionIncluded: (boolean)  when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* showPlot: (boolean) show plot (triggers plt.show()), useful when generating multiple plots at once in the background, defaults to True
- *[OPTIONAL]* showYearMarker: (boolean) show dotted line for current year
- *[OPTIONAL]* fig_plot_title: (string) figure plot title, defaults to `<COMMON NAME> <DECLINATION/RA> (<With/Without> Precession) from <START BCE/CE> to <END BCE/CE>, every <YEAR INCREMENT> Years`
- *[OPTIONAL]* fig_plot_color: (string) figure plot color, defaults to blue `C0`
- *[OPTIONAL]* figsize_n: (float/int) figure plot size NxN, `12`
- *[OPTIONAL]* figsize_dpi: (float/int) figure dpi, defaults to `100`
- *[OPTIONAL]* save_plot_name: (string) save plot name and location

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnair', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Delta Velorum', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kaus Australis', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Thuban', 'Tureis', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']
</details>

**Declination with Precession:**
```python
star_chart_spherical_projection.plot_position(builtInStarName="Vega",
							newStar=None,
							startYearSince2000=-15000,
							endYearSince2000=15000,
							isPrecessionIncluded=True,
							incrementYear=5,
							DecOrRA="D")
```
![plot_star_declination_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/plot_star_vega_declination_with_precession.png) 
**Declination without Precession:**
```python
star_chart_spherical_projection.plot_position(builtInStarName="Vega",
							newStar=None,
							startYearSince2000=-15000,
							endYearSince2000=15000,
							isPrecessionIncluded=False,
							incrementYear=5,
							DecOrRA="D")
```
![plot_star_declination_without_prcession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/plot_star_vega_declination_without_precession.png) 
**Right Ascension with Precession:**
```python
star_chart_spherical_projection.plot_position(builtInStarName="Vega",
							newStar=None,
							startYearSince2000=-15000,
							endYearSince2000=15000,
							isPrecessionIncluded=True,
							incrementYear=5,
							DecOrRA="R")
```
![plot_star_RA_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/plot_star_vega_right_ascension_with_precession.png) 
**Right Ascension without Precession:**
```python
star_chart_spherical_projection.plot_position(builtInStarName="Vega",
							newStar=None,
							startYearSince2000=-15000,
							endYearSince2000=15000,
							isPrecessionIncluded=False,
							incrementYear=5,
							DecOrRA="R")
```
![plot_star_RA_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/plot_star_vega_right_ascension_without_precession.png) 

# Star Chart Examples:
__Star Chart in the Northern Hemisphere (centered on 90°) without Precession__
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="North",
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="red")
```
![north_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_without_precession.png) 
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="North",
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="red")
```
![north_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_without_precession.png) 
__Star Chart in the Northern Hemisphere (centered on 90°) with Precession__
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="North",
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="red")
```
![north_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_without_labels_with_precession.png) 
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="North",
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="red")
```
![north_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/north_with_labels_with_precession.png) 
__Star Chart in the Southern Hemisphere (centered on -90°) without Precession__
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="South", 
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_without_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_without_precession.png) 
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="South", 
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=False,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_with_labels_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_without_precession.png) 
__Star Chart in the Southern Hemisphere (centered on -90°) with Precession__
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="South", 
							displayStarNamesLabels=False,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_without_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_without_labels_with_precession.png) 
```
star_chart_spherical_projection.plot_stereographic_projection(northOrSouth="South", 
							displayStarNamesLabels=True,
							yearSince2000=11500,
							isPrecessionIncluded=True,
							fig_plot_color="cornflowerblue")
```
![south_star_chart_with_labels_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/examples/south_with_labels_with_precession.png) 

## Development Environment
To run or test against `star-chart-spherical-projection` github repo/fork, a development environment can be created via conda/miniconda

First, [install Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)

Then, using the existing `environment.yml`, a new conda environment can be create to run/test scripts against

```
conda env create --file environment.yml
```
Once the environment has been built, activate the environment:
```
conda activate star_chart
```
To run existing and new tests from the root directory:
```
python -m pytest
```

## Bibliography

Named stars specified by ["IAU Catalog of Star Names"](https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt) with the star position (right ascension and declination) as well as the angle and speed of proper motion from [in-the-sky.org](https://in-the-sky.org/) and Wikipedia where indicated

Precession model: [Vondrák, J., et al. “New Precession Expressions, Valid for Long Time Intervals.” Astronomy &amp; Astrophysics, vol. 534, 2011](https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf)

Precession code adapted to Python 3+ from [the Vondrak long term precession model Github repo 'vondrak')](https://github.com/dreamalligator/vondrak)

## Bug and Feature Request

Submit a bug fix, question, or feature request as a [Github Issue](https://github.com/cyschneck/Star-Chart-Spherical-Projection/issues) or to cyschneck@gmail.com
