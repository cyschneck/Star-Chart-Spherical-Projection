# Star-Chart-Spherical-Projection

![PyPi](https://img.shields.io/pypi/v/star-chart-spherical-projection)
![PyPi-Versions](https://img.shields.io/pypi/pyversions/star-chart-spherical-projection)
![license](https://img.shields.io/github/license/cyschneck/Star-Chart-Spherical-Projection)
[![repo-status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![pytests](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml/badge.svg?branch=main)](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/pytests.yml)
[![data-up-to-date](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/keep_data_up_to_date.yml/badge.svg)](https://github.com/cyschneck/Star-Chart-Spherical-Projection/actions/workflows/keep_data_up_to_date.yml)
[![codecov](https://codecov.io/gh/cyschneck/Star-Chart-Spherical-Projection/graph/badge.svg?token=NUBO678KTO)](https://codecov.io/gh/cyschneck/Star-Chart-Spherical-Projection)

A Python package to generate circular astronomy star charts (past, present, and future) with spherical projection to correct for distortions with all IAU named stars accurate over 400,000 years with proper motion and precession of the equinoxes

* **Plot Stars on a (Polar) Star Chart**
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

scsp.plot_stereographic_projection(pole="South",
                display_labels=False,
                max_magnitude=3,
                year_since_2000=25)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/quickstart_south_years.png) 

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
                pm_speed_dec=60.1,
                magnitude=0.3)
scsp.plot_stereographic_projection(pole="North",
                included_stars=["Vega", "Arcturus", "Altair"],
                added_stars=[exalibur_star, karaboudjan_star],
                display_labels=True,
                fig_plot_color="red",
                year_since_2000=-39)
```
![quickstart_star_chart+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/quickstart_newstar_example.png) 

Or, a simple chart with the Big Dipper
```python
import star_chart_spherical_projection as scsp

scsp.plot_stereographic_projection(pole="North",
                                   included_stars=["Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alkaid"],
                                   display_labels=False,
                                   year_since_2000=-39,
                                   declination_min=40)
```
![quickstart_star_chart_big_dipper+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/quickstart_bigDipper.png) 

Return the final position of a Vega (can be a single star or a list of stars) after 11,500 years when Vega is the new North Pole Star (star closest to +90°)
```python
import star_chart_spherical_projection as scsp

star_final_pos_dict = scsp.final_position(included_stars=["Vega"],
                        year_since_2000=11500,
                        save_to_csv="final_star_positions.csv")
```
Returns a dictionary with a star and its declination and right ascension: `{'Vega': {'Declination': 83.02282965393113, 'RA': '05.07.57655389657'}}`

The final position of the stars are saved in `final_star_positions.csv` with the headers ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]

This can be used to determine past and future pole stars. For example, [Wikipedia states that the star Thuban](https://en.wikipedia.org/wiki/Thuban) is:

> A relatively inconspicuous star in the night sky of the Northern Hemisphere, it is historically significant as having been the north pole star from the 4th to 2nd millennium BC

```python
import star_chart_spherical_projection as scsp

scsp.final_position(included_stars=["Thuban"], year_since_2000=-5000))
```
So, 5000 years ago, Thuban sat at a declination of `88.89649680362646` degrees, representing the nearest named star to the North Pole (90 degrees)

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

All IAU named stars are collected from the [IAU WSGN Star Catalog](https://exopla.net/star-names/modern-iau-star-names/)

[![ReadMe Card](https://github-readme-stats.vercel.app/api/pin/?username=cyschneck&repo=iau-star-names)](https://github.com/cyschneck/iau-star-names)

[IAU Named Stars with Data](https://github.com/cyschneck/iau-star-names/blob/main/iau_proper_stars.csv)

- Proper Names
- WSGN-ID
- Designation
- HIP
- Bayer ID
- Constellation
- Origin
- Ethnic, Cultural Group, or Language
- Reference
- Additional Info, e.g. language corruptions
- Date of Adoption

Data is collected via automatic web scrapping from [`in-the-sky.org`](https://github.com/cyschneck/iau-star-names/blob/main/data/2_inthesky_star_data.csv) and [`wikipedia.org`](https://github.com/cyschneck/iau-star-names/blob/main/data/3_backup_star_data.csv) (and some [manual additions](https://github.com/cyschneck/iau-star-names/blob/main/data/0_missing_manual.csv))

The [stars with relevant data](https://github.com/cyschneck/iau-star-names/blob/main/stars_with_data.csv) is collected as:

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

The star chart package comes with hundreds of the brightest stars as part of a built-in library. However, a new star can be easily added for plotting or calculations by creating a new star object. The new star object will require a few important features that plot_stereographic_projection() and final_position() can now accept as an additional argument.

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

As seen in [wikipedia.org for Pollux](https://en.wikipedia.org/wiki/Pollux_(star))

```
star_chart_spherical_projection.add_new_star(star_name=None,
                    ra=None,
                    dec=None,
                    pm_speed_ra=None,
                    pm_speed_dec=None,
                    magnitude=None)
```
* **[REQUIRED]** star_name: (string) A star name to be displayed as a label
* **[REQUIRED]** ra: (string) Right Ascension of star as a string with three parts 'HH.MM.SS' (Hours, Minutes, Seconds)
* **[REQUIRED]** dec: (int/float) Declination of star (a positive or negative value)
* **[REQUIRED]** pm_speed_ra: (int/float) Speed of Proper Motion along the Right Ascension
* **[REQUIRED]** pm_speed_dec: (int/float) Speed of Proper Motion along the Declination
* **[REQUIRED]** magnitude: (int/float) Absolute Visual Magnitude

Important Note: RA/Dec proper motion will be converted from speed along the right ascension and declination to a proper motion speed (`pm_speed`) and an angle (`pm_angle`) for further calculations

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
'Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aiolos', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfarasalkamil', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Antinous', 'Arcalís', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axólotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Añañuca', 'Baekdu', 'Bake-eo', "Barnard's Star", 'Baten Kaitos', 'Batsũ̀', 'Beemim', 'Beid', 'Belel', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibhā', 'Biham', 'Bodu', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Bélénos', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chasoň', 'Chechia', 'Chertan', 'Citadelle', 'Citalá', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Danfeng', 'Deltoton', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dilmun', 'Dingolay', 'Diphda', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Dìwö', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Filetdor', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Gar', 'Garnet Star', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gnomon', 'Gomeisa', 'Grumium', 'Guahayona', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heng', 'Heze', 'Hoerikwaggo', 'Hoggar', 'Homam', 'Honores', 'Horna', 'Hunahpú', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaewkosin', 'Kaffaljidhma', 'Kaffalmusalsala', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Komondor', 'Kornephoros', 'Kosjenka', 'Kraz', 'Kui', 'Kulou', 'Kurhah', 'La Superba', 'Lang-exster', 'Larawag', 'Leepwal', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitânia', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marsic', 'Maru', 'Matar', 'Matza', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Márohu', 'Mönch', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Noquisi', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Násti', 'Ogma', 'Okab', 'Orkaria', 'Paikauhale', 'Paradys', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Phyllon Kissinou', 'Piautos', 'Pincoya', 'Pipirima', 'Pipit', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Quadrans', 'Ramus', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rasalnaqa', 'Rastaban', 'Regulus', 'Revati', 'Rhombus', 'Rigel', 'Rigil Kentaurus', 'Rosalíadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Safina', 'Sagarmatha', 'Saiph', 'Salm', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Shaomin', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Shimu', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Solitaire', 'Spica', 'Stellio', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Sāmaya', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Tengshe', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianfu', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupi', 'Tupã', 'Tureis', 'Tusizuo', 'Udkadua', 'Ukdah', 'Uklun', 'Unukalhai', 'Uridim', 'Uruk', 'Uúba', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wattle', 'Wazn', 'Wezen', 'Wouri', 'Wurren', 'Xami', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Yunü', 'Zaniah', 'Zaurak', 'Zavijava', 'Zembra', 'Zhang', 'Zhou', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali'
</details>

## Plot Stars on a Polar Chart
**plot_stereographic_projection()**

Plot stars on a Stereographic Polar Plot
```
plot_stereographic_projection(pole=None, 
            included_stars=[], 
            declination_min=None,
            year_since_2000=0,
            display_labels=True,
            display_dec=True,
            increment=10,
            is_precession=True,
            max_magnitude=None,
            added_stars=[],
            only_added_stars=False,
            show_plot=True,
            fig_plot_title=None,
            fig_plot_color="C0",
            figsize_n=12,
            figsize_dpi=100,
            save_plot_name=None)
```
- **[REQUIRED]** pole: (string) map for either the "North" or "South" hemisphere
- *[OPTIONAL]* included_stars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in stars_with_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* declination_min: (int/float) outer declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* year_since_2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* display_labels: (boolean) display the star name labels, defaults to True
- *[OPTIONAL]* display_dec: (boolean) display declination values, defaults to True
- *[OPTIONAL]* increment: (int) increment values for declination (either 1, 5, 10), defaults to 10
- *[OPTIONAL]* is_precession: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* max_magnitude: (int/float) filter existing stars by magnitude by setting the max magnitude for the chart to include, defaults to None (shows all stars)
- *[OPTIONAL]* added_stars: (list) List of new star objects of stars the user has added
- *[OPTIONAL]* only_added_stars: (bool) Only display the stars defined by the users (added_stars)
- *[OPTIONAL]* show_plot: (boolean) show plot (triggers plt.show()), useful when generating multiple plots at once in the background, defaults to True
- *[OPTIONAL]* fig_plot_title: (string) figure title, defaults to "<North/South>ern Hemisphere [<YEAR NUMBERS> Years Since 2000 (YYYY)]: +/-90° to <DECLINATION MIN>°"
- *[OPTIONAL]* fig_plot_color: (string) scatter plot star color, defaults to C0
- *[OPTIONAL]* figsize_n: (int/float) figure size, default to 12
- *[OPTIONAL]* figsize_dpi: (int/float) figure DPI, default to 100
- *[OPTIONAL]* save_plot_name: (string) save plot with a string name, defaults to not saving

<details closed>
<summary>Stars that will be included by default when included_stars = [] (Click to view all)</summary>
<br>
'Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aiolos', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfarasalkamil', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Antinous', 'Arcalís', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axólotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Añañuca', 'Baekdu', 'Bake-eo', "Barnard's Star", 'Baten Kaitos', 'Batsũ̀', 'Beemim', 'Beid', 'Belel', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibhā', 'Biham', 'Bodu', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Bélénos', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chasoň', 'Chechia', 'Chertan', 'Citadelle', 'Citalá', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Danfeng', 'Deltoton', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dilmun', 'Dingolay', 'Diphda', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Dìwö', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Filetdor', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Gar', 'Garnet Star', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gnomon', 'Gomeisa', 'Grumium', 'Guahayona', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heng', 'Heze', 'Hoerikwaggo', 'Hoggar', 'Homam', 'Honores', 'Horna', 'Hunahpú', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaewkosin', 'Kaffaljidhma', 'Kaffalmusalsala', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Komondor', 'Kornephoros', 'Kosjenka', 'Kraz', 'Kui', 'Kulou', 'Kurhah', 'La Superba', 'Lang-exster', 'Larawag', 'Leepwal', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitânia', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marsic', 'Maru', 'Matar', 'Matza', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Márohu', 'Mönch', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Noquisi', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Násti', 'Ogma', 'Okab', 'Orkaria', 'Paikauhale', 'Paradys', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Phyllon Kissinou', 'Piautos', 'Pincoya', 'Pipirima', 'Pipit', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Quadrans', 'Ramus', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rasalnaqa', 'Rastaban', 'Regulus', 'Revati', 'Rhombus', 'Rigel', 'Rigil Kentaurus', 'Rosalíadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Safina', 'Sagarmatha', 'Saiph', 'Salm', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Shaomin', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Shimu', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Solitaire', 'Spica', 'Stellio', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Sāmaya', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Tengshe', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianfu', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupi', 'Tupã', 'Tureis', 'Tusizuo', 'Udkadua', 'Ukdah', 'Uklun', 'Unukalhai', 'Uridim', 'Uruk', 'Uúba', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wattle', 'Wazn', 'Wezen', 'Wouri', 'Wurren', 'Xami', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Yunü', 'Zaniah', 'Zaurak', 'Zavijava', 'Zembra', 'Zhang', 'Zhou', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali'
</details>

| pole="North" (-30° to 90°) (without star labels) | pole="South" (30° to -90°) (without star labels) |
| ------------- | ------------- |
| ![pole+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/pole_north.png) |  ![pole+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/pole_south.png) |

| included_stars=[] (Includes all stars, default) | included_stars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"]|
| ------------- | ------------- |
| ![includedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/includedStars_default.png) | ![includedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/includedStars_subset.png) |

| declination_min=-30° (default) (without star labels) | declination_min=10° (without star labels) |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/declination_min_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/declination_min_10.png) |

| year_since_2000=0 (default) (without star labels) | year_since_2000=-3100 (without star labels) |
| ------------- | ------------- |
| ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/yearSince2000_default.png) | ![declination_min+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/yearSince2000_negative_3100.png) |

| display_labels=True (default) | display_labels=False |
| ------------- | ------------- |
| ![display_labels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/displayLabels_default.png)  | ![display_labels+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/displayLabels_false.png) |

| display_dec=True (default) (without star labels) | display_dec=False (without star labels) |
| ------------- | ------------- |
| ![display_dec+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/displayDeclinationNumbers_default.png)  | ![display_dec+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/displayDeclinationNumbers_false.png) |

| increment=10 (default) (without star labels) | increment=5 (without star labels) |
| ------------- | ------------- |
| ![increment_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/increment_default.png) | ![increment_5+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/increment_5.png) |

| is_precession=True (default) (year_since_2000=11500) (without star labels) | is_precession=False (year_since_2000=11500) (without star labels) |
| ------------- | ------------- |
| ![isPrecession_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/isPrecession_default.png) | ![isPrecession_false+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/isPrecession_false.png) |

| max_magnitude=None (default) | max_magnitude=1 |
| ------------- | ------------- |
| ![maxMagnitude_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/maxMagnitudeFilter_default.png) | ![maxMagnitude+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/maxMagnitudeFilter_1.png) |

| added_stars=[] (default) (with just "Vega") | added_stars=[exalibur_star, karaboudjan_star] (from Quickstart with "Vega") |
| ------------- | ------------- |
| ![addedStars_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/added_stars_none.png) | ![addedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/added_stars_included.png) |

| only_added_stars=False (default) with `added_stars` | only_added_stars=True with added_stars=[exalibur_star, karaboudjan_star] (from Quickstart) |
| ------------- | ------------- |
| ![onlyAddedStars_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/only_added_stars_default.png) | ![onlyAddedStars+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/only_added_stars_true.png) |

| fig_plot_title=(default) | fig_plot_title="This is a Example Title for a Star Chart" |
| ------------- | ------------- |
| ![fig_plot_title_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/fig_plot_title_default.png) | ![fig_plot_title+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/fig_plot_title_example.png) |

| fig_plot_color="C0" (default) (without star labels) | fig_plot_color="darkorchid" (without star labels) |
| ------------- | ------------- |
| ![fig_plot_color_default+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/fig_plot_color_default.png) | ![fig_plot_color_dark_orchid+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/fig_plot_color_darkorchid.png) |

## Return Final Position of Stars
**final_position()**

Returns a dictionary for the final positions of the stars for a specific year in the format: {'Common Name': {"Declination" : Declination (int), "RA": RA (str)}
```
final_position(included_stars=[],
        year_since_2000=0, 
        is_precession=True,
        added_stars=[],
        only_added_stars=False,
        declination_min=None,
        declination_max=None,
        save_to_csv=None)
```
- *[OPTIONAL]* included_stars: (list) a list of star names to include from built-in list, by default = [] includes all stars (in stars_with_data.csv). Example: ["Vega", "Merak", "Dubhe"]
- *[OPTIONAL]* year_since_2000: (int/float) years since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* is_precession: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* added_stars: (list): List of new star objects of stars the user has added
- *[OPTIONAL]* only_added_stars: (bool) Only include the stars defined by the users (added_stars)
- *[OPTIONAL]* declination_min: (int/float) set minimum declination value, defaults to -30° in Northern hemisphere and 30° in Southern hemisphere
- *[OPTIONAL]* declination_max: (int/float) set maximum declination value, defaults to 90° in Northern hemisphere and -90° in Southern hemisphere
- *[OPTIONAL]* save_to_csv: (string) CSV filename and location to save final star positions with headers ["Common Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]

<details closed>
<summary>Stars that will be included by default when included_stars = [] (Click to view all)</summary>
<br>
'Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aiolos', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfarasalkamil', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Antinous', 'Arcalís', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axólotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Añañuca', 'Baekdu', 'Bake-eo', "Barnard's Star", 'Baten Kaitos', 'Batsũ̀', 'Beemim', 'Beid', 'Belel', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibhā', 'Biham', 'Bodu', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Bélénos', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chasoň', 'Chechia', 'Chertan', 'Citadelle', 'Citalá', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Danfeng', 'Deltoton', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dilmun', 'Dingolay', 'Diphda', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Dìwö', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Filetdor', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Gar', 'Garnet Star', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gnomon', 'Gomeisa', 'Grumium', 'Guahayona', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heng', 'Heze', 'Hoerikwaggo', 'Hoggar', 'Homam', 'Honores', 'Horna', 'Hunahpú', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaewkosin', 'Kaffaljidhma', 'Kaffalmusalsala', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Komondor', 'Kornephoros', 'Kosjenka', 'Kraz', 'Kui', 'Kulou', 'Kurhah', 'La Superba', 'Lang-exster', 'Larawag', 'Leepwal', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitânia', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marsic', 'Maru', 'Matar', 'Matza', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Márohu', 'Mönch', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Noquisi', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Násti', 'Ogma', 'Okab', 'Orkaria', 'Paikauhale', 'Paradys', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Phyllon Kissinou', 'Piautos', 'Pincoya', 'Pipirima', 'Pipit', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Quadrans', 'Ramus', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rasalnaqa', 'Rastaban', 'Regulus', 'Revati', 'Rhombus', 'Rigel', 'Rigil Kentaurus', 'Rosalíadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Safina', 'Sagarmatha', 'Saiph', 'Salm', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Shaomin', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Shimu', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Solitaire', 'Spica', 'Stellio', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Sāmaya', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Tengshe', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianfu', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupi', 'Tupã', 'Tureis', 'Tusizuo', 'Udkadua', 'Ukdah', 'Uklun', 'Unukalhai', 'Uridim', 'Uruk', 'Uúba', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wattle', 'Wazn', 'Wezen', 'Wouri', 'Wurren', 'Xami', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Yunü', 'Zaniah', 'Zaurak', 'Zavijava', 'Zembra', 'Zhang', 'Zhou', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali'
</details>

```python
star_chart_spherical_projection.final_position(included_stars=["Thuban", "Vega"], year_since_2000=20000)
```
Returns `{'Thuban': {'Declination': 87.71930377133644, 'RA': '02.43.565884268673'}, 'Vega': {'Declination': 45.70083460323206, 'RA': '15.23.181614439801'}}`

## Return A Star's Position over Time
**position_over_time()**

Returns a single star's position over time

```
position_over_time(star=None,
            added_star=None,
            start_year_since_2000=None,
            end_year_since_2000=None,
            increment=5,
            is_precession=True,
            save_to_csv=None)
```
- **[REQUIRED]** star: (string) a star name from the built-in list, example: `Vega`
- **[REQUIRED]** added_star: (add_new_star object) a new star included created from `add_new_star()`
- **[REQUIRED]** start_year_since_2000: (float/int) start year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** end_year_since_2000: (float/int) end year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** increment: (float/int) number of year to increment from start to end by, defaults to `5` years
- *[OPTIONAL]* is_precession: (boolean) when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* save_to_csv: (string) CSV filename and location to save star's position over time with headers ["Year", "Declination (DD.SS)", "Right Ascension (HH.MM.SS)", "Right Ascension (radians)"]

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
'Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aiolos', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfarasalkamil', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Antinous', 'Arcalís', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axólotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Añañuca', 'Baekdu', 'Bake-eo', "Barnard's Star", 'Baten Kaitos', 'Batsũ̀', 'Beemim', 'Beid', 'Belel', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibhā', 'Biham', 'Bodu', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Bélénos', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chasoň', 'Chechia', 'Chertan', 'Citadelle', 'Citalá', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Danfeng', 'Deltoton', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dilmun', 'Dingolay', 'Diphda', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Dìwö', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Filetdor', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Gar', 'Garnet Star', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gnomon', 'Gomeisa', 'Grumium', 'Guahayona', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heng', 'Heze', 'Hoerikwaggo', 'Hoggar', 'Homam', 'Honores', 'Horna', 'Hunahpú', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaewkosin', 'Kaffaljidhma', 'Kaffalmusalsala', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Komondor', 'Kornephoros', 'Kosjenka', 'Kraz', 'Kui', 'Kulou', 'Kurhah', 'La Superba', 'Lang-exster', 'Larawag', 'Leepwal', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitânia', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marsic', 'Maru', 'Matar', 'Matza', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Márohu', 'Mönch', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Noquisi', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Násti', 'Ogma', 'Okab', 'Orkaria', 'Paikauhale', 'Paradys', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Phyllon Kissinou', 'Piautos', 'Pincoya', 'Pipirima', 'Pipit', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Quadrans', 'Ramus', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rasalnaqa', 'Rastaban', 'Regulus', 'Revati', 'Rhombus', 'Rigel', 'Rigil Kentaurus', 'Rosalíadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Safina', 'Sagarmatha', 'Saiph', 'Salm', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Shaomin', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Shimu', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Solitaire', 'Spica', 'Stellio', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Sāmaya', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Tengshe', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianfu', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupi', 'Tupã', 'Tureis', 'Tusizuo', 'Udkadua', 'Ukdah', 'Uklun', 'Unukalhai', 'Uridim', 'Uruk', 'Uúba', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wattle', 'Wazn', 'Wezen', 'Wouri', 'Wurren', 'Xami', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Yunü', 'Zaniah', 'Zaurak', 'Zavijava', 'Zembra', 'Zhang', 'Zhou', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali'
</details>

```python

star_chart_spherical_projection.position_over_time(star="Altair",
            start_year_since_2000=0,
            end_year_since_2000=20000,
            increment=10000,
            is_precession=True)
```
Returns `{2000: {'RA (radians)': -1.0907972465777118, 'RA (hours)': '19.50.4611519855', 'Dec (degrees)': 8.520199548428346}, 12000: {'RA (radians)': 1.4375977893307674, 'RA (hours)': '05.29.283886318377', 'Dec (degrees)': 52.15167008959445}, 22000: {'RA (radians)': -2.2007513306814537, 'RA (hours)': '15.35.374968785967', 'Dec (degrees)': 13.159743703293836}}`

## Predict Past and Future Pole Stars
**predict_pole_star**

Return the North/South Pole star for a given year since 2000
```
predict_pole_star(year_since_2000=0, pole="North", max_magnitude=None)
```
- **[REQUIRED]** year_since_2000 (int/float): ear since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- *[OPTIONAL]* pole (string): North or South Pole where `North` = 90° and `South` = -90°, defaults to `North`
- *[OPTIONAL]* max_magnitude: (int/float) filter existing stars by magnitude by setting the max magnitude for the chart to include, defaults to None (all stars)

For example:
```python
import star_chart_spherical_projection as scsp

scsp.predict_pole_star(year_since_2000=20000, pole="North")
```
As a result, in 20,000 years, `Thuban` will be the North Pole, replacing Polaris. 

## Plot a Star's Position over Time
**plot_position()**

Plot a star's declination and right ascension position over time

```
plot_position(star=None, 
            added_star=None,
            start_year_since_2000=None,
            end_year_since_2000=None,
            increment=10,
            is_precession=True,
            dec_ra="D",
            show_plot=True,
            display_year_marker=True,
            fig_plot_title=None,
            fig_plot_color="C0",
            figsize_n=12,
            figsize_dpi=100,
            save_plot_name=None)
```
- **[REQUIRED]** star: (string) a star name from the built-in list, example: `Vega`
- **[REQUIRED]** added_star: (new star object) a new star included created from `add_new_star()`
- **[REQUIRED]** start_year_since_2000: (float/int) start year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** end_year_since_2000: (float/int) end year since 2000 (-50 = 1950 and +50 = 2050) to calculate proper motion and precession, defaults = 0 years
- **[REQUIRED]** dec_ra: (string) Plot the Declination `D` or Right Ascension `RA`, defaults to `D`
- **[REQUIRED]** increment: (float/int)  number of year to increment from start to end by, defaults to `10` years
- *[OPTIONAL]* is_precession: (boolean)  when calculating star positions include predictions for precession, defaults to True
- *[OPTIONAL]* show_plot: (boolean) show plot (triggers plt.show()), useful when generating multiple plots at once in the background, defaults to True
- *[OPTIONAL]* display_year_marker: (boolean) show dotted line for current year
- *[OPTIONAL]* fig_plot_title: (string) figure plot title, defaults to `<COMMON NAME> <DECLINATION/RA> (<With/Without> Precession) from <START BCE/CE> to <END BCE/CE>, every <YEAR INCREMENT> Years`
- *[OPTIONAL]* fig_plot_color: (string) figure plot color, defaults to blue `C0`
- *[OPTIONAL]* figsize_n: (float/int) figure plot size NxN, `12`
- *[OPTIONAL]* figsize_dpi: (float/int) figure dpi, defaults to `100`
- *[OPTIONAL]* save_plot_name: (string) save plot name and location

<details closed>
<summary>Stars Built-in (Click to view all)</summary>
<br>
'Absolutno', 'Acamar', 'Achernar', 'Achird', 'Acrab', 'Acrux', 'Acubens', 'Adhafera', 'Adhara', 'Adhil', 'Ain', 'Ainalrami', 'Aiolos', 'Aladfar', 'Alasia', 'Albaldah', 'Albali', 'Albireo', 'Alchiba', 'Alcor', 'Alcyone', 'Aldebaran', 'Alderamin', 'Aldhanab', 'Aldhibah', 'Aldulfin', 'Alfarasalkamil', 'Alfirk', 'Algedi', 'Algenib', 'Algieba', 'Algol', 'Algorab', 'Alhena', 'Alioth', 'Aljanah', 'Alkaid', 'Alkalurops', 'Alkaphrah', 'Alkarab', 'Alkes', 'Almaaz', 'Almach', 'Alnair', 'Alnasl', 'Alnilam', 'Alnitak', 'Alniyat', 'Alphard', 'Alphecca', 'Alpheratz', 'Alpherg', 'Alrakis', 'Alrescha', 'Alruba', 'Alsafi', 'Alsciaukat', 'Alsephina', 'Alshain', 'Alshat', 'Altair', 'Altais', 'Alterf', 'Aludra', 'Alula Australis', 'Alula Borealis', 'Alya', 'Alzirr', 'Amadioha', 'Amansinaya', 'Anadolu', 'Ancha', 'Angetenar', 'Aniara', 'Ankaa', 'Anser', 'Antares', 'Antinous', 'Arcalís', 'Arcturus', 'Arkab Posterior', 'Arkab Prior', 'Arneb', 'Ascella', 'Asellus Australis', 'Asellus Borealis', 'Ashlesha', 'Aspidiske', 'Asterope', 'Atakoraka', 'Athebyne', 'Atik', 'Atlas', 'Atria', 'Avior', 'Axólotl', 'Ayeyarwady', 'Azelfafage', 'Azha', 'Azmidi', 'Añañuca', 'Baekdu', 'Bake-eo', "Barnard's Star", 'Baten Kaitos', 'Batsũ̀', 'Beemim', 'Beid', 'Belel', 'Bellatrix', 'Berehynia', 'Betelgeuse', 'Bharani', 'Bibhā', 'Biham', 'Bodu', 'Bosona', 'Botein', 'Brachium', 'Bubup', 'Buna', 'Bunda', 'Bélénos', 'Canopus', 'Capella', 'Caph', 'Castor', 'Castula', 'Cebalrai', 'Ceibo', 'Celaeno', 'Cervantes', 'Chalawan', 'Chamukuy', 'Chaophraya', 'Chara', 'Chasoň', 'Chechia', 'Chertan', 'Citadelle', 'Citalá', 'Cocibolca', 'Copernicus', 'Cor Caroli', 'Cujam', 'Cursa', 'Dabih', 'Dalim', 'Danfeng', 'Deltoton', 'Deneb', 'Deneb Algedi', 'Denebola', 'Diadem', 'Dilmun', 'Dingolay', 'Diphda', 'Diya', 'Dofida', 'Dombay', 'Dschubba', 'Dubhe', 'Dziban', 'Dìwö', 'Ebla', 'Edasich', 'Electra', 'Elgafar', 'Elkurud', 'Elnath', 'Eltanin', 'Emiw', 'Enif', 'Errai', 'Fafnir', 'Fang', 'Fawaris', 'Felis', 'Felixvarela', 'Filetdor', 'Flegetonte', 'Fomalhaut', 'Formosa', 'Franz', 'Fulu', 'Fumalsamakah', 'Funi', 'Furud', 'Fuyue', 'Gacrux', 'Gakyid', 'Gar', 'Garnet Star', 'Geminga', 'Giausar', 'Gienah', 'Ginan', 'Gloas', 'Gnomon', 'Gomeisa', 'Grumium', 'Guahayona', 'Gudja', 'Gumala', 'Guniibuu', 'Hadar', 'Haedus', 'Hamal', 'Hassaleh', 'Hatysa', 'Helvetios', 'Heng', 'Heze', 'Hoerikwaggo', 'Hoggar', 'Homam', 'Honores', 'Horna', 'Hunahpú', 'Hunor', 'Iklil', 'Illyrian', 'Imai', 'Inquill', 'Intan', 'Intercrus', 'Irena', 'Itonda', 'Izar', 'Jabbah', 'Jishui', 'Kaewkosin', 'Kaffaljidhma', 'Kaffalmusalsala', 'Kalausi', 'Kamuy', 'Kang', 'Karaka', 'Kaus Australis', 'Kaus Borealis', 'Kaus Media', 'Kaveh', 'Keid', 'Khambalia', 'Kitalpha', 'Kochab', 'Koeia', 'Koit', 'Komondor', 'Kornephoros', 'Kosjenka', 'Kraz', 'Kui', 'Kulou', 'Kurhah', 'La Superba', 'Lang-exster', 'Larawag', 'Leepwal', 'Lerna', 'Lesath', 'Libertas', 'Lich', 'Liesma', 'Lilii Borea', 'Lionrock', 'Lucilinburhuc', 'Lusitânia', 'Maasym', 'Macondo', 'Mago', 'Mahasim', 'Mahsati', 'Maia', 'Malmok', 'Marfik', 'Markab', 'Markeb', 'Marsic', 'Maru', 'Matar', 'Matza', 'Mazaalai', 'Mebsuta', 'Megrez', 'Meissa', 'Mekbuda', 'Meleph', 'Menkalinan', 'Menkar', 'Menkent', 'Menkib', 'Merak', 'Merga', 'Meridiana', 'Merope', 'Mesarthim', 'Miaplacidus', 'Mimosa', 'Minchir', 'Minelauva', 'Mintaka', 'Mira', 'Mirach', 'Miram', 'Mirfak', 'Mirzam', 'Misam', 'Mizar', 'Moldoveanu', 'Montuno', 'Morava', 'Moriah', 'Mothallah', 'Mouhoun', 'Mpingo', 'Muliphein', 'Muphrid', 'Muscida', 'Musica', 'Muspelheim', 'Márohu', 'Mönch', 'Nahn', 'Naledi', 'Naos', 'Nashira', 'Natasha', 'Nekkar', 'Nembus', 'Nenque', 'Nervia', 'Nganurganity', 'Nihal', 'Nikawiy', 'Noquisi', 'Nosaxa', 'Nunki', 'Nusakan', 'Nushagak', 'Nyamien', 'Násti', 'Ogma', 'Okab', 'Orkaria', 'Paikauhale', 'Paradys', 'Parumleo', 'Peacock', 'Petra', 'Phact', 'Phecda', 'Pherkad', 'Phoenicia', 'Phyllon Kissinou', 'Piautos', 'Pincoya', 'Pipirima', 'Pipit', 'Pipoltr', 'Pleione', 'Poerava', 'Polaris', 'Polaris Australis', 'Polis', 'Pollux', 'Porrima', 'Praecipua', 'Prima Hyadum', 'Procyon', 'Propus', 'Proxima Centauri', 'Quadrans', 'Ramus', 'Ran', 'Rana', 'Rapeto', 'Rasalas', 'Rasalgethi', 'Rasalhague', 'Rasalnaqa', 'Rastaban', 'Regulus', 'Revati', 'Rhombus', 'Rigel', 'Rigil Kentaurus', 'Rosalíadecastro', 'Rotanev', 'Ruchbah', 'Rukbat', 'Sabik', 'Saclateni', 'Sadachbia', 'Sadalbari', 'Sadalmelik', 'Sadalsuud', 'Sadr', 'Safina', 'Sagarmatha', 'Saiph', 'Salm', 'Sansuna', 'Sargas', 'Sarin', 'Sceptrum', 'Scheat', 'Schedar', 'Secunda Hyadum', 'Segin', 'Seginus', 'Sham', 'Shama', 'Shaomin', 'Sharjah', 'Shaula', 'Sheliak', 'Sheratan', 'Shimu', 'Sika', 'Sirius', 'Situla', 'Skat', 'Solaris', 'Solitaire', 'Spica', 'Stellio', 'Sterrennacht', 'Stribor', 'Sualocin', 'Subra', 'Suhail', 'Sulafat', 'Syrma', 'Sāmaya', 'Tabit', 'Taika', 'Taiyangshou', 'Taiyi', 'Talitha', 'Tangra', 'Tania Australis', 'Tania Borealis', 'Tapecue', 'Tarazed', 'Tarf', 'Taygeta', 'Tegmine', 'Tejat', 'Tengshe', 'Terebellum', 'Tevel', 'Theemin', 'Thuban', 'Tiaki', 'Tianfu', 'Tianguan', 'Tianyi', 'Timir', 'Tislit', 'Titawin', 'Tojil', 'Toliman', 'Tonatiuh', 'Torcular', 'Tuiren', 'Tupi', 'Tupã', 'Tureis', 'Tusizuo', 'Udkadua', 'Ukdah', 'Uklun', 'Unukalhai', 'Uridim', 'Uruk', 'Uúba', 'Vega', 'Veritate', 'Vindemiatrix', 'Wasat', 'Wattle', 'Wazn', 'Wezen', 'Wouri', 'Wurren', 'Xami', 'Xamidimura', 'Xihe', 'Xuange', 'Yed Posterior', 'Yed Prior', 'Yildun', 'Yunü', 'Zaniah', 'Zaurak', 'Zavijava', 'Zembra', 'Zhang', 'Zhou', 'Zibal', 'Zosma', 'Zubenelgenubi', 'Zubenelhakrabi', 'Zubeneschamali'
</details>

**Declination with Precession:**
```python
star_chart_spherical_projection.plot_position(star="Vega",
                            added_star=None,
                            start_year_since_2000=-15000,
                            end_year_since_2000=15000,
                            is_precession=True,
                            increment=5,
                            dec_ra="D")
```
![plot_star_declination_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/plot_star_vega_declination_with_precession.png) 
**Declination without Precession:**
```python
star_chart_spherical_projection.plot_position(star="Vega",
                            added_star=None,
                            start_year_since_2000=-15000,
                            end_year_since_2000=15000,
                            is_precession=False,
                            increment=5,
                            dec_ra="D")
```
![plot_star_declination_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/plot_star_vega_declination_without_precession.png) 
**Right Ascension with Precession:**
```python
star_chart_spherical_projection.plot_position(star="Vega",
                            added_star=None,
                            start_year_since_2000=-15000,
                            end_year_since_2000=15000,
                            is_precession=True,
                            increment=5,
                            dec_ra="R")
```
![plot_star_RA_with_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/plot_star_vega_right_ascension_with_precession.png) 
**Right Ascension without Precession:**
```python
star_chart_spherical_projection.plot_position(star="Vega",
                            added_star=None,
                            start_year_since_2000=-15000,
                            end_year_since_2000=15000,
                            is_precession=False,
                            increment=5,
                            dec_ra="R")
```
![plot_star_RA_without_precession+png](https://raw.githubusercontent.com/cyschneck/Star-Chart-Spherical-Projection/main/star_chart_spherical_projection/pytests/examples/plot_star_vega_right_ascension_without_precession.png) 

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

## Beta :test_tube: Features

These features are not included in pip install because they are still experimental and being tested/debugged. For more information and getting them up and running, contact cyschneck@gmail.com or post a question as a [Github Issue](https://github.com/cyschneck/Star-Chart-Spherical-Projection/issues)
- Plot stars in a constellation/asterism with connected lines

## Bibliography

Precession model: [Vondrák, J., et al. “New Precession Expressions, Valid for Long Time Intervals.” Astronomy &amp; Astrophysics, vol. 534, 2011](https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf)

Precession code adapted to Python 3+ from [the Vondrak long term precession model Github repo 'vondrak'](https://github.com/dreamalligator/vondrak)

## Bug and Feature Request

Submit a bug fix, question, or feature request as a [Github Issue](https://github.com/cyschneck/Star-Chart-Spherical-Projection/issues) or to cyschneck@gmail.com
