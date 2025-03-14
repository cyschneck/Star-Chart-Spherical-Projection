########################################################################
# Generate a star chart centered on the poles:
#		Northern Hemsiphere = 90°
#		Southern Hemsiphere = -90°
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

		# convert RA from degrees to radians
		ra_in_degrees = ra_total * 15
		ra_in_radians = np.deg2rad(ra_in_degrees)
		star[1] = ra_in_radians
	return star_list

def convertRadianstoRAhr(ra_in_radians):
	# change star in radians to RA in hours
	ra_in_degree = np.rad2deg(ra_in_radians)

	if ra_in_degree > 360 or ra_in_degree < 0: # lock degrees between 0 and 360, if negative, re-write as a positive degree
		ra_in_degree %= 360

	hours = int(ra_in_degree / 15)
	minutes = int(((ra_in_degree / 15) - hours) * 60) # measured in minutes
	seconds = round(((((ra_in_degree / 15) - hours) * 60) - minutes) * 60) # measured in seconds

	# RA in hours 'HH.MM.SS'
	if hours < 10: hours = '0' + str(hours) # convert 6 to 06
	if minutes < 10: minutes = '0' + str(minutes) # convert 6 to 06
	if seconds < 10: seconds = '0' + str(seconds) # convert 6 to 06
	ra_in_hours = f"{hours}.{minutes}.{seconds}"
	return ra_in_hours

def calculateRAandDeclinationViaProperMotion(years_since_2000, star_ra, star_dec, star_pm_speed, star_pm_angle):
	# Calculate the RA and Declination of a star based on changes due to Proper Motion
	# returns calculated RA and Declination

	logger.debug(f"Proper Motion for {years_since_2000} Years")
	logger.debug(f"Date {years_since_2000}, RA = {star_ra}, Dec = {star_dec}, PM Speed = {star_pm_speed}, PM Angle = {star_pm_angle}")

	star_pm_speed_degrees = 0.00000027777776630942 * star_pm_speed # convert mas/yr to degrees/yr
	star_pm_speed_radains = np.deg2rad(star_pm_speed_degrees) # radains/yr
	star_movement_radains_per_year = star_pm_speed_radains * years_since_2000
	logger.debug(f"Movement Over Time = {star_movement_radains_per_year} (rad), {star_movement_radains_per_year} (deg)")

	ra_x_difference_component = star_movement_radains_per_year * math.cos(np.deg2rad(star_pm_angle))
	dec_y_difference_component = star_movement_radains_per_year * math.sin(np.deg2rad(star_pm_angle))
	logger.debug(f"(RA)  x Difference = {ra_x_difference_component} (rad) = {np.rad2deg(ra_x_difference_component)} degrees"))
	logger.debug(f"(DEC) y Difference = {dec_y_difference_component} (rad) = {np.rad2deg(dec_y_difference_component)} degrees")

	star_adjusted_ra = star_ra + ra_x_difference_component # in radians with proper motion (potentionally will be flipped 180 based on new declination)
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

def precessionVondrak(star_name, star_ra, star_dec, year_YYYY_since_2000):
	# Temporary fix for vondrak plugin (will only find a smaller subsections of the stars)
	logger.debug("INCLUDING PRECESSION VIA VONDRAK")
	vondrak_dec, vondrak_ra = vondrakDreamalligator(star_name, star_ra, np.deg2rad(star_dec), 2000 + year_YYYY_since_2000)
	vondrak_dec = np.rad2deg(vondrak_dec)
	logger.debug(f"Precession for Star = {star_name}, Declination = {vondrak_dec}, RA = {vondrak_ra}")
	return vondrak_dec, vondrak_ra

