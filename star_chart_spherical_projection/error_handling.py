########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import csv
import numpy as np
import os
import pandas as pd

import star_chart_spherical_projection

def errorHandling(isPlotFunction=None,
                included_stars=None,
                pole=None, 
                year_since_2000=None,
                is_precession=None,
                declination_max=None,
                declination_min=None,
                max_magnitude=None,
                added_stars=None,
                only_added_stars=None,
                display_labels=None,
                display_dec=None,
                increment=None,
                show_plot=None,
                fig_plot_title=None,
                fig_plot_color=None,
                figsize_n=None,
                figsize_dpi=None,
                save_plot_name=None,
                save_to_csv=None):
    # Error Handling for Variables shared between final_position() and plot_stereographic_projection() (defined by isPlotFunction)

    # Ensure that star list is a list
    if type(included_stars) != list:
        raise ValueError(f"[included_stars]: Must be a list, current type = '{type(included_stars)}'")

    ## Check that user list has stars that are found in current list
    if len(included_stars) != 0:
        all_common_names = [name[0] for name in star_chart_spherical_projection._get_stars()]
        for star_given in included_stars:
            if star_given.lower() not in [x.lower() for x in all_common_names]: # convert all stars to lower case:
                raise ValueError(f"[included_stars]: '{star_given}' not a star in current list of stars, please select one of the following: {all_common_names}")

    # Ensure that declination ranges are set and within within ranges
    if declination_min is not None:
        if type(declination_min) != int and type(declination_min) != float:
            raise ValueError(f"[declination_min]: Must be a int or float, current type = '{type(declination_min)}'")
        if declination_min not in np.arange(-89, 90): # if defined, but not in range
            raise ValueError(f"[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{declination_min}'")

    # Ensure if a year is selected it is a float or int, set by default to 0 (the year = 2000)
    if type(year_since_2000) != int and type(year_since_2000) != float:
        raise ValueError(f"[year_since_2000]: Must be a int or float, current type = '{type(year_since_2000)}'")

    # Ensure that precession options are booleans ["True", "False"]
    if type(is_precession) != bool:
        raise ValueError(f"[is_precession]: Must be a bool, current type = '{type(is_precession)}'")

    if type(added_stars) != list:
        raise ValueError(f"[added_stars]: Must be a list, current type = '{type(added_stars)}'")
    for user_star in added_stars:
        if type(user_star) != star_chart_spherical_projection.add_new_star:
            raise ValueError(f"[added_stars]: {type(user_star)} is not a valid new star object (see: star_chart_spherical_projection.add_new_star)")

    if type(only_added_stars) != bool:
        raise ValueError(f"[only_added_stars]: Must be a bool, current type = '{type(only_added_stars)}'")

    # Error Handling for final_position() function
    if not isPlotFunction:
        # Ensure that declination ranges are set and within within ranges
        if declination_max is not None:
            if type(declination_max) != int and type(declination_max) != float:
                raise ValueError(f"[declination_max]: Must be a int or float, current type = '{type(declination_max)}'")
            if declination_max not in np.arange(-89, 90): # if defined, but not in range
                raise ValueError(f"[declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{declination_max}'")
        if save_to_csv is not None:
            if type(save_to_csv) != str:
                raise ValueError(f"[save_to_csv]: Must be a str, current type = '{type(save_to_csv)}'")
            if not save_to_csv.lower().endswith(".csv"):
                raise ValueError(f"[save_to_csv]: Extension must be a .csv file, current extension = '{save_to_csv.split('.')[1]}'")

    # Error Handling for plot_stereographic_projection() function
    if isPlotFunction:
        # Ensure that Pole selected are within options
        if type(pole) != str:
            raise ValueError(f"[pole]: Must be a str, current type = '{type(pole)}'")
        else:
            if pole not in ["North", "South"]:
                raise ValueError(f"[pole]: Pole options are ['North', 'South'], current option = '{pole}'")

        # Ensure that max_magnitude options is a float, set by default to None
        if max_magnitude is not None:
            if type(max_magnitude) != int and type(max_magnitude) != float:
                raise ValueError(f"[max_magnitude]: Must be a int or float, current type = '{type(max_magnitude)}'")

        # Ensure that the display options for star names and declination numbers are booleans ["True", "False"]
        if type(display_labels) != bool:
            raise ValueError(f"[display_labels]: Must be a bool, current type = '{type(display_labels)}'")

        if type(display_dec) != bool:
            raise ValueError(f"[display_dec]: Must be a bool, current type = '{type(display_dec)}'")

        # Ensure that increment options are 1, 5, 10
        if type(increment) != int:
            raise ValueError(f"[increment]: Must be a int, current type = '{type(increment)}'")
        if increment not in [1, 5, 10]:
            raise ValueError(f"[increment]: Must be one of the options [1, 5, 10], current value = '{increment}'")

        # Ensure that the only options for show_plot are booleans ["True", "False"]
        if type(show_plot) != bool:
            raise ValueError(f"[show_plot]: Must be a bool, current type = '{type(show_plot)}'")

        # Ensure that the color given is a string (matplotlib has error checking for invalid color options)
        if type(fig_plot_color) != str:
            raise ValueError(f"[fig_plot_color]: Must be a string, current type = '{type(fig_plot_color)}'")

        # Ensure that the user defined title of the plot is a string
        if fig_plot_title is not None and type(fig_plot_title) != str:
            raise ValueError(f"[fig_plot_title]: Must be a string, current type = '{type(fig_plot_title)}'")

        # Ensure that figure options are integers or floats
        if type(figsize_n) != int and type(figsize_n) != float:
            raise ValueError(f"[figsize_n]: Must be a int or float, current type = '{type(figsize_n)}'")
        if type(figsize_dpi) != int and type(figsize_dpi) != float:
            raise ValueError(f"[figsize_dpi]: Must be a int or float, current type = '{type(figsize_dpi)}'")

        # Ensure that the user defined figure saved name is a string
        if save_plot_name is not None and type(save_plot_name) != str:
            raise ValueError(f"[save_plot_name]: Must be a string, current type = '{type(save_plot_name)}'")

