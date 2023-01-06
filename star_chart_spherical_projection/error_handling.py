########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import configparser
import csv
import logging
import numpy as np
import os
import pandas as pd

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def errorHandling(isPlotFunction=None,
				userListOfStars=None,
				northOrSouth=None, 
				yearSince2000=None,
				isPrecessionIncluded=None,
				declination_max=None,
				declination_min=None,
				maxMagnitudeFilter=None,
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
	if type(userListOfStars) != list:
		logger.critical("\nCRITICAL ERROR, [userListOfStars]: Must be a list, current type = '{0}'".format(type(userListOfStars)))
		exit()
	## Check that user list has stars that are found in current list
	if len(userListOfStars) != 0:
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		all_star_names_in_csv = list(star_dataframe['Star Name'])
		for star_given in userListOfStars:
			if star_given not in all_star_names_in_csv:
				logger.critical("\nCRITICAL ERROR, [userListOfStars]: '{0}' not a star in current list of stars, please select one of the following: {1}".format(star_given, all_star_names_in_csv))
				exit()
	logger.debug("userListOfStars = '{0}'".format(userListOfStars))

	# Ensure if a year is selected it is a float or int, set by default to 0 (the year = 2000)
	if type(yearSince2000) != int and type(yearSince2000) != float:
		logger.critical("\nCRITICAL ERROR, [yearSince2000]: Must be a int or float, current type = '{0}'".format(type(yearSince2000)))
		exit()
	logger.debug("yearSince2000 = '{0}'".format(yearSince2000))

	# Ensure that precession options are booleans ["True", "False"]
	if type(isPrecessionIncluded) != bool:
		logger.critical("\nCRITICAL ERROR, [isPrecessionIncluded]: Must be a bool, current type = '{0}'".format(type(isPrecessionIncluded)))
		exit()
	logger.debug("isPrecessionIncluded = '{0}'".format(isPrecessionIncluded))

	# Ensure that declination ranges are set and within within ranges
	if declination_min is not None and declination_min not in np.arange(-89, 90): # if defined, but not in range
		logger.critical("\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{0}'".format(declination_min))
		exit()
	logger.debug("declination_min = '{0}'".format(declination_min))

	# Error Handling for finalPositionOfStars() function
	if not isPlotFunction:
		# Ensure that declination ranges are set and within within ranges
		if declination_max is not None and declination_max not in np.arange(-89, 90): # if defined, but not in range
			logger.critical("\nCRITICAL ERROR, [declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{0}'".format(declination_max))
			exit()
		logger.debug("declination_max = '{0}'".format(declination_max))

	# Error Handling for plotStereographicProjection() function
	if isPlotFunction:
		# Ensure that Hemisphere selected are within options
		if northOrSouth not in ["North", "South"]:
			logger.critical("\nCRITICAL ERROR, [northOrSouth]: Hemisphere options are ['North', 'South'], current option = '{0}'".format(northOrSouth))
			exit()
		logger.debug("northOrSouth = '{0}'".format(northOrSouth))

		# Ensure that maxMagnitudeFilter options is a float, set by default to None
		if maxMagnitudeFilter is not None and type(maxMagnitudeFilter) != float:
			logger.critical("\nCRITICAL ERROR, [maxMagnitudeFilter]: Must be a float, current type = '{0}'".format(type(maxMagnitudeFilter)))
			exit()
		logger.debug("maxMagnitudeFilter = '{0}'".format(maxMagnitudeFilter))

		# Ensure that the display options for star names and declination numbers are booleans ["True", "False"]
		if type(displayStarNamesLabels) != bool:
			logger.critical("\nCRITICAL ERROR, [displayStarNamesLabels]: Must be a bool, current type = '{0}'".format(type(displayStarNamesLabels)))
			exit()
		logger.debug("displayStarNamesLabels = '{0}'".format(displayStarNamesLabels))
		if type(displayDeclinationNumbers) != bool:
			logger.critical("\nCRITICAL ERROR, [displayDeclinationNumbers]: Must be a bool, current type = '{0}'".format(type(displayDeclinationNumbers)))
			exit()
		logger.debug("displayDeclinationNumbers = '{0}'".format(displayDeclinationNumbers))

		# Ensure that increment options are 1, 5, 10
		if type(incrementBy) != int or incrementBy not in [1, 5, 10]:
			logger.critical("\nCRITICAL ERROR, [incrementBy]: Must be one of the options [1, 5, 10], current value = '{0}'".format(incrementBy))
			exit()
		logger.debug("incrementBy = '{0}'".format(incrementBy))

		# Ensure that the only options for showPlot are booleans ["True", "False"]
		if type(showPlot) != bool:
			logger.critical("\nCRITICAL ERROR, [showPlot]: Must be a bool, current type = '{0}'".format(type(showPlot)))
			exit()
		logger.debug("showPlot = '{0}'".format(showPlot))

		# Ensure that the color given is a string (matplotlib has error checking for invalid color options)
		if type(fig_plot_color) != str:
			logger.critical("\nCRITICAL ERROR, [fig_plot_color]: Must be a string, current type = '{0}'".format(type(fig_plot_color)))
			exit()
		logger.debug("fig_plot_color = '{0}'".format(fig_plot_color))

		# Ensure that the user defined title of the plot is a string
		if fig_plot_title is not None and type(fig_plot_title) != str:
			logger.critical("\nCRITICAL ERROR, [fig_plot_title]: Must be a string, current type = '{0}'".format(type(fig_plot_title)))
			exit()
		logger.debug("fig_plot_title = '{0}'".format(fig_plot_title))

		# Ensure that figure options are integers or floats
		if type(figsize_n) != int and type(figsize_n) != float:
			logger.critical("\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(type(figsize_n)))
			exit()
		logger.debug("figsize_n = '{0}'".format(figsize_n))
		if type(figsize_dpi) != int and type(figsize_dpi) != float:
			logger.critical("\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(type(figsize_dpi)))
			exit()
		logger.debug("figsize_dpi = '{0}'".format(figsize_dpi))

		# Ensure that the user defined figure saved name is a string
		if save_plot_name is not None and type(save_plot_name) != str:
			logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a string, current type = '{0}'".format(type(save_plot_name)))
			exit()
		logger.debug("save_plot_name = '{0}'".format(save_plot_name))
