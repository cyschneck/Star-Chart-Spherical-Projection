########################################################################
# Generate a star chart centered on the poles:
#		Northern Hemsiphere = 90°
#		Southern Hemsiphere = -90°
########################################################################
import configparser
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
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Start Year (JP2000)
j2000 = 2000 # start year of the star catalogue (jan 1 2000 via IAU)

def getStarList(selectStars=[]):
	# generate a star object
	# selectStars only returns a subset of all the stars saved, empty will return all in the star_data.csv file
	# stars: ["name", "RA: HH.MM.SS", Declination DD.SS, Proper Motion Speed (mas/yr), Proper Motion Angle (DD.SS), Magnitude (V, Visual)]
	star_data_list = []
	star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
	star_dataframe = pd.read_csv(star_csv_file)
	for index, row in star_dataframe.iterrows():
		if len(selectStars) > 0: # get only a subset of all stars
			if row["Star Name"] in selectStars:
				star_data_list.append(row.tolist())
		else:
			star_data_list.append(row.tolist())
	return star_data_list

def convertRAhrtoRadians(star_list):
	# change first element in the list object [RA, dec]
	for star in star_list:
		ra_in_hr = star[1]
		# convert RA from hours to degrees
		ra_hr, ra_min, ra_sec = list(map(int, ra_in_hr.split('.')))
		ra_min /= 60
		ra_sec /= 3600
		ra_total = ra_hr + ra_min + ra_sec
		ra_in_degrees = ra_total * 15

		# convert RA from degrees to radians
		ra_in_radians = np.deg2rad(ra_in_degrees)
		star[1] = ra_in_radians
	return star_list

def calculateRAandDeclinationViaProperMotion(years_since_2000, star_ra, star_dec, star_pm_speed, star_pm_angle):
	# Calculate the RA and Declination of a star based on changes due to Proper Motion
	# returns calculated RA and Declination

	logger.debug("Proper Motion for {0} Years".format(years_since_2000))
	logger.debug("Date {0}, RA = {1}, Dec = {2}, PM Speed = {3}, PM Angle = {4}".format(years_since_2000, star_ra, star_dec, star_pm_speed, star_pm_angle))

	star_pm_speed_degrees = 0.00000027777776630942 * star_pm_speed # convert mas/yr to degrees/yr
	star_pm_speed_radains = np.deg2rad(star_pm_speed_degrees) # radains/yr
	star_movement_radains_per_year = star_pm_speed_radains * years_since_2000
	logger.debug("Movement Over Time = {0} (rad), {1} (deg)".format(star_movement_radains_per_year, np.rad2deg(star_movement_radains_per_year)))

	ra_x_difference_component = star_movement_radains_per_year * math.cos(np.deg2rad(star_pm_angle))
	dec_y_difference_component = star_movement_radains_per_year * math.sin(np.deg2rad(star_pm_angle))
	logger.debug("(RA)  x Difference = {0} (rad) = {1} degrees".format(ra_x_difference_component, np.rad2deg(ra_x_difference_component)))
	logger.debug("(DEC) y Difference = {0} (rad) = {1} degrees".format(dec_y_difference_component, np.rad2deg(dec_y_difference_component)))

	star_adjusted_ra = star_ra + ra_x_difference_component # in radians with proper motion (potentionally will be flipped 180 based on new declination)
	star_adjusted_declination = star_dec + np.rad2deg(dec_y_difference_component) # in degrees new with proper motion

	dec_x = star_adjusted_declination
	# remap within -90 and 90 for postive declinations
	if star_adjusted_declination > 0: # Postive declinations
		dec_x = star_adjusted_declination % 360
		# map from 0 to 90 (postive declinations)
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
		# map from 0 to 90 (postive declinations)
		if dec_x >= -270 and dec_x <= -180:
			dec_x = 180 + dec_x
			dec_x = abs(dec_x)
		if dec_x > -360 and dec_x < -270:
			dec_x = 90 + (dec_x + 270)
	logger.debug("New mapped dec = {0}".format(dec_x))
	logger.debug("Original Dec = {0}, New Dec = {1}".format(star_dec, star_adjusted_declination))

	# flip over RA by rotating 180
	is_flipped_across_pole = False
	star_over_ninety_ra = star_adjusted_declination
	if star_over_ninety_ra >= 0: # postive declinations
		while (star_over_ninety_ra > 90):
			star_over_ninety_ra -= 90
			is_flipped_across_pole = not is_flipped_across_pole # flip across the center by 180
	if star_over_ninety_ra < 0: # negative declinations
		while (star_over_ninety_ra < -90):
			star_over_ninety_ra += 90
			is_flipped_across_pole = not is_flipped_across_pole # flip across the center by 180
	logger.debug("Original RA = {0}, New RA = {1}, Flipped = {2} (if true +180?)".format(np.rad2deg(star_ra), np.rad2deg(star_adjusted_ra), is_flipped_across_pole))

	# If declination goes over ninety, flip over by 180
	if is_flipped_across_pole:
		star_adjusted_ra = star_adjusted_ra + np.deg2rad(180)

	star_adjusted_declination = dec_x
	logger.debug("Final RA: {0} degrees".format(np.rad2deg(star_adjusted_ra)))
	logger.debug("Final Dec: {0} degrees ".format(star_adjusted_declination))
	return star_adjusted_ra, star_adjusted_declination

