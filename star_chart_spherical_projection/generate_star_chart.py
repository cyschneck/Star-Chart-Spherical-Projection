########################################################################
# Generate a star chart centered on:
#		Northern Hemsiphere = 90°
#		Southern Hemsiphere = -90°
########################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import configparser
import logging
import csv

import star_chart_spherical_projection

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

## Constants
config = configparser.ConfigParser()
config.read("config.ini")

# Start Year (JP2000)
j2000 = 2000 # start year of the star catalogue (jan 1 2000 via IAU)

def getStarList(required_stars):
	# generate a star object
	# stars: ["name", "RA: HH.MM.SS", Declination DD.SS, Proper Motion Speed (mas/yr), Proper Motion Angle (DD.SS), Magnitude (V, Visual)]
	star_data_list = []
	import os
	print(os.getcwd())
	star_dataframe = pd.read_csv("star_data/star_data.csv")
	for index, row in star_dataframe.iterrows():
		if row["Star Name"] in required_stars:
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

def plotStarChart(list_of_stars=[], 
				northOrSouth="Both", 
				declination_min=None,
				year_since_2000=0,
				displayStarNamesLabels=True,
				displayDeclinationNumbers=True,
				increment_by=5, 
				figsize_n=12,
				figsize_dpi=100):
	# plot star chart as a circular graph

	# Catch errors in given arguments before plotting and set default constants
	northOrSouth = northOrSouth.capitalize()
	star_chart_spherical_projection.errorHandling(list_of_stars, 
													northOrSouth, 
													declination_min,
													year_since_2000,
													displayStarNamesLabels,
													displayDeclinationNumbers,
													increment_by, 
													figsize_n,
													figsize_dpi)

	# Set max declination based on hemisphere selected
	if declination_min is None:
		if northOrSouth == "North": declination_min = int(config["declinationDefaultValues"]["northern_declination_min"])
		if northOrSouth == "South": declination_min = int(config["declinationDefaultValues"]["southern_declination_min"])
	if northOrSouth == "North": declination_max = int(config["declinationDefaultValues"]["northern_declination_max"])
	if northOrSouth == "South": declination_max = int(config["declinationDefaultValues"]["southern_declination_max"])

	logger.info("PLOTTING: {0}".format(list_of_stars))
	logger.info("list_of_stars = {0}".format(list_of_stars))
	logger.info("northOrSouth = {0}".format(northOrSouth))
	logger.info("declination_min = {0}".format(declination_min))
	logger.info("declination_max = {0}".format(declination_max))
	logger.info("year_since_2000 = {0}".format(year_since_2000))
	logger.info("displayStarNamesLabels = {0}".format(displayStarNamesLabels))
	logger.info("displayDeclinationNumbers = {0}".format(displayDeclinationNumbers))
	logger.info("displayDeclinationNumbers = {0}".format(displayDeclinationNumbers))
	logger.info("increment_by = {0}".format(increment_by))
	logger.info("figsize_n = {0}".format(figsize_n))
	logger.info("figsize_dpi = {0}".format(figsize_dpi))

	fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
	ax = fig.subplots(subplot_kw={'projection': 'polar'})

	# Set Declination (astronomical 'latitude') as Y (radius of polar plot)

	# Split up chart into North/South hemisphere
	declination_values = np.arange(declination_min, declination_max+1, increment_by) # +1 to show max value in range
	min_dec_value = declination_min
	max_dec_value = declination_max

	# Store the ruler positions based on degrees and the ratio of the ruler
	ruler_position_dict = star_chart_spherical_projection.calculateRuler(min_dec_value, max_dec_value, increment_by, northOrSouth)