def generateStereographicProjection(starList=None, 
									northOrSouth=None, 
									yearSince2000=None,
									isPrecessionIncluded=None,
									maxMagnitudeFilter=None,
									declination_min=None,
									declination_max=None):
	# Generate sterographic projections and return declination and right ascension

	# Convert Star chart from RA hours to Radians to chart
	list_of_stars = convertRAhrtoRadians(starList)

	finalPositionOfStarsDict = {} # {'Star Name': {"Declination" : Declination (int), "RA": RA (str)}
	x_star_labels = []
	x_ra_values = []
	y_dec_values = []
	for star in list_of_stars:
		if maxMagnitudeFilter is None or star[5] < maxMagnitudeFilter: # Optional: Filter out stars with a magnitude greater than maxMagnitudeFilter
			logger.debug(f"Star = '{star[0]}'")

			radius_of_circle = star_chart_spherical_projection.calculateRadiusOfCircle(declination_min, northOrSouth)

			# Calculate position of star due to PROPER MOTION (changes RA and Declination over time)
			logger.debug(f"'{star[0]}' original RA = {np.rad2deg(star[1])} and Declination = {star[2]}")
			star_ra, star_declination = calculateRAandDeclinationViaProperMotion(yearSince2000, 
																				star[1], 
																				star[2], 
																				star[3], 
																				star[4])
			logger.debug(f"Adjusted: {star[1]} RA (radians) = {star_ra}")
			logger.debug(f"Adjusted via Proper Motion: '{star[1]}': {star[2]} Declination (degrees) = {star_declination} ")

			# Optional: Calculate new position of star due to PRECESSION (change RA and Declination over time)
			# Vondrak accurate up  +/- 200K years around 2000
			if isPrecessionIncluded:
				star_declination, star_ra = precessionVondrak(star[0], star_ra, star_declination, yearSince2000)
				logger.debug(f"Precession: {star_ra} RA (radians)\nPrecession: Declination (degrees) = {star_declination}")

				# convert degree to position on radius
				dec_ruler_position = star_chart_spherical_projection.calculateLength(star_declination, radius_of_circle, northOrSouth) 

				logger.debug(f"{star[0]}: {star_declination} declination = {dec_ruler_position:.4f} cm")

				in_range_value = False # Determine if within range of South/North Hemisphere
				if star_declination > declination_min and star_declination < declination_max: # only display stars within range of declination values
					in_range_value = True # North
				if star_declination < declination_min and star_declination > declination_max: # only display stars within range of declination values
					in_range_value = True # South

				if in_range_value:
					finalPositionOfStarsDict[star[0]] = {"Declination" : star_declination, "RA": convertRadianstoRAhr(star_ra)} # {'Star Name': {"Declination" : Declination (int), "RA": RA (str)}
					x_star_labels.append(star[0])
					x_ra_values.append(star_ra)
					y_dec_values.append(dec_ruler_position)
					logger.debug(f"Original: '{star[0]}': {np.rad2deg(star[1])} RA (degrees) and {star[2]} Declination (degrees)")
			if not isPrecessionIncluded:
				dec_ruler_position = star_chart_spherical_projection.calculateLength(star_declination, radius_of_circle, northOrSouth) # convert degree to position on radius

				logger.debug(f"{star[0]}: {star_declination} declination = {dec_ruler_position:.4f} cm")
				in_range_value = False # Determine if within range of South/North Hemisphere
				if star_declination > declination_min and star_declination < declination_max: # only display stars within range of declination values
					in_range_value = True # North
				if star_declination < declination_min and star_declination > declination_max: # only display stars within range of declination values
					in_range_value = True # South

				if in_range_value:
					finalPositionOfStarsDict[star[0]] = {"Declination" : star_declination, "RA": convertRadianstoRAhr(star_ra)} # {'Star Name': {"Declination" : Declination (int), "RA": RA (str)}
					x_star_labels.append(star[0])
					x_ra_values.append(star_ra)
					y_dec_values.append(dec_ruler_position)
					logger.debug(f"Original: '{star[0]}': {np.rad2deg(star[1])} RA (degrees) and {star[2]} Declination (degrees)")

	return x_star_labels, x_ra_values, y_dec_values, finalPositionOfStarsDict

