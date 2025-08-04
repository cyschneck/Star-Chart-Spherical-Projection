########################################################################
# Generate a star chart centered on the poles:
#       Northern Hemisphere = 90°
#       Southern Hemisphere = -90°
########################################################################
import csv
import logging
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

import star_chart_spherical_projection

## Logging set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

## Constants
northern_declination_min = -30
northern_declination_max = 90
southern_declination_min = 30
southern_declination_max = -90

# Start Year (JP2000)
j2000 = 2000 # start year of the star catalogue (jan 1 2000 via IAU)

def _get_stars(selectStars=[]):
    # selectStars only returns a subset of all the stars saved, empty will return all in the star_data.csv file
    # stars: ["name", "RA: HH.MM.SS", Declination DD.SS, Proper Motion Speed (mas/yr), Proper Motion Angle (DD.SS), Magnitude (V, Visual)]
    star_data_list = []
    star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/4_all_stars_data.csv
    star_dataframe = pd.read_csv(star_csv_file)
    for index, row in star_dataframe.iterrows():
        if len(selectStars) > 0: # get only a subset of all stars
            if row["Common Name"] in selectStars:
                star_data_list.append(row.tolist())
        else:
            star_data_list.append(row.tolist())
    return star_data_list

def _ra_to_radians(star_list):
    # convert RA to radians
    for star in star_list:
        # convert RA from hours to degrees
        ra_in_hr = star[1]
        
        ra_hr, ra_min, ra_sec = ra_in_hr.split('.')    
        ra_hr = int(ra_hr)
        ra_min = int(ra_min)
        prec_zero = len(ra_sec)-len(ra_sec.lstrip('0')) # count number of preceding zeroes (for example, 0.00868)
        
        # if seconds have greater than 2 degrees of accuracy (for example: 07.46.519615)
        len_degrees = 0
        if prec_zero >= 30: # account for measuring the length of a number in scientifiic notation
            len_degrees = -1
        len_degrees += len(ra_sec)-prec_zero
        if len_degrees < 0: len_degrees = 0
        second_degrees = 10**(len_degrees + prec_zero) 
        ra_sec = int(ra_sec)
        ra_sec /= second_degrees # divide seconds by a multiple (for example, to convert: 519615 to 51.9615)
        
        # convert minutes and seconds to decimals
        ra_min /= 60
        ra_sec /= 3600
        ra_total = ra_hr + ra_min + ra_sec

        # convert RA from degrees to radians
        ra_in_degrees = ra_total * 15
        ra_in_radians = np.deg2rad(ra_in_degrees)
        star[1] = ra_in_radians
 
    return star_list

def _radians_to_ra(ra_in_radians):
    # change star in radians to RA in hours
    ra_in_degree = np.rad2deg(ra_in_radians)

    if ra_in_degree > 360 or ra_in_degree < 0: # lock degrees between 0 and 360, if negative, re-write as a positive degree
        ra_in_degree %= 360
    
    hours = int(ra_in_degree / 15)
    minutes = int(((ra_in_degree / 15) - hours) * 60) # measured in minutes
    seconds = round(((((ra_in_degree / 15) - hours) * 60) - minutes) * 60, 10) # measured in seconds
    
    precision = len(str(seconds).split(".")[1])
    if precision > 5:
        seconds = f"{seconds:.10f}".rstrip("0") #str(float(f"{seconds:.{precision}}"))# # account for scientific notation (for example, convert 8.68e-05 to 0.0000868)
    else:
        seconds = str(seconds)
    prec_seconds = seconds.split(".")[1]
    if prec_seconds == "": prec_seconds = 0

    # count preceding zeroes
    prec_zero = 0 
    if int(prec_seconds) != 0:
        prec_zero = len(prec_seconds)-len(prec_seconds.lstrip('0')) # count number of preceding zeroes (for example, 0.00868)
    
    # handle edge case to convert "0870314" to "870314" to "8.70314" when value is a long decimal
    is_less_ten = False 
    if float(seconds) < 10: is_less_ten = True
    if not float(seconds).is_integer(): # if float/decimal (for example, 54.47676 becomes 5447676, but 9.0 stays at 9)
        # convert from decimal to whole number while maintaining precession
        seconds = int(str(seconds).replace(".", ""))
    else:
        # convert float of integer to integer (9.0 = 9)
        seconds = int(float(seconds))
    
    # handle edge case if seconds == 60, increment minutes by one
    if seconds == 60:
        minutes += 1
        seconds = 0

    # RA in hours 'HH.MM.SS'
    if hours < 10: hours = '0' + str(hours) # convert 6 to 06
    if minutes < 10: minutes = '0' + str(minutes) # convert 6 to 06
    if (seconds < 10 and seconds > 0) or is_less_ten:
        seconds = ('0'*prec_zero) + str(seconds) # dynamically add zeroes to front of string 
    if seconds == 0:
        seconds = "00" # add trailing zero when exactly 0
    if len(str(seconds)) == 1: # add trailing zero for 1 -> 10
        seconds += "0"

    ra_in_hours = f"{hours}.{minutes}.{seconds}"
    return ra_in_hours

