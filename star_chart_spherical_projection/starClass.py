class newStar:
	def __init__(self,
				starName=None,
				ra=None,
				dec=None,
				properMotionSpeed=None,
				properMotionAngle=None,
				properMotionRA=None,
				properMotionDec=None,
				magnitudeVisual=None):
		self.starName = starName
		self.ra = ra
		self.dec = dec
		self.magnitudeVisual = magnitudeVisual

		if properMotionSpeed is None and properMotionAngle is None:
			# TOODO
			self.properMotionSpeed,  self.properMotionAngle = self.convertToSpeedAndAngle(proper_motion_ra=properMotionRA,
																					proper_motion_dec=properMotionDec)
		else:
			self.properMotionSpeed = properMotionSpeed
			self.properMotionAngle = properMotionAngle

	def convertToSpeedAndAngle(self, proper_motion_ra=None, proper_motion_dec=None):
		# convert proper motion ra and declination to a speed and angle
		return None, None
