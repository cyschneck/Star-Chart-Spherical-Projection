########################################################################
# Generate a star chart centered on:
#		Northern Hemsiphere = 90°
#		Southern Hemsiphere = -90°
########################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
import csv

import error_handling as error_handling_script

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

# Start Year (JP2000)
j2000 = 2000 # start year of the star catalogue (jan 1 2000 via IAU)

def getStarList(required_stars):
	# generate a star object
	# stars: ["name", "RA: HH.MM.SS", Declination DD.SS, Proper Motion Speed (mas/yr), Proper Motion Angle (DD.SS), Magnitude (V, Visual)]
	star_data_list = []
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

	# Catch errors in given arguments before plotting
	error_handling_script.errorHandling(list_of_stars, 
										northOrSouth, 
										declination_min,
										year_since_2000,
										displayStarNamesLabels,
										displayDeclinationNumbers,
										increment_by, 
										figsize_n,
										figsize_dpi)
	
	fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)
	ax = fig.subplots(subplot_kw={'projection': 'polar'})

	logger.info("PLOTTING: {0}".format(list_of_stars))