def plotStarChart(userListOfStars=[], 
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
				save_plot_name=None):
	# plot star chart as a circular graph
	list_of_stars = getStarList(userListOfStars)

	# Convert Star chart from RA hours to Radians to chart
	list_of_stars = convertRAhrtoRadians(list_of_stars)

	# Catch errors in given arguments before plotting and set default constants
	star_chart_spherical_projection.errorHandling(userListOfStars, 
													northOrSouth, 
													declination_min,
													yearSince2000,
													displayStarNamesLabels,
													displayDeclinationNumbers,
													incrementBy, 
													fig_plot_title,
													fig_plot_color,
													figsize_n,
													figsize_dpi,
													save_plot_name)
	northOrSouth = northOrSouth.capitalize()

	# Set max declination based on hemisphere selected
	if declination_min is None:
		if northOrSouth == "North": declination_min = int(config["declinationDefaultValues"]["northern_declination_min"])
		if northOrSouth == "South": declination_min = int(config["declinationDefaultValues"]["southern_declination_min"])
	if northOrSouth == "North": declination_max = int(config["declinationDefaultValues"]["northern_declination_max"])
	if northOrSouth == "South": declination_max = int(config["declinationDefaultValues"]["southern_declination_max"])

	logger.debug("userListOfStars = {0}".format(userListOfStars))
	logger.debug("northOrSouth = {0}".format(northOrSouth))
	logger.debug("declination_min = {0}".format(declination_min))
	logger.debug("declination_max = {0}".format(declination_max))
	logger.debug("yearSince2000 = {0}".format(yearSince2000))
	logger.debug("displayStarNamesLabels = {0}".format(displayStarNamesLabels))
	logger.debug("displayDeclinationNumbers = {0}".format(displayDeclinationNumbers))
	logger.debug("displayDeclinationNumbers = {0}".format(displayDeclinationNumbers))
	logger.debug("incrementBy = {0}".format(incrementBy))
	logger.debug("fig_plot_title = {0}".format(fig_plot_title))
	logger.debug("fig_plot_color = {0}".format(fig_plot_color))
	logger.debug("figsize_n = {0}".format(figsize_n))
	logger.debug("figsize_dpi = {0}".format(figsize_dpi))
	logger.debug("save_plot_name = {0}".format(save_plot_name))

	fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
	ax = fig.subplots(subplot_kw={'projection': 'polar'})

	# Set Declination (astronomical 'latitude') as Y (radius of polar plot)

	# Split up chart into North/South hemisphere
	declination_values = np.arange(declination_min, declination_max+1, incrementBy) # +1 to show max value in range
	min_dec_value = declination_min
	max_dec_value = declination_max

	# Store the ruler positions based on degrees and the ratio of the ruler
	ruler_position_dict = star_chart_spherical_projection.calculateRuler(min_dec_value,
																		max_dec_value,
																		incrementBy, 
																		northOrSouth)

	# Display declination lines on the chart from -min to +max
	def displayDeclinationMarksOnAxis(declination_values, dec_min, dec_max, isInverted):
		# set declination marks based on the ruler to space out lines
		ruler_declination_position = list(ruler_position_dict.values())
		ruler_declination_labels = list(ruler_position_dict.keys())
		both_label_values = [list(x) for x in zip(ruler_declination_position, ruler_declination_labels)] # for testing
		ax.set_ylim(0, max(ruler_declination_position))

		# Display Axis
		if displayDeclinationNumbers:
			ruler_declination_labels = ["{0}°".format(deg) for deg in ruler_declination_labels]
			plt.yticks(ruler_declination_position, fontsize=7)
			ax.set_yticklabels(ruler_declination_labels)
			ax.set_rlabel_position(120) # declination labels position
		else:
			plt.yticks(ruler_declination_position, fontsize=0) # do not display axis
			ax.set_yticklabels(ruler_declination_labels)
			ax.set_rlabel_position(120) # declination labels position

	# Display declination lines based on hemisphere
	if northOrSouth == "North":
		displayDeclinationMarksOnAxis(declination_values, int(config["declinationDefaultValues"]["northern_declination_min"]), int(config["declinationDefaultValues"]["northern_declination_max"]), False)
	if northOrSouth == "South":
		displayDeclinationMarksOnAxis(declination_values, int(config["declinationDefaultValues"]["southern_declination_min"]), int(config["declinationDefaultValues"]["southern_declination_max"]), True)

	logger.debug("\n{0}ern Range of Declination: {1} to {2}".format(northOrSouth, min_dec_value, max_dec_value))

	radius_of_circle = star_chart_spherical_projection.calculateRadiusOfCircle(declination_min, northOrSouth)

	# convert to x and y values for stars
	x_star_labels = []
	x_ra_values = []
	y_dec_values = []
	for star in list_of_stars:
		logger.debug(star[0])

		# Calculate position of star due to PROPER MOTION (changes RA and Declination over time)
		logger.debug("'{0}' original RA = {1} and Declination = {2}".format(star[0], np.rad2deg(star[1]), star[2]))
		star_ra, star_declination = calculateRAandDeclinationViaProperMotion(yearSince2000, 
																			star[1], 
																			star[2], 
																			star[3], 
																			star[4])
		logger.debug("Adjusted: {0} RA (radians) = {1}".format(star[1], star_ra))
		logger.debug("Adjusted via Proper Motion: '{0}': {1} Declination (degrees) = {2} ".format(star[0], star[2], star_declination))

		dec_ruler_position = star_chart_spherical_projection.calculateLength(star_declination, radius_of_circle, northOrSouth) # convert degree to position on radius

		logger.debug("{0}: {1} declination = {2:.4f} cm".format(star[0], star_declination, dec_ruler_position))
		in_range_value = False # Determine if within range of South/North Hemisphere
		if star_declination > min_dec_value and star_declination < max_dec_value: # only display stars within range of declination values
			in_range_value = True # North
		if star_declination < min_dec_value and star_declination > max_dec_value: # only display stars within range of declination values
			in_range_value = True # South

		if in_range_value:
			x_star_labels.append(star[0])
			x_ra_values.append(star_ra)
			y_dec_values.append(dec_ruler_position)
			logger.debug("Original: '{0}': {1} RA (degrees) and {2} Declination (degrees)".format(star[0], np.rad2deg(star[1]), star[2]))

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

	# Label stars (optional)
	if displayStarNamesLabels:
		for i, txt in enumerate(x_star_labels):
			ax.annotate(txt, (x_ra_values[i], y_dec_values[i]), 
						horizontalalignment='center', verticalalignment='bottom', 
						fontsize=8)
	for i, txt in enumerate(x_star_labels):
		logger.debug("{0}: {1:05f} RA (degrees) and {2:05f} Declination (ruler)".format(txt, np.rad2deg(x_ra_values[i]), y_dec_values[i]))
		output_string = "Proper Motion"
		logger.debug("{0} for {1} Years\n".format(output_string, yearSince2000))

	ax.scatter(x_ra_values, y_dec_values, s=10, c=fig_plot_color)
	years_for_title = yearSince2000
	suffix = ""
	if 1000 <  abs(years_for_title) and abs(years_for_title) < 1000000:
		years_for_title = years_for_title / 1000
		suffix = "K"
	if abs(years_for_title) > 1000000:
		years_for_title = years_for_title / 1000000
		suffix = "M"
	if yearSince2000 >= 0: year_bce_ce = "{0} C.E".format(yearSince2000 + 2000) # postive years for C.E
	if yearSince2000 < 0: year_bce_ce = "{0} B.C.E".format(abs(yearSince2000 + 2000)) # negative years for B.C.E

	if fig_plot_title is None: # by default sets title of plot
		ax.set_title("{0}ern Hemisphere [{1}{2} Years Since 2000 ({3})]: {4}° to {5}°".format(northOrSouth,
																								years_for_title,
																								suffix,
																								year_bce_ce,
																								declination_max,
																								declination_min))
	else:
		ax.set_title(fig_plot_title)

	if save_plot_name is not None: 
		fig.savefig(save_plot_name)

	plt.show()
