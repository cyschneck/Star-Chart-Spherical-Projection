# Test generate_star_chart functions
# python3 test_generate_star_chart.py
import pandas as pd

import star_chart_spherical_projection

if __name__ == '__main__':
	year_to_calculate = 11500

	new_star_object = star_chart_spherical_projection.newStar(starName="testing star",
																ra="1.2.3",
																dec=10.45,
																properMotionSpeed=1200.0,
																properMotionAngle=56.3,
																magnitudeVisual=1.2)
	#new_star_object = star_chart_spherical_projection.newStar(starName="testing star2",
	#															ra="1.2.3",
	#															dec=65.45,
	#															properMotionRA=12.14,
	#															properMotionDec=14.15,
	#															magnitudeVisual=1.2)
	print("new_star_object.starName = {0}".format(new_star_object.starName))
	print("new_star_object.ra = {0}".format(new_star_object.ra))
	print("new_star_object.dec = {0}".format(new_star_object.dec))
	print("new_star_object.properMotionSpeed = {0}".format(new_star_object.properMotionSpeed))
	print("new_star_object.properMotionAngle = {0}".format(new_star_object.properMotionAngle))
	print("new_star_object.magnitudeVisual = {0}".format(new_star_object.magnitudeVisual))


	star_chart_spherical_projection.plotStereographicProjection(userListOfStars=["Vega"],
																userDefinedStars=[new_star_object],
																northOrSouth="North",
																onlyDisplayUserStars=False,
																displayStarNamesLabels=True,
																yearSince2000=23)

	exit()
	# Generate a .csv file with final positions of stars
	#star_final_pos_dict = star_chart_spherical_projection.finalPositionOfStars(yearSince2000=year_to_calculate)
	#header_options = ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)"]
	#star_chart_list = []
	#for star_name, star_position in star_final_pos_dict.items():
	#	star_chart_list.append([star_name, star_position["RA"], star_position["Declination"]])
	#df = pd.DataFrame(star_chart_list, columns=header_options)
	#df = df.sort_values(by=["Star Name"])
	#df.to_csv("examples/star_final_position_data.csv", header=header_options, index=False)
	#print(df['Star Name'].tolist())

	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South",
																displayStarNamesLabels=False,
																yearSince2000=23,
																save_plot_name="examples/quickstart_south_2023")
	## Northern Hemisphere: Graph Without and With Precession
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=True,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=False,
																fig_plot_color="red",
																save_plot_name="examples/north_with_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=True,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=True,
																fig_plot_color="red",
																save_plot_name="examples/north_with_labels_with_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=False,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=False,
																fig_plot_color="red",
																save_plot_name="examples/north_without_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=False,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=True,
																fig_plot_color="red",
																save_plot_name="examples/north_without_labels_with_precession")

	## Southern Hemisphere: Graph Without and With Precession
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=True,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=False,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_with_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=True,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=True,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_with_labels_with_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=False,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=False,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_without_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=False,
																yearSince2000=year_to_calculate,
																isPrecessionIncluded=True,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_without_labels_with_precession")
