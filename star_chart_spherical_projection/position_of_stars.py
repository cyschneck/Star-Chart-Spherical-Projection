########################################################################
# Return the calculated position of Stars
########################################################################
import logging
import os
from datetime import datetime
import string

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import star_chart_spherical_projection

## Logging set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def final_position(included_stars=[], 
                    year_since_2000=0,
                    is_precession=True,
                    added_stars=[],
                    only_added_stars=False,
                    declination_min=None,
                    declination_max=None,
                    save_to_csv=None):
    # return the final position of the stars as a dictionary

    star_chart_spherical_projection.errorHandling(isPlotFunction=False,
                                                included_stars=included_stars,
                                                year_since_2000=year_since_2000,
                                                is_precession=is_precession,
                                                added_stars=added_stars,
                                                only_added_stars=only_added_stars,
                                                declination_min=declination_min,
                                                declination_max=declination_max,
                                                save_to_csv=save_to_csv)

    if not only_added_stars:
        # show all stars
        included_stars = [string.capwords(x) for x in included_stars]
        listOfStars = star_chart_spherical_projection._get_stars(included_stars)
        for star_object in added_stars:
            star_row = [star_object.star_name,
                        star_object.ra,
                        star_object.dec,
                        star_object.pm_speed,
                        star_object.pm_angle,
                        star_object.magnitude]
            listOfStars.append(star_row)
    else:
        # show only the user's added stars
        listOfStars = []
        for star_object in added_stars:
            star_row = [star_object.star_name,
                        star_object.ra,
                        star_object.dec,
                        star_object.pm_speed,
                        star_object.pm_angle,
                        star_object.magnitude]
            listOfStars.append(star_row)
    
    # Set declination min values when using the _generate_stereographic_projection() to capture all stars if not set
    declination_min = -90
    declination_max = 90

    _, _, _, finalPositionOfStarsDict = star_chart_spherical_projection._generate_stereographic_projection(starList=listOfStars, 
                                                                                                        pole="North", 
                                                                                                        declination_min=declination_min,
                                                                                                        year_since_2000=year_since_2000,
                                                                                                        is_precession=is_precession,
                                                                                                        max_magnitude=None,
                                                                                                        declination_max=declination_max)
    # Generate a .csv file with final positions of stars
    if save_to_csv is not None:
        header_options = ["Common Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]
        star_chart_list = []
        for star_name, star_position in finalPositionOfStarsDict.items():
            star_chart_list.append([star_name, star_position["RA"], star_position["Declination"]])
        df = pd.DataFrame(star_chart_list, columns=header_options)
        df = df.sort_values(by=["Common Name"])
        df.to_csv(save_to_csv, header=header_options, index=False)

    return finalPositionOfStarsDict

def position_over_time(star=None,
                        added_star=None,
                        start_year_since_2000=None,
                        end_year_since_2000=None,
                        increment=5,
                        is_precession=True,
                        save_to_csv=None):

    if star is not None:
        star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
        star_dataframe = pd.read_csv(star_csv_file)
        star_data = star_dataframe.loc[star_dataframe["Common Name"] == star].values.flatten().tolist()
        star_name, star_ra, star_declination, star_mag, star_pm_speed, star_pm_angle, star_pm_ra, star_pm_dec, star_alt_names, star_url = star_data
    if added_star is not None:
        star_name = added_star.star_name
        star_ra = added_star.ra
        star_declination = added_star.dec
        star_pm_speed = added_star.pm_speed
        star_pm_angle = added_star.pm_angle
        star_mag = added_star.magnitude

    years_to_calculate = np.arange(start_year_since_2000, end_year_since_2000+1, increment).tolist()
    position_over_time = {}
    for year in years_to_calculate:
        star_row = [[star_name, star_ra, star_declination, star_pm_speed, star_pm_angle, star_mag]]
        _, star_radians, _, star_dict = star_chart_spherical_projection._generate_stereographic_projection(starList=star_row, 
                                                                                            year_since_2000=year,
                                                                                            is_precession=is_precession,
                                                                                            pole="North",
                                                                                            declination_min=-90,
                                                                                            declination_max=90)
        
        position_over_time[year+2000] = {"RA (radians)": star_radians[0], 
                                    "RA (hours)" : star_dict[star_name]["RA"], 
                                    "Dec (degrees)" : star_dict[star_name]["Declination"]}
    
    # Generate a .csv file with final positions of the star
    if save_to_csv is not None:
        header_options = ["Year", "Declination (DD.SS)", "Right Ascension (HH.MM.SS)", "Right Ascension (radians)"]
        star_chart_list = []
        for year, star_position in position_over_time.items():
            star_chart_list.append([year, star_position["Dec (degrees)"], star_position["RA (hours)"], star_position["RA (radians)"]])
        df = pd.DataFrame(star_chart_list, columns=header_options)
        df = df.sort_values(by=["Year"])
        df.to_csv(save_to_csv, header=header_options, index=False)

    return position_over_time

def plot_position(star=None, 
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
                save_plot_name=None):

    position_over_time_dict = position_over_time(star=star,
                                                added_star=added_star,
                                                start_year_since_2000=start_year_since_2000,
                                                end_year_since_2000=end_year_since_2000,
                                                increment=increment,
                                                is_precession=is_precession)

    if star is not None:
        star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
        star_dataframe = pd.read_csv(star_csv_file)
        star_data = star_dataframe.loc[star_dataframe["Common Name"] == star].values.flatten().tolist()
        star_name = star_data[0]
    if added_star is not None:
        star_name = added_star.star_name
    
    fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
    ax = fig.subplots()

    year_lst = []
    dec_lst = []
    ra_radians_lst = []
    for year, position_dict in position_over_time_dict.items():
        year_lst.append(year)
        dec_lst.append(position_dict["Dec (degrees)"])
        ra_radians_lst.append(position_dict["RA (radians)"])

    if dec_ra == "D":
        plot_y = dec_lst
        title = "Declination"
        y_label = "Declination (°)"
    if dec_ra == "R":
        plot_y = ra_radians_lst
        title = "Right Ascension"
        y_label = "Right Ascension (Radians)"

    if is_precession:
        precession_label = "(With Precession)"
    else:
        precession_label = "(Without Precession)"

    # prevent the axis from populate more than 70 elements (to prevent overlapping)
    x_increment = increment
    x_plot_len = np.arange(year_lst[0], year_lst[-1]+1, x_increment)
    while len(x_plot_len) > 71:
        x_increment *= 5
        x_plot_len = np.arange(year_lst[0], year_lst[-1]+1, x_increment)
    y_increment = len(plot_y)
    while y_increment > 20:
        y_increment = 20

    if year_lst[0] >= -2000: startYear_bce_ce = f"{year_lst[0]} C.E" # positive years for C.E
    if year_lst[0] < -2000: startYear_bce_ce = f"{abs(year_lst[0])} B.C.E" # negative years for B.C.E
    if year_lst[-1] >= -2000: endYear_bce_ce = f"{year_lst[-1]} C.E" # positive years for C.E
    if year_lst[-1] < -2000: endYear_bce_ce = f"{abs(year_lst[-1])} B.C.E" # negative years for B.C.E
    
    plt.title(f"{star_name}'s {title} {precession_label} from {startYear_bce_ce} to {endYear_bce_ce}, Every {increment} Years")
    plt.plot(year_lst, plot_y)
    plt.xlabel("Year")
    plt.ylabel(y_label)
    
    ax.set_xticks(np.arange(year_lst[0], year_lst[-1]+1, x_increment))
    ax.set_yticks(np.linspace(min(plot_y), max(plot_y), y_increment))

    if display_year_marker:
        current_year = datetime.now().year
        plt.axvline(current_year, linewidth=0.5, color="black", linestyle="dashed")
    plt.xticks(rotation=90)

    if show_plot:
        plt.show()

    if save_plot_name is not None:
        fig.savefig(save_plot_name, dpi=fig.dpi)

def predict_pole_star(year_since_2000=0, pole="North", max_magnitude=None):
    # Find the next North/South Pole Star

    star_chart_spherical_projection.errorHandlingPredictPoleStar(year_since_2000=year_since_2000, pole=pole)
    pole = pole.title()

    final_position_builtin_stars = star_chart_spherical_projection.final_position(year_since_2000=year_since_2000,
                                                                                is_precession=True)
    # Set the pole declination based on either North/South
    if pole == "North":
        pole_declination = 90
    if pole == "South":
        pole_declination = -90
    
    # Collect data to check magnitude of each star
    star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
    star_dataframe = pd.read_csv(star_csv_file)

    # Set max_magnitude to max magnitude in star data if set to None
    if max_magnitude is None:
        max_magnitude = star_dataframe["Magnitude (V, Visual)"].max()

    # Find the closest star in built-in stars
    closest_pole_star = None
    closest_pole_declination = None
    for star, star_data in final_position_builtin_stars.items():
        star_mag = star_dataframe.loc[star_dataframe["Common Name"]==star]["Magnitude (V, Visual)"].values[0]
        if star_mag <= max_magnitude: # filter out stars with magnitudes larger than filter
            if closest_pole_star is None:
                closest_pole_star = star
                closest_pole_declination = star_data["Declination"]
            else:
                if abs(float(star_data["Declination"]) - pole_declination) < abs(closest_pole_declination - pole_declination):
                    closest_pole_star = star
                    closest_pole_declination = star_data["Declination"]
        
    return closest_pole_star
