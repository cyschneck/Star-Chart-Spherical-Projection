########################################################################
# Return the calculated position of Stars
########################################################################
import logging
import os
from datetime import datetime

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
                    userDefinedStars=[],
                    onlyDisplayUserStars=False,
                    declination_min=None,
                    declination_max=None,
                    save_to_csv=None):
    # return the final position of the stars as a dictionary

    star_chart_spherical_projection.errorHandling(isPlotFunction=False,
                                                included_stars=included_stars,
                                                year_since_2000=year_since_2000,
                                                is_precession=is_precession,
                                                userDefinedStars=userDefinedStars,
                                                onlyDisplayUserStars=onlyDisplayUserStars,
                                                declination_min=declination_min,
                                                declination_max=declination_max,
                                                save_to_csv=save_to_csv)

    if not onlyDisplayUserStars:
        included_stars = [x.title() for x in included_stars] # convert all names to capitalized
        listOfStars = star_chart_spherical_projection._get_stars(included_stars)
        for star_object in userDefinedStars:
            star_row = [star_object.star_name,
                        star_object.ra,
                        star_object.dec,
                        star_object.pm_speed,
                        star_object.pm_angle,
                        star_object.magnitude]
            listOfStars.append(star_row)
    else:
        listOfStars = []
        for star_object in userDefinedStars:
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

def position_over_time(builtInStarName=None,
                        newStar=None,
                        startYearSince2000=None,
                        endYearSince2000=None,
                        incrementYear=5,
                        is_precession=True,
                        save_to_csv=None):

    if builtInStarName is not None:
        star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
        star_dataframe = pd.read_csv(star_csv_file)
        star_data = star_dataframe.loc[star_dataframe["Common Name"] == builtInStarName].values.flatten().tolist()
        star_name, star_ra, star_declination, star_mag, star_pm_speed, star_pm_angle, star_pm_ra, star_pm_dec, star_alt_names, star_url = star_data
    if newStar is not None:
        star_name = newStar.star_name
        star_ra = newStar.ra
        star_declination = newStar.dec
        star_pm_speed = newStar.pm_speed
        star_pm_angle = newStar.pm_angle
        star_mag = newStar.magnitude

    years_to_calculate = np.arange(startYearSince2000, endYearSince2000+1, incrementYear).tolist()
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

def plot_position(builtInStarName=None, 
                newStar=None,
                startYearSince2000=None,
                endYearSince2000=None,
                incrementYear=10,
                is_precession=True,
                DecOrRA="D",
                show_plot=True,
                showYearMarker=True,
                fig_plot_title=None,
                fig_plot_color="C0",
                figsize_n=12,
                figsize_dpi=100,
                save_plot_name=None):

    position_over_time_dict = position_over_time(builtInStarName=builtInStarName,
                                                newStar=newStar,
                                                startYearSince2000=startYearSince2000,
                                                endYearSince2000=endYearSince2000,
                                                incrementYear=incrementYear,
                                                is_precession=is_precession)

    if builtInStarName is not None:
        star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
        star_dataframe = pd.read_csv(star_csv_file)
        star_data = star_dataframe.loc[star_dataframe["Common Name"] == builtInStarName].values.flatten().tolist()
        star_name = star_data[0]
    if newStar is not None:
        star_name = newStar.star_name
    
    fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
    ax = fig.subplots()

    year_lst = []
    dec_lst = []
    ra_radians_lst = []
    for year, position_dict in position_over_time_dict.items():
        year_lst.append(year)
        dec_lst.append(position_dict["Dec (degrees)"])
        ra_radians_lst.append(position_dict["RA (radians)"])

    if DecOrRA == "D":
        plot_y = dec_lst
        title = "Declination"
        y_label = "Declination (°)"
    if DecOrRA == "R":
        plot_y = ra_radians_lst
        title = "Right Ascension"
        y_label = "Right Ascension (Radians)"

    if is_precession:
        precession_label = "(With Precession)"
    else:
        precession_label = "(Without Precession)"

    # prevent the axis from populate more than 70 elements (to prevent overlapping)
    x_increment = incrementYear
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
    
    plt.title(f"{star_name}'s {title} {precession_label} from {startYear_bce_ce} to {endYear_bce_ce}, Every {incrementYear} Years")
    plt.plot(year_lst, plot_y)
    plt.xlabel("Year")
    plt.ylabel(y_label)
    
    ax.set_xticks(np.arange(year_lst[0], year_lst[-1]+1, x_increment))
    ax.set_yticks(np.linspace(min(plot_y), max(plot_y), y_increment))

    if showYearMarker:
        current_year = datetime.now().year
        plt.axvline(current_year, linewidth=0.5, color="black", linestyle="dashed")
    plt.xticks(rotation=90)

    if show_plot:
        plt.show()

    if save_plot_name is not None:
        fig.savefig(save_plot_name, dpi=fig.dpi)

def predict_pole_star(year_since_2000=0, pole="North"):
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

    # Find the closest star in builtin stars
    closest_pole_star = None
    closest_pole_declination = None
    for star, star_data in final_position_builtin_stars.items():
        if closest_pole_star is None:
            closest_pole_star = star
            closest_pole_declination = star_data["Declination"]
        else:
            if abs(float(star_data["Declination"]) - pole_declination) < abs(closest_pole_declination - pole_declination):
                closest_pole_star = star
                closest_pole_declination = star_data["Declination"]
    
    return closest_pole_star