def _ra_dec_via_pm(years_since_2000, star_ra, star_dec, star_pm_speed, star_pm_angle):
    # Calculate the RA and Declination of a star based on changes due to Proper Motion
    # returns calculated RA and Declination

    logger.debug(f"Proper Motion for {years_since_2000} Years")
    logger.debug(f"Date {years_since_2000}, RA = {star_ra}, Dec = {star_dec}, PM Speed = {star_pm_speed}, PM Angle = {star_pm_angle}")

    star_pm_speed_degrees = 0.00000027777776630942 * star_pm_speed # convert mas/yr to degrees/yr
    star_pm_speed_radians = np.deg2rad(star_pm_speed_degrees) # radians/yr
    star_movement_radians_per_year = star_pm_speed_radians * years_since_2000
    logger.debug(f"Movement Over Time = {star_movement_radians_per_year} (rad), {star_movement_radians_per_year} (deg)")

    ra_x_difference_component = star_movement_radians_per_year * math.cos(np.deg2rad(star_pm_angle))
    dec_y_difference_component = star_movement_radians_per_year * math.sin(np.deg2rad(star_pm_angle))
    logger.debug(f"(RA)  x Difference = {ra_x_difference_component} (rad) = {np.rad2deg(ra_x_difference_component)} degrees")
    logger.debug(f"(DEC) y Difference = {dec_y_difference_component} (rad) = {np.rad2deg(dec_y_difference_component)} degrees")

    star_adjusted_ra = star_ra + ra_x_difference_component # in radians with proper motion (potentially  will be flipped 180 based on new declination)
    star_adjusted_declination = star_dec + np.rad2deg(dec_y_difference_component) # in degrees new with proper motion

    dec_x = star_adjusted_declination
    # remap within -90 and 90 for positive declinations
    if star_adjusted_declination > 0: # Positive declinations
        dec_x = star_adjusted_declination % 360
        # map from 0 to 90 (positive declinations)
        if dec_x > 90 and dec_x <= 180: 
            dec_x = 90 + (90 - dec_x)
        # map from 0 to -90 (negative declinations)
        if dec_x <= 270 and dec_x > 180:
            dec_x = 180 - dec_x
        if dec_x < 360 and dec_x > 270:
            dec_x = -90 + (dec_x - 270)
    if star_adjusted_declination < -0: # Negative declinations
        dec_x = star_adjusted_declination % -360
        # map from 0 to -90 (negative declinations)
        if dec_x < -90 and dec_x >= -180: 
            dec_x = -90 - (90 + dec_x)
        # map from 0 to 90 (positive declinations)
        if dec_x >= -270 and dec_x <= -180:
            dec_x = 180 + dec_x
            dec_x = abs(dec_x)
        if dec_x > -360 and dec_x < -270:
            dec_x = 90 + (dec_x + 270)
    logger.debug(f"New mapped dec = {dec_x}")
    logger.debug(f"Original Dec = {star_dec}, New Dec = {star_adjusted_declination}")

    # flip over RA by rotating 180
    is_flipped_across_pole = False
    star_over_ninety_ra = star_adjusted_declination
    if star_over_ninety_ra >= 0: # positive declinations
        while (star_over_ninety_ra > 90):
            star_over_ninety_ra -= 90
            is_flipped_across_pole = not is_flipped_across_pole # flip across the center by 180
    if star_over_ninety_ra < 0: # negative declinations
        while (star_over_ninety_ra < -90):
            star_over_ninety_ra += 90
            is_flipped_across_pole = not is_flipped_across_pole # flip across the center by 180
    logger.debug(f"Original RA = {np.rad2deg(star_ra)}, New RA = {np.rad2deg(star_adjusted_ra)}, Flipped = {is_flipped_across_pole} (if true +180?)")

    # If declination goes over ninety, flip over by 180
    if is_flipped_across_pole:
        star_adjusted_ra = star_adjusted_ra + np.deg2rad(180)

    star_adjusted_declination = dec_x
    logger.debug(f"Final RA: {np.rad2deg(star_adjusted_ra)} degrees")
    logger.debug(f"Final Dec: {star_adjusted_declination} degrees")
    return star_adjusted_ra, star_adjusted_declination

