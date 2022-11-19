import logging
import configparser
import numpy as np

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

## Declination default options from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

def errorHandling(list_of_stars, 
				northOrSouth, 
				declination_min,
				year_since_2000,
				displayStarNamesLabels,
				displayDeclinationNumbers,
				increment_by, 
				figsize_n,
				figsize_dpi):
	####################################################################
	# ERROR CATCHES AND LOGGING
	####################################################################
	# Ensure that star list has at least one star to chart
	if len(list_of_stars) == 0:
		logger.critical("\nCRITICAL ERROR, [list_of_stars]: List of stars needs at least one star to chart, current list = {0}".format(full_star_list))
		exit()
	logger.debug("list_of_stars = '{0}'".format(list_of_stars))

	# Ensure that Hemisphere selected are within options
	if northOrSouth not in ["North", "South"]:
		logger.critical("\nCRITICAL ERROR, [northOrSouth]: Hemisphere options are ['North', 'South'], current option = '{0}'".format(northOrSouth))
		exit()
	logger.debug("northOrSouth = '{0}'".format(northOrSouth))

	# Ensure that declination ranges are set and within within ranges
	if declination_min is not None and declination_min not in np.arange(-89, 90): # if defined, but not in range
		logger.critical("\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{0}'".format(declination_min))
		exit()
	logger.debug("declination_min = '{0}'".format(declination_min))

	# Ensure if a year is selected it is a float or int, set by default to 0 (the year = 2000)
	if type(year_since_2000) != int and type(year_since_2000) != float:
		logger.critical("\nCRITICAL ERROR, [year_since_2000]: Must be a int or float, current type = '{0}'".format(type(year_since_2000)))
		exit()
	logger.debug("year_since_2000 = '{0}'".format(year_since_2000))

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
	if type(increment_by) != int or increment_by not in [1, 5, 10]:
		logger.critical("\nCRITICAL ERROR, [increment_by]: Must be one of the options [1, 5, 10], current value = '{0}'".format(increment_by))
		exit()
	logger.debug("increment_by = '{0}'".format(increment_by))
	
	# Ensure that figure options are integers or floats
	if type(figsize_n) != int and type(figsize_n) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(type(figsize_n)))
		exit()
	logger.debug("figsize_n = '{0}'".format(figsize_n))
	if type(figsize_dpi) != int and type(figsize_dpi) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(type(figsize_dpi)))
		exit()
	logger.debug("figsize_dpi = '{0}'".format(figsize_dpi))
