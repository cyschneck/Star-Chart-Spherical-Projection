########################################################################
# Return the calculated position of Stars
########################################################################
import logging
import os

import numpy as np
import pandas as pd

import star_chart_spherical_projection

## Logging set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def finalPositionOfStars(builtInStars=[], 
						yearSince2000=0,
						isPrecessionIncluded=True,
						userDefinedStars=[],
						onlyDisplayUserStars=False,
						declination_min=None,
						declination_max=None,
						save_to_csv=None):
	# return the final position of the stars as a dictionary

	star_chart_spherical_projection.errorHandling(isPlotFunction=False,
												builtInStars=builtInStars,
												yearSince2000=yearSince2000,
												isPrecessionIncluded=isPrecessionIncluded,
												userDefinedStars=userDefinedStars,
												onlyDisplayUserStars=onlyDisplayUserStars,
												declination_min=declination_min,
												declination_max=declination_max,
												save_to_csv=save_to_csv)
	if not onlyDisplayUserStars:
		builtInStars = [x.title() for x in builtInStars] # convert all names to capitalized
		listOfStars = star_chart_spherical_projection.getStarList(builtInStars)
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
	
	# Set declination min values when using the generateStereographicProjection() to capture all stars if not set
	declination_min = -90
	declination_max = 90

	_, _, _, finalPositionOfStarsDict = star_chart_spherical_projection.generateStereographicProjection(starList=listOfStars, 
																										northOrSouth="North", 
																										declination_min=declination_min,
																										yearSince2000=yearSince2000,
																										isPrecessionIncluded=isPrecessionIncluded,
																										maxMagnitudeFilter=None,
																										declination_max=declination_max)
	# Generate a .csv file with final positions of stars
	if save_to_csv is not None:
		header_options = ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]
		star_chart_list = []
		for star_name, star_position in finalPositionOfStarsDict.items():
			star_chart_list.append([star_name, star_position["RA"], star_position["Declination"]])
		df = pd.DataFrame(star_chart_list, columns=header_options)
		df = df.sort_values(by=["Star Name"])
		df.to_csv(save_to_csv, header=header_options, index=False)
	return finalPositionOfStarsDict

def starPositionOverTime(builtInStarName=None,
						newStar=None,
						startYear=None,
						endYear=None,
						incrementYear=None,
						isPrecessionIncluded=True,
						save_to_csv=None):
	
	if builtInStarName is not None:
		print(builtInStarName)
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		star_data = star_dataframe.loc[star_dataframe["Star Name"] == builtInStarName].values.flatten().tolist()
		star_data = star_chart_spherical_projection.convertRAhrtoRadians([star_data])[0]
		star_name, star_right_ascension_radians, star_declination, star_pm_speed, star_pm_angle, star_mag = star_data
	if newStar is not None:
		print("TODO: starPositionOverTime newStar option")

	endYear += 1 # inclusive of endYear
	years_to_calculate = np.arange(startYear, endYear, incrementYear).tolist()
	position_over_time = {}
	for year in years_to_calculate:
		star_right_ascension_radians, star_declination = star_chart_spherical_projection.calculateRAandDeclinationViaProperMotion(year - 2000, 
																														star_right_ascension_radians, 
																														star_declination, 
																														star_pm_speed, 
																														star_pm_angle)
		if isPrecessionIncluded:
			star_declination, star_right_ascension_radians = star_chart_spherical_projection.precessionVondrak(star_name,
																									star_right_ascension_radians,
																									star_declination,
																									year - 2000)			
		star_right_ascension_hours = star_chart_spherical_projection.convertRadianstoRAhr(star_right_ascension_radians)
		position_over_time[year] = {"Right Right Ascension (radians)": star_right_ascension_radians, 
									"Right Ascension (HH.MM.SS)" : star_right_ascension_hours, 
									"Declination (DD.SS)": star_declination}
	print(position_over_time)
	return None
