########################################################################
# Distance between declination values in the radius are defined as either
#		Northern Hemsiphere = tan(45° - angle of inclination)
#		Southern Hemsiphere = tan(45° + angle of inclination)
########################################################################
import math
import numpy as np

def calculateLength(angle_of_inclination, radius_of_circle, northOrSouth):
	# convert angle into length of radius
	if northOrSouth == "North":
		angle_in_radians = np.deg2rad(45 - angle_of_inclination/2) # + angle for northern projection
	if northOrSouth == "South":
		angle_in_radians = np.deg2rad(45 +  angle_of_inclination/2) # - angle for southern projection
	equation_of_length = radius_of_circle * math.tan(angle_in_radians) # calculated
	return equation_of_length

def calculateRadiusOfCircle(min_dec, northOrSouth):
	# calculate radius of full circle from -80 to 80 where min dec is the radius of smaller circle
	# assumes total length = 1
	total_ruler_len = 1
	if northOrSouth == "North":
		radius_of_circle_at_min_dec = (total_ruler_len/2) / math.tan(np.deg2rad(45 - min_dec/2))
	if northOrSouth == "South":
		radius_of_circle_at_min_dec = (total_ruler_len/2) / math.tan(np.deg2rad(45 + min_dec/2))
	return radius_of_circle_at_min_dec

def calculateRuler(declination_min, declination_max, increment, northOrSouth):
	# define the length of each segment in ruler when radius = 1

	x_angleOfDeclination = np.arange(-90, 90+1,increment) # declination max range from -90 to 90
	y_lengthSegments = []

	declination_angles_ruler = np.arange(-90, 90+1, increment) # declination max range from -90 to 90

	# calculate full size of circle to find declination for smaller range
	radius_of_circle = calculateRadiusOfCircle(declination_min, northOrSouth)

	ruler_position_dict = {} # dict: {degree : position_on_ruler }

	for n_angle in declination_angles_ruler:
		if northOrSouth == "North":
			ruler_position = calculateLength(n_angle, radius_of_circle, "North")
			y_lengthSegments.append(ruler_position)
			if n_angle >= declination_min and n_angle <= declination_max: # North
				ruler_position_dict[n_angle] = round(ruler_position, 4)
		if northOrSouth == "South":
			ruler_position = calculateLength(n_angle, radius_of_circle, "South")
			y_lengthSegments.append(ruler_position)
			if n_angle <= declination_min and n_angle >= declination_max: # South
				ruler_position_dict[n_angle] = round(ruler_position, 4)

	return ruler_position_dict