def errorHandlingStarClass(star_name=None,
                        ra=None,
                        dec=None,
                        pm_speed=None,
                        pm_angle=None,
                        pm_speed_ra=None,
                        pm_speed_dec=None,
                        magnitude=None):
    
    if star_name is None:
        raise ValueError("[star_name]: star_name is required")
    else:
        if type(star_name) != str:
            raise ValueError(f"[star_name]: Must be a str, current type = '{type(star_name)}'")

    if ra is None:
        raise ValueError("[ra]: Right Ascension is required")
    else:
        if type(ra) != str:
            raise ValueError(f"[ra]: Must be a str, current type = '{type(ra)}'")
        ra_items = ra.split('.')
        if len(ra_items) != 3:
            raise ValueError(f"[ra]: Right Ascension must be three parts '[HH, MM, SS]' (Hours, Minutes, Seconds), currently  = '{ra_items}'")
        for ra_time in ra_items:
            if not ra_time.isdigit():
                raise ValueError(f"[ra]: Each part of the Right Ascension must be an integer, '{ra_time}' current type = {type(ra_time)}")

    if dec is None:
        raise ValueError("[dec]: Declination is required")
    else:
        if type(dec) != int and type(dec) != float:
            raise ValueError(f"[dec]: Must be a int or float, current type = '{type(dec)}'")

    if pm_speed is not None:
        if type(pm_speed) != int and type(pm_speed) != float:
            raise ValueError(f"[pm_speed]: Must be a int or float, current type = '{type(pm_speed)}'")

    if pm_angle is not None:
        if type(pm_angle) != int and type(pm_angle) != float:
            raise ValueError(f"[pm_angle]: Must be a int or float, current type = '{type(pm_angle)}'")

    if pm_speed_ra is not None:
        if type(pm_speed_ra) != int and type(pm_speed_ra) != float:
            raise ValueError(f"[pm_speed_ra]: Must be a int or float, current type = '{type(pm_speed_ra)}'")

    if pm_speed_dec is not None:
        if type(pm_speed_dec) != int and type(pm_speed_dec) != float:
            raise ValueError(f"[pm_speed_dec]: Must be a int or float, current type = '{type(pm_speed_dec)}'")

    # Verify at least one pair is set
    if pm_speed_ra is None and pm_speed_dec is None:
        # Neither pairs are set
        if pm_speed is None and pm_angle is None:
            raise ValueError("Either pm_speed_ra/pm_speed_dec or pm_speed/pm_angle is required")

    # Verify when only one value is set, make sure to set up its pair
    if pm_speed_ra is not None:
        if pm_speed_dec is None and pm_speed is None and pm_angle is None:
            raise ValueError("[pm_speed_dec]: With pm_speed_ra set, pm_speed_dec is required")

    if pm_speed_dec is not None:
        if pm_speed_ra is None and pm_speed is None and pm_angle is None:
            raise ValueError("[pm_speed_ra]: With pm_speed_dec set, pm_speed_ra is required")
    if pm_speed is not None:
        if pm_speed_ra is None and pm_speed_dec is None and pm_angle is None:
            raise ValueError("[pm_angle]: With pm_speed set, pm_angle is required")
    if pm_angle is not None:
        if pm_speed_ra is None and pm_speed_dec is None and pm_speed is None:
            raise ValueError("[pm_speed]: With pm_angle set, pm_speed is required")

    # Remove the invalid extra options when pm_speed/pm_angle should be the only pair set
    if pm_speed is not None and pm_angle is not None:
        if pm_speed_ra is not None and pm_speed_dec is not None:
            raise ValueError("Either pm_speed_ra/pm_speed_dec or pm_speed/pm_angle is required, not both")
        if pm_speed_ra is not None and pm_speed_dec is None:
            raise ValueError("[pm_speed_ra]: With pm_speed/pm_angle set, pm_speed_ra should be None")
        if pm_speed_ra is None and pm_speed_dec is not None:
            raise ValueError("[pm_speed_dec]: With pm_speed/pm_angle set, pm_speed_dec should be None")

    # Remove the invalid extra options when pm_speed_ra/pm_speed_dec should be the only pair set
    if pm_speed_ra is not None and pm_speed_dec is not None:
        if pm_speed is None and pm_angle is not None:
            raise ValueError("[pm_angle]: With pm_speed_ra/pm_speed_dec set, pm_angle should be None")
        if pm_speed is not None and pm_angle is None:
            raise ValueError("[pm_speed]: With pm_speed_ra/pm_speed_dec set, pm_speed should be None")

    # Verify the non-None values are the correct pairs: pm_speed_ra/pm_speed_dec or pm_speed/pm_angle
    if pm_speed is None and pm_speed_dec is None:
        if pm_speed_ra is not None and pm_angle is not None:
            raise ValueError("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_angle/pm_speed_ra")
    if pm_speed is None and pm_speed_ra is None:
        if pm_angle is not None and pm_speed_dec is not None:
            raise ValueError("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_angle/pm_speed_dec")
    if pm_angle is None and pm_speed_ra is None:
        if pm_speed is not None and pm_speed_dec is not None:
            raise ValueError("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_speed/pm_speed_dec")
    if pm_angle is None and pm_speed_dec is None:
        if pm_speed is not None and pm_speed_ra is not None:
            raise ValueError("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_speed/pm_speed_ra")

    if magnitude is None:
        raise ValueError("[magnitude]: magnitude is required")
    else:
        if type(magnitude) != int and type(magnitude) != float:
            raise ValueError(f"[magnitude]: Must be a int or float, current type = '{type(magnitude)}'")

def errorHandlingPredictPoleStar(year_since_2000=None, pole=None):
    # Error Handling for predict_pole_star()
    if year_since_2000 is None:
        raise ValueError("[year_since_2000]: year_since_2000 is required")
    else:
        if type(year_since_2000) != int and type(year_since_2000) != float:
            raise ValueError(f"[year_since_2000]: Must be a int or float, current type = '{type(year_since_2000)}'")
    
    if pole is not None:
        if type(pole) != str:
            raise ValueError(f"[pole]: Must be a str, current type = '{type(pole)}'")
        else:
            if pole.title() not in ["North", "South"]:
                raise ValueError(f"[pole]: Must be a 'North' or 'South', currently = '{pole}'")
