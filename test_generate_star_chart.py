# Test generate_star_chart functions
import star_chart_spherical_projection

if __name__ == '__main__':
	# Get List of Stars with data
	#stars_list = ["Polaris", "Vega", "Merak"]
	star_chart_list = star_chart_spherical_projection.getStarList()

	# Convert Star chart from RA hours to Radians to chart
	star_chart_list = star_chart_spherical_projection.convertRAhrtoRadians(star_chart_list)
	#print(star_chart_list)

	star_chart_spherical_projection.plotStarChart(list_of_stars=star_chart_list,
												displayDeclinationNumbers=True,
												year_since_2000=10.2,
												displayStarNamesLabels=False,
												northOrSouth="north",
												increment_by=10,
												figsize_n=15,
												figsize_dpi=120)