def calculatePositionOfPolePrecession(years_since_2000, original_declination, original_ra):
    # Calculate change in the position of the pole due to precession
    obliquity_for_YYYY = 23.439167
    logger.debug(f"Years Since 2000 = {years_since_2000}")

    # Rate of change of right ascension and declination of a star due to precession
    declination_change_arcseconds_per_year = (19.9 * math.cos(original_ra)) * years_since_2000
    ra_change_arcseconds_per_year = (46.1 * (19.9 * math.sin(original_ra) * math.tan(np.deg2rad(original_declination)))) * years_since_2000

    change_in_declination = declination_change_arcseconds_per_year/3600 # degrees
    change_in_ra = np.deg2rad(ra_change_arcseconds_per_year/3600) # degrees to radians

    final_declination_due_to_precession = original_declination + change_in_declination
    final_ra_due_to_precession = original_ra + change_in_ra

    logger.debug(f"Dec: {original_declination} + {change_in_declination} = {final_declination_due_to_precession}")
    logger.debug(f"RA:  {original_ra} + {change_in_ra} = {final_ra_due_to_precession}")
    return final_ra_due_to_precession, final_declination_due_to_precession

def vondrakDreamalligator(star_name, star_ra_rad, star_dec_rad, year_to_calculate):
    # Modified code from github.com/dreamalligator/vondrak to calculate precession
    def position_matrix(ra=None, dec=None):
        x = math.cos(dec) * math.cos(ra)
        y = math.cos(dec) * math.sin(ra)
        z = math.sin(dec)
        return np.array([[x], [y], [z]])

    def compute_star(compute_ra, compute_dec):
        return position_matrix(ra=compute_ra, dec=compute_dec)

    precession_matrix = star_chart_spherical_projection.ltp_pbmat(year_to_calculate) # Precession matrix for the given year
    p_1 = compute_star(star_ra_rad, star_dec_rad) # compute star's position matrix for given year
    p_1 = star_chart_spherical_projection.pdp(precession_matrix, p_1) # apply precession matrix for given year
    (ra_as_rad, dec_as_rad) = star_chart_spherical_projection.ra_dec(p_1)

    return dec_as_rad, ra_as_rad # new declination and right ascension

def _precession_vondrak(star_name, star_ra, star_dec, year_YYYY_since_2000):
    # Temporary fix for vondrak plugin (will only find a smaller subsections of the stars)
    logger.debug("INCLUDING PRECESSION VIA VONDRAK")
    vondrak_dec, vondrak_ra = vondrakDreamalligator(star_name, star_ra, np.deg2rad(star_dec), 2000 + year_YYYY_since_2000)
    vondrak_dec = np.rad2deg(vondrak_dec)
    logger.debug(f"Precession for Star = {star_name}, Declination = {vondrak_dec}, RA = {vondrak_ra}")
    return vondrak_dec, vondrak_ra

