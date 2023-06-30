########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import configparser
import csv
import logging
import numpy as np
import os
import pandas as pd

import star_chart_spherical_projection

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def errorHandling(isPlotFunction=None,
				builtInStars=None,
				northOrSouth=None, 
				yearSince2000=None,
				isPrecessionIncluded=None,
				declination_max=None,
				declination_min=None,
				maxMagnitudeFilter=None,
				userDefinedStars=None,
				onlyDisplayUserStars=None,
				displayStarNamesLabels=None,
				displayDeclinationNumbers=None,
				incrementBy=None,
				showPlot=None,
				fig_plot_title=None,
				fig_plot_color=None,
				figsize_n=None,
				figsize_dpi=None,
				save_plot_name=None):
	# Error Handling for Variables shared beween finalPositionOfStars() and plotStereographicProjection() (defined by isPlotFunction)

	# Ensure that star list is a list
	if type(builtInStars) != list:
		logger.critical("\nCRITICAL ERROR, [builtInStars]: Must be a list, current type = '{0}'".format(type(builtInStars)))
		exit()
	## Check that user list has stars that are found in current list
	if len(builtInStars) != 0:
		builtInStars = [x.title() for x in builtInStars] # convert all names to capitalized
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		all_star_names_in_csv = list(star_dataframe['Star Name'])
		for star_given in builtInStars:
			if star_given not in all_star_names_in_csv:
				logger.critical("\nCRITICAL ERROR, [builtInStars]: '{0}' not a star in current list of stars, please select one of the following: {1}".format(star_given, all_star_names_in_csv))
				exit()

	# Ensure that declination ranges are set and within within ranges
	if declination_min is not None:
		if type(declination_min) != int and type(declination_min) != float:
			logger.critical("\nCRITICAL ERROR, [declination_min]: Must be a int or float, current type = '{0}'".format(type(declination_min)))
			exit()
		if declination_min not in np.arange(-89, 90): # if defined, but not in range
			logger.critical("\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{0}'".format(declination_min))
			exit()

	# Ensure if a year is selected it is a float or int, set by default to 0 (the year = 2000)
	if type(yearSince2000) != int and type(yearSince2000) != float:
		logger.critical("\nCRITICAL ERROR, [yearSince2000]: Must be a int or float, current type = '{0}'".format(type(yearSince2000)))
		exit()

	# Ensure that precession options are booleans ["True", "False"]
	if type(isPrecessionIncluded) != bool:
		logger.critical("\nCRITICAL ERROR, [isPrecessionIncluded]: Must be a bool, current type = '{0}'".format(type(isPrecessionIncluded)))
		exit()

	if type(userDefinedStars) != list:
		logger.critical("\nCRITICAL ERROR, [userDefinedStars]: Must be a list, current type = '{0}'".format(type(userDefinedStars)))
		exit()
	for user_star in userDefinedStars:
		if type(user_star) != star_chart_spherical_projection.newStar:
			logger.critical("\nCRITICAL ERROR, [userDefinedStars]: {0} is not a valid newStar object (see: star_chart_spherical_projection.newStar)".format(type(user_star)))
			exit()

	if type(onlyDisplayUserStars) != bool:
		logger.critical("\nCRITICAL ERROR, [onlyDisplayUserStars]: Must be a bool, current type = '{0}'".format(type(onlyDisplayUserStars)))
		exit()

	# Error Handling for finalPositionOfStars() function
	if not isPlotFunction:
		# Ensure that declination ranges are set and within within ranges
		if declination_max is not None:
			if type(declination_max) != int and type(declination_max) != float:
				logger.critical("\nCRITICAL ERROR, [declination_max]: Must be a int or float, current type = '{0}'".format(type(declination_max)))
				exit()
			if declination_max not in np.arange(-89, 90): # if defined, but not in range
				logger.critical("\nCRITICAL ERROR, [declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{0}'".format(declination_max))
				exit()

	# Error Handling for plotStereographicProjection() function
	if isPlotFunction:
		# Ensure that Hemisphere selected are within options
		if type(northOrSouth) != str:
			logger.critical("\nCRITICAL ERROR, [northOrSouth]: Must be a str, current type = '{0}'".format(type(northOrSouth)))
			exit()
		else:
			if northOrSouth not in ["North", "South"]:
				logger.critical("\nCRITICAL ERROR, [northOrSouth]: Hemisphere options are ['North', 'South'], current option = '{0}'".format(northOrSouth))
				exit()

		# Ensure that maxMagnitudeFilter options is a float, set by default to None
		if maxMagnitudeFilter is not None:
			if type(maxMagnitudeFilter) != int and type(maxMagnitudeFilter) != float:
				logger.critical("\nCRITICAL ERROR, [maxMagnitudeFilter]: Must be a int or float, current type = '{0}'".format(type(maxMagnitudeFilter)))
				exit()

		# Ensure that the display options for star names and declination numbers are booleans ["True", "False"]
		if type(displayStarNamesLabels) != bool:
			logger.critical("\nCRITICAL ERROR, [displayStarNamesLabels]: Must be a bool, current type = '{0}'".format(type(displayStarNamesLabels)))
			exit()

		if type(displayDeclinationNumbers) != bool:
			logger.critical("\nCRITICAL ERROR, [displayDeclinationNumbers]: Must be a bool, current type = '{0}'".format(type(displayDeclinationNumbers)))
			exit()

		# Ensure that increment options are 1, 5, 10
		if type(incrementBy) != int:
			logger.critical("\nCRITICAL ERROR, [incrementBy]: Must be a int, current type = '{0}'".format(type(incrementBy)))
			exit()
		if incrementBy not in [1, 5, 10]:
			logger.critical("\nCRITICAL ERROR, [incrementBy]: Must be one of the options [1, 5, 10], current value = '{0}'".format(incrementBy))
			exit()

		# Ensure that the only options for showPlot are booleans ["True", "False"]
		if type(showPlot) != bool:
			logger.critical("\nCRITICAL ERROR, [showPlot]: Must be a bool, current type = '{0}'".format(type(showPlot)))
			exit()

		# Ensure that the color given is a string (matplotlib has error checking for invalid color options)
		if type(fig_plot_color) != str:
			logger.critical("\nCRITICAL ERROR, [fig_plot_color]: Must be a string, current type = '{0}'".format(type(fig_plot_color)))
			exit()

		# Ensure that the user defined title of the plot is a string
		if fig_plot_title is not None and type(fig_plot_title) != str:
			logger.critical("\nCRITICAL ERROR, [fig_plot_title]: Must be a string, current type = '{0}'".format(type(fig_plot_title)))
			exit()

		# Ensure that figure options are integers or floats
		if type(figsize_n) != int and type(figsize_n) != float:
			logger.critical("\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(type(figsize_n)))
			exit()
		if type(figsize_dpi) != int and type(figsize_dpi) != float:
			logger.critical("\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(type(figsize_dpi)))
			exit()

		# Ensure that the user defined figure saved name is a string
		if save_plot_name is not None and type(save_plot_name) != str:
			logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a string, current type = '{0}'".format(type(save_plot_name)))
			exit()

def errorHandlingStarClass(starName=None,
						ra=None,
						dec=None,
						properMotionSpeed=None,
						properMotionAngle=None,
						properMotionSpeedRA=None,
						properMotionSpeedDec=None,
						magnitudeVisual=None):
	
	if starName is None:
		logger.critical("\nCRITICAL ERROR, [starName]: starName is required")
		exit()
	else:
		if type(starName) != str:
			logger.critical("\nCRITICAL ERROR, [starName]: Must be a str, current type = '{0}'".format(type(starName)))
			exit()

	if ra is None:
		logger.critical("\nCRITICAL ERROR, [ra]: Right Ascension is required")
		exit()
	else:
		if type(ra) != str:
			logger.critical("\nCRITICAL ERROR, [ra]: Must be a str, current type = '{0}'".format(type(ra)))
			exit()
		ra_items = ra.split('.')
		if len(ra_items) != 3:
			logger.critical("\nCRITICAL ERROR, [ra]: Right Ascension must be three parts '[HH, MM, SS]' (Hours, Minutes, Seconds), currently  = '{0}'".format(ra_items))
			exit()
		for ra_time in ra_items:
			if not ra_time.isdigit():
				logger.critical("\nCRITICAL ERROR, [ra]: Each part of the Right Ascension must be an integar, '{0}' current type = {1}".format(ra_time, type(ra_time)))
				exit()

	if dec is None:
		logger.critical("\nCRITICAL ERROR, [dec]: Declination is required")
		exit()
	else:
		if type(dec) != int and type(dec) != float:
			logger.critical("\nCRITICAL ERROR, [dec]: Must be a int or float, current type = '{0}'".format(type(dec)))
			exit()

	if properMotionSpeed is not None:
		if type(properMotionSpeed) != int and type(properMotionSpeed) != float:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeed]: Must be a int or float, current type = '{0}'".format(type(properMotionSpeed)))
			exit()

	if properMotionAngle is not None:
		if type(properMotionAngle) != int and type(properMotionAngle) != float:
			logger.critical("\nCRITICAL ERROR, [properMotionAngle]: Must be a int or float, current type = '{0}'".format(type(properMotionAngle)))
			exit()

	if properMotionSpeedRA is not None:
		if type(properMotionSpeedRA) != int and type(properMotionSpeedRA) != float:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedRA]: Must be a int or float, current type = '{0}'".format(type(properMotionSpeedRA)))
			exit()

	if properMotionSpeedDec is not None:
		if type(properMotionSpeedDec) != int and type(properMotionSpeedDec) != float:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedDec]: Must be a int or float, current type = '{0}'".format(type(properMotionSpeedDec)))
			exit()

	# Verify at least one pair is set
	if properMotionSpeedRA is None and properMotionSpeedDec is None:
		# Neither pairs are set
		if properMotionSpeed is None and properMotionAngle is None:
			logger.critical("\nCRITICAL ERROR, Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required")
			exit()

	# Verify when only one value is set, make sure to set up its pair
	if properMotionSpeedRA is not None:
		if properMotionSpeedDec is None and properMotionSpeed is None and properMotionAngle is None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedDec]: With properMotionSpeedRA set, properMotionSpeedDec is required")
			exit()
	if properMotionSpeedDec is not None:
		if properMotionSpeedRA is None and properMotionSpeed is None and properMotionAngle is None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedRA]: With properMotionSpeedDec set, properMotionSpeedRA is required")
			exit()
	if properMotionSpeed is not None:
		if properMotionSpeedRA is None and properMotionSpeedDec is None and properMotionAngle is None:
			logger.critical("\nCRITICAL ERROR, [properMotionAngle]: With properMotionSpeed set, properMotionAngle is required")
			exit()
	if properMotionAngle is not None:
		if properMotionSpeedRA is None and properMotionSpeedDec is None and properMotionSpeed is None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeed]: With properMotionAngle set, properMotionSpeed is required")
			exit()

	# Remove the invalid extra options when properMotionSpeed/properMotionAngle should be the only pair set
	if properMotionSpeed is not None and properMotionAngle is not None:
		if properMotionSpeedRA is not None and properMotionSpeedDec is not None:
			logger.critical("\nCRITICAL ERROR, Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required, not both")
			exit()
		if properMotionSpeedRA is not None and properMotionSpeedDec is None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedRA]: With properMotionSpeed/properMotionAngle set, properMotionSpeedRA should be None")
			exit()
		if properMotionSpeedRA is None and properMotionSpeedDec is not None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeedDec]: With properMotionSpeed/properMotionAngle set, properMotionSpeedDec should be None")
			exit()

	# Remove the invalid extra options when properMotionSpeedRA/properMotionSpeedDec should be the only pair set
	if properMotionSpeedRA is not None and properMotionSpeedDec is not None:
		if properMotionSpeed is None and properMotionAngle is not None:
			logger.critical("\nCRITICAL ERROR, [properMotionAngle]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionAngle should be None")
			exit()
		if properMotionSpeed is not None and properMotionAngle is None:
			logger.critical("\nCRITICAL ERROR, [properMotionSpeed]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionSpeed should be None")
			exit()

	# Verify the non-None values are the correct pairs: properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle
	if properMotionSpeed is None and properMotionSpeedDec is None:
		if properMotionSpeedRA is not None and properMotionAngle is not None:
			logger.critical("\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedRA")
			exit()
	if properMotionSpeed is None and properMotionSpeedRA is None:
		if properMotionAngle is not None and properMotionSpeedDec is not None:
			logger.critical("\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedDec")
			exit()
	if properMotionAngle is None and properMotionSpeedRA is None:
		if properMotionSpeed is not None and properMotionSpeedDec is not None:
			logger.critical("\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedDec")
			exit()
	if properMotionAngle is None and properMotionSpeedDec is None:
		if properMotionSpeed is not None and properMotionSpeedRA is not None:
			logger.critical("\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedRA")
			exit()


	if magnitudeVisual is None:
		logger.critical("\nCRITICAL ERROR, [magnitudeVisual]: magnitudeVisual is required")
		exit()
	else:
		if type(magnitudeVisual) != int and type(magnitudeVisual) != float:
			logger.critical("\nCRITICAL ERROR, [magnitudeVisual]: Must be a int or float, current type = '{0}'".format(type(magnitudeVisual)))
			exit()
