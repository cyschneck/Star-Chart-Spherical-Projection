########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import csv
import numpy as np
import os
import pandas as pd

import star_chart_spherical_projection

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
				save_plot_name=None,
				save_to_csv=None):
	# Error Handling for Variables shared between finalPositionOfStars() and plotStereographicProjection() (defined by isPlotFunction)

	# Ensure that star list is a list
	if type(builtInStars) != list:
		raise ValueError(f"[builtInStars]: Must be a list, current type = '{type(builtInStars)}'")

	## Check that user list has stars that are found in current list
	if len(builtInStars) != 0:
		builtInStars = [x.title() for x in builtInStars] # convert all names to capitalized
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		all_star_names_in_csv = list(star_dataframe['Star Name'])
		for star_given in builtInStars:
			if star_given not in all_star_names_in_csv:
				raise ValueError(f"[builtInStars]: '{star_given}' not a star in current list of stars, please select one of the following: {all_star_names_in_csv}")

	# Ensure that declination ranges are set and within within ranges
	if declination_min is not None:
		if type(declination_min) != int and type(declination_min) != float:
			raise ValueError(f"[declination_min]: Must be a int or float, current type = '{type(declination_min)}'")
		if declination_min not in np.arange(-89, 90): # if defined, but not in range
			raise ValueError(f"[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '{declination_min}'")

	# Ensure if a year is selected it is a float or int, set by default to 0 (the year = 2000)
	if type(yearSince2000) != int and type(yearSince2000) != float:
		raise ValueError(f"[yearSince2000]: Must be a int or float, current type = '{type(yearSince2000)}'")

	# Ensure that precession options are booleans ["True", "False"]
	if type(isPrecessionIncluded) != bool:
		raise ValueError(f"[isPrecessionIncluded]: Must be a bool, current type = '{type(isPrecessionIncluded)}'")

	if type(userDefinedStars) != list:
		raise ValueError(f"[userDefinedStars]: Must be a list, current type = '{type(userDefinedStars)}'")
	for user_star in userDefinedStars:
		if type(user_star) != star_chart_spherical_projection.newStar:
			raise ValueError(f"[userDefinedStars]: {type(user_star)} is not a valid newStar object (see: star_chart_spherical_projection.newStar)")

	if type(onlyDisplayUserStars) != bool:
		raise ValueError(f"[onlyDisplayUserStars]: Must be a bool, current type = '{type(onlyDisplayUserStars)}'")

	# Error Handling for finalPositionOfStars() function
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

	# Error Handling for plotStereographicProjection() function
	if isPlotFunction:
		# Ensure that Hemisphere selected are within options
		if type(northOrSouth) != str:
			raise ValueError(f"[northOrSouth]: Must be a str, current type = '{type(northOrSouth)}'")
		else:
			if northOrSouth not in ["North", "South"]:
				raise ValueError(f"[northOrSouth]: Hemisphere options are ['North', 'South'], current option = '{northOrSouth}'")

		# Ensure that maxMagnitudeFilter options is a float, set by default to None
		if maxMagnitudeFilter is not None:
			if type(maxMagnitudeFilter) != int and type(maxMagnitudeFilter) != float:
				raise ValueError(f"[maxMagnitudeFilter]: Must be a int or float, current type = '{type(maxMagnitudeFilter)}'")

		# Ensure that the display options for star names and declination numbers are booleans ["True", "False"]
		if type(displayStarNamesLabels) != bool:
			raise ValueError(f"[displayStarNamesLabels]: Must be a bool, current type = '{type(displayStarNamesLabels)}'")

		if type(displayDeclinationNumbers) != bool:
			raise ValueError(f"[displayDeclinationNumbers]: Must be a bool, current type = '{type(displayDeclinationNumbers)}'")

		# Ensure that increment options are 1, 5, 10
		if type(incrementBy) != int:
			raise ValueError(f"[incrementBy]: Must be a int, current type = '{type(incrementBy)}'")
		if incrementBy not in [1, 5, 10]:
			raise ValueError(f"[incrementBy]: Must be one of the options [1, 5, 10], current value = '{incrementBy}'")

		# Ensure that the only options for showPlot are booleans ["True", "False"]
		if type(showPlot) != bool:
			raise ValueError(f"[showPlot]: Must be a bool, current type = '{type(showPlot)}'")

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