def _generate_stereographic_projection(starList=None, 
                                    pole=None, 
                                    year_since_2000=None,
                                    is_precession=None,
                                    max_magnitude=None,
                                    declination_min=None,
                                    declination_max=None):
    # Generate stereographic projections and return declination and right ascension

    # Convert Star chart from RA hours to Radians to chart
    list_of_stars = _ra_to_radians(starList)

    finalPositionOfStarsDict = {} # {'Common Name': {"Declination" : Declination (float), "RA": RA (str)}
    x_star_labels = []
    x_ra_values = []
    y_dec_values = []
    for star in list_of_stars:
        # [[star_name, star_ra, star_declination, star_pm_speed, star_pm_angle, star_mag]]
        name = star[0]
        ra = star[1]
        dec = star[2]
        pm_speed = float(star[3])
        pm_angle = float(star[4])
        mag = float(star[5])
        if max_magnitude is None or mag < max_magnitude: # Optional: Filter out stars with a magnitude greater than max_magnitude
            logger.debug(f"Star = '{name}'")

            radius_of_circle = star_chart_spherical_projection._calculate_radius_of_circle(declination_min, pole)

            # Calculate position of star due to PROPER MOTION (changes RA and Declination over time)
            logger.debug(f"'{name}' original RA = {np.rad2deg(ra)} and Declination = {dec}")
            star_ra, star_declination = _ra_dec_via_pm(year_since_2000, 
                                                        ra, 
                                                        dec, 
                                                        pm_speed, 
                                                        pm_angle)
            logger.debug(f"Adjusted: {ra} RA (radians) = {star_ra}")
            logger.debug(f"Adjusted via Proper Motion: '{ra}': {dec} Declination (degrees) = {star_declination} ")

            # Optional: Calculate new position of star due to PRECESSION (change RA and Declination over time)
            # Vondrak accurate up  +/- 200K years around 2000
            if is_precession:
                star_declination, star_ra = _precession_vondrak(name, star_ra, star_declination, year_since_2000)
                logger.debug(f"Precession: {star_ra} RA (radians)\nPrecession: Declination (degrees) = {star_declination}")

                # convert degree to position on radius
                dec_ruler_position = star_chart_spherical_projection._calculate_length(star_declination, radius_of_circle, pole) 

                logger.debug(f"{name}: {star_declination} declination = {dec_ruler_position:.4f} cm")

                in_range_value = False # Determine if within range of South/North Hemisphere
                if star_declination > declination_min and star_declination < declination_max: # only display stars within range of declination values
                    in_range_value = True # North
                if star_declination < declination_min and star_declination > declination_max: # only display stars within range of declination values
                    in_range_value = True # South

                if in_range_value:
                    finalPositionOfStarsDict[name] = {"Declination" : float(star_declination), "RA": _radians_to_ra(star_ra)} # {'Common Name': {"Declination" : Declination (int), "RA": RA (str)}
                    x_star_labels.append(name)
                    x_ra_values.append(star_ra)
                    y_dec_values.append(dec_ruler_position)
                    logger.debug(f"Original: '{name}': {np.rad2deg(ra)} RA (degrees) and {dec} Declination (degrees)")
            if not is_precession:
                dec_ruler_position = star_chart_spherical_projection._calculate_length(star_declination, radius_of_circle, pole) # convert degree to position on radius

                logger.debug(f"{name}: {star_declination} declination = {dec_ruler_position:.4f} cm")
                in_range_value = False # Determine if within range of South/North Hemisphere
                if star_declination > declination_min and star_declination < declination_max: # only display stars within range of declination values
                    in_range_value = True # North
                if star_declination < declination_min and star_declination > declination_max: # only display stars within range of declination values
                    in_range_value = True # South

                if in_range_value:
                    finalPositionOfStarsDict[name] = {"Declination" : float(star_declination), "RA": _radians_to_ra(star_ra)} # {'Common Name': {"Declination" : Declination (int), "RA": RA (str)}
                    x_star_labels.append(name)
                    x_ra_values.append(star_ra)
                    y_dec_values.append(dec_ruler_position)
                    logger.debug(f"Original: '{name}': {np.rad2deg(ra)} RA (degrees) and {dec} Declination (degrees)")

    return x_star_labels, x_ra_values, y_dec_values, finalPositionOfStarsDict

