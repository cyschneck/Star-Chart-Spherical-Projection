import math
import numpy as np

import star_chart_spherical_projection

class add_new_star:
	def __init__(self,
				starName=None,
				ra=None,
				dec=None,
				properMotionSpeed=None,
				properMotionAngle=None,
				properMotionSpeedRA=None,
				properMotionSpeedDec=None,
				magnitudeVisual=None):

		star_chart_spherical_projection.errorHandlingStarClass(starName=starName,
																ra=ra,
																dec=dec,
																properMotionSpeed=properMotionSpeed,
																properMotionAngle=properMotionAngle,
																properMotionSpeedRA=properMotionSpeedRA,
																properMotionSpeedDec=properMotionSpeedDec,
																magnitudeVisual=magnitudeVisual)

		self.starName = starName
		self.ra = ra
		self.dec = dec
		self.magnitudeVisual = magnitudeVisual
		self.properMotionSpeedRA = properMotionSpeedRA
		self.properMotionSpeedDec = properMotionSpeedDec

		if self.properMotionSpeedRA is not None and self.properMotionSpeedDec is not None:
			self.convertToSpeedAndAngle(proper_motion_ra=self.properMotionSpeedRA, proper_motion_dec=self.properMotionSpeedDec)
		else:
			self.properMotionSpeed = properMotionSpeed
			self.properMotionAngle = properMotionAngle

	def convertToSpeedAndAngle(self, proper_motion_ra=None, proper_motion_dec=None):
		# convert proper motion ra and declination to a speed and angle
		self.properMotionSpeed = math.sqrt(proper_motion_dec**2 + proper_motion_ra**2)
		self.properMotionAngle = np.rad2deg(math.atan(proper_motion_ra / proper_motion_dec))
		if self.properMotionAngle < 0: self.properMotionAngle += 360 # clamp between 0 and 360
