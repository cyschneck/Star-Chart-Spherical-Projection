import math
import numpy as np

import star_chart_spherical_projection

class add_new_star:
    def __init__(self,
                star_name=None,
                ra=None,
                dec=None,
                pm_speed=None,
                pm_angle=None,
                pm_speed_ra=None,
                pm_speed_dec=None,
                magnitude=None):

        star_chart_spherical_projection.errorHandlingStarClass(star_name=star_name,
                                                                ra=ra,
                                                                dec=dec,
                                                                pm_speed=pm_speed,
                                                                pm_angle=pm_angle,
                                                                pm_speed_ra=pm_speed_ra,
                                                                pm_speed_dec=pm_speed_dec,
                                                                magnitude=magnitude)

        self.star_name = star_name
        self.ra = ra
        self.dec = dec
        self.magnitude = magnitude
        self.pm_speed_ra = pm_speed_ra
        self.pm_speed_dec = pm_speed_dec

        if self.pm_speed_ra is not None and self.pm_speed_dec is not None:
            self.convertToSpeedAndAngle(proper_motion_ra=self.pm_speed_ra, proper_motion_dec=self.pm_speed_dec)
        else:
            self.pm_speed = pm_speed
            self.pm_angle = pm_angle

    def convertToSpeedAndAngle(self, proper_motion_ra=None, proper_motion_dec=None):
        # convert proper motion ra and declination to a speed and angle
        self.pm_speed = math.sqrt(proper_motion_dec**2 + proper_motion_ra**2)
        self.pm_angle = np.rad2deg(math.atan(proper_motion_ra / proper_motion_dec))
        if self.pm_angle < 0: self.pm_angle += 360 # clamp between 0 and 360
