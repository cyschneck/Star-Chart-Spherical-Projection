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
						startYearSince2000=None,
						endYearSince2000=None,
						incrementYear=None,
						isPrecessionIncluded=True,
						save_to_csv=None):

	if builtInStarName is not None:
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		star_data = star_dataframe.loc[star_dataframe["Star Name"] == builtInStarName].values.flatten().tolist()
		#star_data = star_chart_spherical_projection.convertRAhrtoRadians([star_data])[0]
		star_name, star_ra, star_declination, star_pm_speed, star_pm_angle, star_mag = star_data
	if newStar is not None:
		star_name = newStar.starName
		star_ra = newStar.ra
		#star_right_ascension_radians = star_chart_spherical_projection.convertRAhrtoRadians([[None, newStar.ra]])[0][1]
		star_declination = newStar.dec
		star_pm_speed = newStar.properMotionSpeed
		star_pm_angle = newStar.properMotionAngle
		star_mag = newStar.magnitudeVisual

	years_to_calculate = np.arange(startYearSince2000, endYearSince2000+1, incrementYear).tolist()
	position_over_time = {}
	for year in years_to_calculate:
		star_row = [[star_name, star_ra, star_declination, star_pm_speed, star_pm_angle, star_mag]]
		_, star_radians, _, star_dict = star_chart_spherical_projection.generateStereographicProjection(starList=star_row, 
																							yearSince2000=year,
																							isPrecessionIncluded=isPrecessionIncluded,
																							northOrSouth="North",
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

def plotStarPositionOverTime(builtInStarName=None, 
							newStar=None,
							startYearSince2000=None,
							endYearSince2000=None,
							incrementYear=10,
							isPrecessionIncluded=True,
							DecOrRA="D",
							showPlot=True,
							showYearMarker=True,
							fig_plot_title=None,
							fig_plot_color="C0",
							figsize_n=12,
							figsize_dpi=100,
							save_plot_name=None):

	position_over_time_dict = starPositionOverTime(builtInStarName=builtInStarName,
													newStar=newStar,
													startYearSince2000=startYearSince2000,
													endYearSince2000=endYearSince2000,
													incrementYear=incrementYear,
													isPrecessionIncluded=isPrecessionIncluded)

	if builtInStarName is not None:
		star_csv_file = os.path.join(os.path.dirname(__file__), 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
		star_dataframe = pd.read_csv(star_csv_file)
		star_data = star_dataframe.loc[star_dataframe["Star Name"] == builtInStarName].values.flatten().tolist()
		star_name, _, _, _, _, _ = star_data
	if newStar is not None:
		star_name = newStar.starName
	
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

	if isPrecessionIncluded:
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

	if year_lst[0] >= -2000: startYear_bce_ce = "{0} C.E".format(year_lst[0]) # postive years for C.E
	if year_lst[0] < -2000: startYear_bce_ce = "{0} B.C.E".format(abs(year_lst[0])) # negative years for B.C.E
	if year_lst[-1] >= -2000: endYear_bce_ce = "{0} C.E".format(year_lst[-1]) # postive years for C.E
	if year_lst[-1] < -2000: endYear_bce_ce = "{0} B.C.E".format(abs(year_lst[-1])) # negative years for B.C.E
	
	plt.title("{0}'s {1} {2} from {3} to {4}, Every {5} Years".format(star_name,
																	title,
																	precession_label,
																	startYear_bce_ce,
																	endYear_bce_ce,
																	incrementYear))
	plt.plot(year_lst, plot_y)
	plt.xlabel("Year")
	plt.ylabel(y_label)
	
	ax.set_xticks(np.arange(year_lst[0], year_lst[-1]+1, x_increment))
	ax.set_yticks(np.linspace(min(plot_y), max(plot_y), y_increment))

	if showYearMarker:
		current_year = datetime.now().year
		plt.axvline(current_year, linewidth=0.5, color="black", linestyle="dashed")
	plt.xticks(rotation=90)

	if showPlot:
		plt.show()

	if save_plot_name is not None:
		fig.savefig(save_plot_name, dpi=fig.dpi)

def predictPoleStar(yearSince2000=None, northOrSouth="North"):
	# Find the next North/South Pole Star
	final_position_builtin_stars = star_chart_spherical_projection.finalPositionOfStars(yearSince2000=yearSince2000,
																						isPrecessionIncluded=True)
	# Set the pole declination based on either North/South
	if northOrSouth == "North":
		pole_declination = 90
	if northOrSouth == "South":
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
