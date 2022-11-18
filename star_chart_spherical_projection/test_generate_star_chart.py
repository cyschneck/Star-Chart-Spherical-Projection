# Test generate_star_chart functions
import generate_star_chart

if __name__ == '__main__':
	# Get List of Stars with data
	stars_list = ["Polaris", "Vega", "Merak"]
	star_chart_list = generate_star_chart.getStarList(stars_list)

	# Convert Star chart from RA hours to Radians to chart
	star_chart_list = generate_star_chart.convertRAhrtoRadians(star_chart_list)
	#print(star_chart_list)

	generate_star_chart.plotStarChart(list_of_stars=star_chart_list,
									declination_min=-25,
									displayDeclinationNumbers=False,
									year_since_2000=10.2,
									displayStarNamesLabels=False,
									northOrSouth="north",
									increment_by=10,
									figsize_n=8,
									figsize_dpi=120)
