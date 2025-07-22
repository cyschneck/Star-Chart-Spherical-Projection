########################################################################
# Distance between declination values in the radius are defined as either
#       Northern Hemisphere = tan(45° - angle of inclination)
#       Southern Hemisphere = tan(45° + angle of inclination)
########################################################################
import math
import numpy as np

def _calculate_length(angle_of_inclination, radius_of_circle, pole):
    # convert angle into length of radius
    if pole == "North":
        angle_in_radians = np.deg2rad(45 - angle_of_inclination/2) # + angle for northern projection
    if pole == "South":
        angle_in_radians = np.deg2rad(45 +  angle_of_inclination/2) # - angle for southern projection
    equation_of_length = radius_of_circle * math.tan(angle_in_radians) # calculated
    return equation_of_length

def _calculate_radius_of_circle(min_dec, pole):
    # calculate radius of full circle from -80 to 80 where min dec is the radius of smaller circle
    # assumes total length = 1
    total_ruler_len = 1
    if pole == "North":
        radius_of_circle_at_min_dec = (total_ruler_len/2) / math.tan(np.deg2rad(45 - min_dec/2))
    if pole == "South":
        radius_of_circle_at_min_dec = (total_ruler_len/2) / math.tan(np.deg2rad(45 + min_dec/2))
    return radius_of_circle_at_min_dec

def _calculate_ruler(declination_min, declination_max, increment, pole):
    # define the length of each segment in ruler when radius = 1

    x_angleOfDeclination = np.arange(-90, 90+1,increment) # declination max range from -90 to 90
    y_lengthSegments = []

    declination_angles_ruler = np.arange(-90, 90+1, increment) # declination max range from -90 to 90

    # calculate full size of circle to find declination for smaller range
    radius_of_circle = _calculate_radius_of_circle(declination_min, pole)

    ruler_position_dict = {} # dict: {degree : position_on_ruler }

    for n_angle in declination_angles_ruler:
        if pole == "North":
            ruler_position = _calculate_length(n_angle, radius_of_circle, "North")
            y_lengthSegments.append(ruler_position)
            if n_angle >= declination_min and n_angle <= declination_max: # North
                ruler_position_dict[n_angle] = round(ruler_position, 4)
        if pole == "South":
            ruler_position = _calculate_length(n_angle, radius_of_circle, "South")
            y_lengthSegments.append(ruler_position)
            if n_angle <= declination_min and n_angle >= declination_max: # South
                ruler_position_dict[n_angle] = round(ruler_position, 4)

    return ruler_position_dict