def plotStereographicProjection(builtInStars=[], 
								northOrSouth=None, 
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
								save_plot_name=None):

	# Catch errors in given arguments before plotting and set default constants
	star_chart_spherical_projection.errorHandling(isPlotFunction=True,
												builtInStars=builtInStars,
												northOrSouth=northOrSouth, 
												declination_min=declination_min,
												yearSince2000=yearSince2000,
												displayStarNamesLabels=displayStarNamesLabels,
												displayDeclinationNumbers=displayDeclinationNumbers,
												incrementBy=incrementBy, 
												isPrecessionIncluded=isPrecessionIncluded,
												maxMagnitudeFilter=maxMagnitudeFilter,
												userDefinedStars=userDefinedStars,
												onlyDisplayUserStars=onlyDisplayUserStars,
												showPlot=showPlot,
												fig_plot_title=fig_plot_title,
												fig_plot_color=fig_plot_color,
												figsize_n=figsize_n,
												figsize_dpi=figsize_dpi,
												save_plot_name=save_plot_name)
	northOrSouth = northOrSouth.capitalize()
	if not onlyDisplayUserStars:
		builtInStars = [x.title() for x in builtInStars] # convert all names to capitalized
		listOfStars = getStarList(builtInStars)
		for star_object in userDefinedStars:
			star_row = [star_object.starName,
						star_object.ra,
						star_object.dec,
						star_object.properMotionSpeed,
						star_object.properMotionAngle,
						star_object.magnitudeVisual]
			listOfStars.append(star_row)
	else:
		listOfStars = []
		for star_object in userDefinedStars:
			star_row = [star_object.starName,
						star_object.ra,
						star_object.dec,
						star_object.properMotionSpeed,
						star_object.properMotionAngle,
						star_object.magnitudeVisual]
			listOfStars.append(star_row)

	# plot star chart as a circular graph

	# Set declination based on hemisphere selected
	if declination_min is None:
		if northOrSouth == "North": declination_min = northern_declination_min
		if northOrSouth == "South": declination_min = southern_declination_min
	if northOrSouth == "North": declination_max = northern_declination_max
	if northOrSouth == "South": declination_max = southern_declination_max

	# Polar plot figure
	fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
	ax = fig.subplots(subplot_kw={'projection': 'polar'})

	# Set Declination (astronomical 'latitude') as Y (radius of polar plot)

	# Split up chart into North/South hemisphere
	declination_values = np.arange(declination_min, declination_max+1, incrementBy) # +1 to show max value in range

	# Store the ruler positions based on degrees and the ratio of the ruler
	ruler_position_dict = star_chart_spherical_projection.calculateRuler(declination_min,
																		declination_max,
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
			ruler_declination_labels = [f"{deg}°" for deg in ruler_declination_labels]
			plt.yticks(ruler_declination_position, fontsize=7)
			ax.set_yticklabels(ruler_declination_labels)
			ax.set_rlabel_position(120) # declination labels position
		else:
			plt.yticks(ruler_declination_position, fontsize=0) # do not display axis
			ax.set_yticklabels(ruler_declination_labels)
			ax.set_rlabel_position(120) # declination labels position

	# Display declination lines based on hemisphere
	if northOrSouth == "North":
		displayDeclinationMarksOnAxis(declination_values, northern_declination_min, northern_declination_max, False)
	if northOrSouth == "South":
		displayDeclinationMarksOnAxis(declination_values, southern_declination_min, southern_declination_max, True)

	logger.debug(f"\n{northOrSouth}ern Range of Declination: {declination_min} to {declination_max}")

	# convert to x and y values for stars
	x_star_labels, x_ra_values, y_dec_values, star_dict = generateStereographicProjection(starList=listOfStars, 
																						northOrSouth=northOrSouth, 
																						yearSince2000=yearSince2000,
																						isPrecessionIncluded=isPrecessionIncluded,
																						maxMagnitudeFilter=maxMagnitudeFilter,
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
	if displayStarNamesLabels:
		for i, txt in enumerate(x_star_labels):
			ax.annotate(txt, (x_ra_values[i], y_dec_values[i]), 
						horizontalalignment='center', verticalalignment='bottom', 
						fontsize=8)
	for i, txt in enumerate(x_star_labels):
		logger.debug(f"{txt}: {np.rad2deg(x_ra_values[i]):05f} RA (degrees) and {y_dec_values[i]:05f} Declination (ruler)")
		output_string = "Proper Motion"
		logger.debug(f"{output_string} for {yearSince2000} Years\n")

	ax.scatter(x_ra_values, y_dec_values, s=10, c=fig_plot_color)

	# Set Default Figure Title based on variables used in calculation
	years_for_title = yearSince2000
	suffix = ""
	if 1000 <  abs(years_for_title) and abs(years_for_title) < 1000000:
		years_for_title = years_for_title / 1000
		suffix = "K"
	if abs(years_for_title) > 1000000:
		years_for_title = years_for_title / 1000000
		suffix = "M"
	if yearSince2000 >= -2000: year_bce_ce = f"{yearSince2000 + 2000} C.E" # positive years for C.E
	if yearSince2000 < -2000: year_bce_ce = f"{abs(yearSince2000 + 2000)} B.C.E" # negative years for B.C.E
	figure_has_precession_extra_string = "with Precession" if isPrecessionIncluded else "without Precession"

	if fig_plot_title is None: # by default sets title of plot
		ax.set_title(f"{northOrSouth}ern Hemisphere [{years_for_title}{suffix} Years Since 2000 ({year_bce_ce})]: {declination_max}° to {declination_min}° {figure_has_precession_extra_string}")
	else:
		ax.set_title(fig_plot_title)

	# Optional: Save plot with user-defined name/location
	if save_plot_name is not None: 
		fig.savefig(save_plot_name)

	# Optional: Show the plot when it has been calculated
	if showPlot:
		plt.show()
	elseS:
		plt.close()