def errorHandlingStarClass(starName=None,
						ra=None,
						dec=None,
						properMotionSpeed=None,
						properMotionAngle=None,
						properMotionSpeedRA=None,
						properMotionSpeedDec=None,
						magnitudeVisual=None):
	
	if starName is None:
		raise ValueError("[starName]: starName is required")
	else:
		if type(starName) != str:
			raise ValueError(f"[starName]: Must be a str, current type = '{type(starName)}'")

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
				raise ValueError(f"[ra]: Each part of the Right Ascension must be an integar, '{ra_time}' current type = {type(ra_time)}")

	if dec is None:
		raise ValueError("[dec]: Declination is required")
	else:
		if type(dec) != int and type(dec) != float:
			raise ValueError(f"[dec]: Must be a int or float, current type = '{type(dec)}'")

	if properMotionSpeed is not None:
		if type(properMotionSpeed) != int and type(properMotionSpeed) != float:
			raise ValueError(f"[properMotionSpeed]: Must be a int or float, current type = '{type(properMotionSpeed)}'")

	if properMotionAngle is not None:
		if type(properMotionAngle) != int and type(properMotionAngle) != float:
			raise ValueError(f"[properMotionAngle]: Must be a int or float, current type = '{type(properMotionAngle)}'")

	if properMotionSpeedRA is not None:
		if type(properMotionSpeedRA) != int and type(properMotionSpeedRA) != float:
			raise ValueError(f"[properMotionSpeedRA]: Must be a int or float, current type = '{type(properMotionSpeedRA)}'")

	if properMotionSpeedDec is not None:
		if type(properMotionSpeedDec) != int and type(properMotionSpeedDec) != float:
			raise ValueError(f"[properMotionSpeedDec]: Must be a int or float, current type = '{type(properMotionSpeedDec)}'")

	# Verify at least one pair is set
	if properMotionSpeedRA is None and properMotionSpeedDec is None:
		# Neither pairs are set
		if properMotionSpeed is None and properMotionAngle is None:
			raise ValueError("Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required")

	# Verify when only one value is set, make sure to set up its pair
	if properMotionSpeedRA is not None:
		if properMotionSpeedDec is None and properMotionSpeed is None and properMotionAngle is None:
			raise ValueError("[properMotionSpeedDec]: With properMotionSpeedRA set, properMotionSpeedDec is required")

	if properMotionSpeedDec is not None:
		if properMotionSpeedRA is None and properMotionSpeed is None and properMotionAngle is None:
			raise ValueError("[properMotionSpeedRA]: With properMotionSpeedDec set, properMotionSpeedRA is required")
	if properMotionSpeed is not None:
		if properMotionSpeedRA is None and properMotionSpeedDec is None and properMotionAngle is None:
			raise ValueError("[properMotionAngle]: With properMotionSpeed set, properMotionAngle is required")
	if properMotionAngle is not None:
		if properMotionSpeedRA is None and properMotionSpeedDec is None and properMotionSpeed is None:
			raise ValueError("[properMotionSpeed]: With properMotionAngle set, properMotionSpeed is required")

	# Remove the invalid extra options when properMotionSpeed/properMotionAngle should be the only pair set
	if properMotionSpeed is not None and properMotionAngle is not None:
		if properMotionSpeedRA is not None and properMotionSpeedDec is not None:
			raise ValueError("Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required, not both")
		if properMotionSpeedRA is not None and properMotionSpeedDec is None:
			raise ValueError("[properMotionSpeedRA]: With properMotionSpeed/properMotionAngle set, properMotionSpeedRA should be None")
		if properMotionSpeedRA is None and properMotionSpeedDec is not None:
			raise ValueError("[properMotionSpeedDec]: With properMotionSpeed/properMotionAngle set, properMotionSpeedDec should be None")

	# Remove the invalid extra options when properMotionSpeedRA/properMotionSpeedDec should be the only pair set
	if properMotionSpeedRA is not None and properMotionSpeedDec is not None:
		if properMotionSpeed is None and properMotionAngle is not None:
			raise ValueError("[properMotionAngle]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionAngle should be None")
		if properMotionSpeed is not None and properMotionAngle is None:
			raise ValueError("[properMotionSpeed]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionSpeed should be None")

	# Verify the non-None values are the correct pairs: properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle
	if properMotionSpeed is None and properMotionSpeedDec is None:
		if properMotionSpeedRA is not None and properMotionAngle is not None:
			raise ValueError("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedRA")
	if properMotionSpeed is None and properMotionSpeedRA is None:
		if properMotionAngle is not None and properMotionSpeedDec is not None:
			raise ValueError("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedDec")
	if properMotionAngle is None and properMotionSpeedRA is None:
		if properMotionSpeed is not None and properMotionSpeedDec is not None:
			raise ValueError("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedDec")
	if properMotionAngle is None and properMotionSpeedDec is None:
		if properMotionSpeed is not None and properMotionSpeedRA is not None:
			raise ValueError("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedRA")

	if magnitudeVisual is None:
		raise ValueError("[magnitudeVisual]: magnitudeVisual is required")
	else:
		if type(magnitudeVisual) != int and type(magnitudeVisual) != float:
			raise ValueError(f"[magnitudeVisual]: Must be a int or float, current type = '{type(magnitudeVisual)}'")

def errorHandlingPredictPoleStar(yearSince2000=None, northOrSouth=None):
	# Error Handling for predictPoleStar()
	if yearSince2000 is None:
		raise ValueError("[yearSince2000]: yearSince2000 is required")
	else:
		if type(yearSince2000) != int and type(yearSince2000) != float:
			raise ValueError(f"[yearSince2000]: Must be a int or float, current type = '{type(yearSince2000)}'")
	
	if northOrSouth is not None:
		if type(northOrSouth) != str:
			raise ValueError(f"[northOrSouth]: Must be a str, current type = '{type(northOrSouth)}'")
		else:
			if northOrSouth.title() not in ["North", "South"]:
				raise ValueError(f"[northOrSouth]: Must be a 'North' or 'South', currently = '{northOrSouth}'")