def plot_stereographic_projection(included_stars=[], 
                                pole=None, 
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
                                save_plot_name=None):

    # Catch errors in given arguments before plotting and set default constants
    star_chart_spherical_projection.errorHandling(isPlotFunction=True,
                                                included_stars=included_stars,
                                                pole=pole, 
                                                declination_min=declination_min,
                                                year_since_2000=year_since_2000,
                                                display_labels=display_labels,
                                                display_dec=display_dec,
                                                increment=increment, 
                                                is_precession=is_precession,
                                                max_magnitude=max_magnitude,
                                                added_stars=added_stars,
                                                only_added_stars=only_added_stars,
                                                show_plot=show_plot,
                                                fig_plot_title=fig_plot_title,
                                                fig_plot_color=fig_plot_color,
                                                figsize_n=figsize_n,
                                                figsize_dpi=figsize_dpi,
                                                save_plot_name=save_plot_name)
    pole = pole.capitalize()
    listOfStars = []
    if not only_added_stars:
        included_stars = [x.title() for x in included_stars] # convert all names to capitalized
        for star in _get_stars(included_stars):
            listOfStars.append([star[0],
                                star[1],
                                star[2],
                                star[4],
                                star[5],
                                star[3]])
        for star_object in added_stars:
            star_row = [star_object.star_name,
                        star_object.ra,
                        star_object.dec,
                        star_object.pm_speed,
                        star_object.pm_angle,
                        star_object.magnitude]
            listOfStars.append(star_row)
    else:
        listOfStars = []
        for star_object in added_stars:
            star_row = [star_object.star_name,
                        star_object.ra,
                        star_object.dec,
                        star_object.pm_speed,
                        star_object.pm_angle,
                        star_object.magnitude]
            listOfStars.append(star_row)

    # plot star chart as a circular graph

    # Set declination based on hemisphere selected
    if declination_min is None:
        if pole == "North": declination_min = northern_declination_min
        if pole == "South": declination_min = southern_declination_min
    if pole == "North": declination_max = northern_declination_max
    if pole == "South": declination_max = southern_declination_max

    # Polar plot figure
    fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
    ax = fig.subplots(subplot_kw={'projection': 'polar'})

    # Set Declination (astronomical 'latitude') as Y (radius of polar plot)

    # Split up chart into North/South hemisphere
    declination_values = np.arange(declination_min, declination_max+1, increment) # +1 to show max value in range

    # Store the ruler positions based on degrees and the ratio of the ruler
    ruler_position_dict = star_chart_spherical_projection._calculate_ruler(declination_min,
                                                                        declination_max,
                                                                        increment, 
                                                                        pole)

    # Display declination lines on the chart from -min to +max
    def displayDeclinationMarksOnAxis(declination_values, dec_min, dec_max, isInverted):
        # set declination marks based on the ruler to space out lines
        ruler_declination_position = list(ruler_position_dict.values())
        ruler_declination_labels = list(ruler_position_dict.keys())
        both_label_values = [list(x) for x in zip(ruler_declination_position, ruler_declination_labels)] # for testing
        ax.set_ylim(0, max(ruler_declination_position))

        # Display Axis
        if display_dec:
            ruler_declination_labels = [f"{deg}°" for deg in ruler_declination_labels]
            plt.yticks(ruler_declination_position, fontsize=7)
            ax.set_yticklabels(ruler_declination_labels)
            ax.set_rlabel_position(120) # declination labels position
        else:
            plt.yticks(ruler_declination_position, fontsize=0) # do not display axis
            ax.set_yticklabels(ruler_declination_labels)
            ax.set_rlabel_position(120) # declination labels position

    # Display declination lines based on hemisphere
    if pole == "North":
        displayDeclinationMarksOnAxis(declination_values, northern_declination_min, northern_declination_max, False)
    if pole == "South":
        displayDeclinationMarksOnAxis(declination_values, southern_declination_min, southern_declination_max, True)

    logger.debug(f"\n{pole}ern Range of Declination: {declination_min} to {declination_max}")

    # convert to x and y values for stars
    x_star_labels, x_ra_values, y_dec_values, star_dict = _generate_stereographic_projection(starList=listOfStars, 
                                                                                        pole=pole, 
                                                                                        year_since_2000=year_since_2000,
                                                                                        is_precession=is_precession,
                                                                                        max_magnitude=max_magnitude,
                                                                                        declination_min=declination_min,
                                                                                        declination_max=declination_max)

    # Set Right Ascension (astronomical 'longitude') as X (theta of polar plot)
    angles_ra = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150,
                        165, 180, 195, 210, 225, 240, 255, 270, 285, 300,
                        315, 330, 345])
    plt.xticks(angles_ra * np.pi / 180, fontsize=8)
    labels_ra = np.array(['$0^h$','$1^h$','$2^h$','$3^h$', '$4^h$','$5^h$',
                        '$6^h$','$7^h$', '$8^h$','$9^h$', '$10^h$',
                        '$11^h$','$12^h$','$13^h$','$14^h$','$15^h$',
                        '$16^h$','$17^h$','$18^h$','$19^h$','$20^h$', 
                        '$21^h$', '$22^h$','$23^h$'])
    ax.set_xticklabels(labels_ra, fontsize=10)

    # Optional: Label the stars with names
    if display_labels:
        for i, txt in enumerate(x_star_labels):
            ax.annotate(txt, (x_ra_values[i], y_dec_values[i]), 
                        horizontalalignment='center', verticalalignment='bottom', 
                        fontsize=8)
    for i, txt in enumerate(x_star_labels):
        logger.debug(f"{txt}: {np.rad2deg(x_ra_values[i]):05f} RA (degrees) and {y_dec_values[i]:05f} Declination (ruler)")
        output_string = "Proper Motion"
        logger.debug(f"{output_string} for {year_since_2000} Years\n")

    ax.scatter(x_ra_values, y_dec_values, s=10, c=fig_plot_color)

    # Set Default Figure Title based on variables used in calculation
    years_for_title = year_since_2000
    suffix = ""
    if 1000 <  abs(years_for_title) and abs(years_for_title) < 1000000:
        years_for_title = years_for_title / 1000
        suffix = "K"
    if abs(years_for_title) > 1000000:
        years_for_title = years_for_title / 1000000
        suffix = "M"
    if year_since_2000 >= -2000: year_bce_ce = f"{year_since_2000 + 2000} C.E" # positive years for C.E
    if year_since_2000 < -2000: year_bce_ce = f"{abs(year_since_2000 + 2000)} B.C.E" # negative years for B.C.E
    figure_has_precession_extra_string = "with Precession" if is_precession else "without Precession"

    if fig_plot_title is None: # by default sets title of plot
        ax.set_title(f"{pole}ern Hemisphere [{years_for_title}{suffix} Years Since 2000 ({year_bce_ce})]: {declination_max}° to {declination_min}° {figure_has_precession_extra_string}")
    else:
        ax.set_title(fig_plot_title)

    # Optional: Save plot with user-defined name/location
    if save_plot_name is not None: 
        fig.savefig(save_plot_name)

    # Optional: Show the plot when it has been calculated
    if show_plot:
        plt.show()
    else:
        plt.close()
