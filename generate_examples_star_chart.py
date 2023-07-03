# Test generate_star_chart functions
# python3 test_generate_star_chart.py
import pandas as pd

import star_chart_spherical_projection

if __name__ == '__main__':
	exalibur_star = star_chart_spherical_projection.newStar(starName="Exalibur",
					ra="14.04.23",
					dec=64.22,
					properMotionSpeed=12.3,
					properMotionAngle=83,
					magnitudeVisual=1.2)
	karaboudjan_star = star_chart_spherical_projection.newStar(starName="Karaboudjan",
					ra="3.14.15",
					dec=10.13,
					properMotionSpeedRA=57.6,
					properMotionSpeedDec=60.1,
					magnitudeVisual=0.3)
	#star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
	#				builtInStars=["Vega", "Arcturus", "Altair"],
	#				userDefinedStars=[exalibur_star, karaboudjan_star],
	#				displayStarNamesLabels=True,
	#				fig_plot_color="red",
	#				yearSince2000=-44000,
	#				showPlot=True)
	#exit()
	#star_final_pos_dict = star_chart_spherical_projection.finalPositionOfStars(builtInStars=["Vega"], yearSince2000=11500, save_to_csv="final_star_positions.csv")
	#print(star_final_pos_dict)
	star_chart_spherical_projection.starPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=-16000,
														endYearSince2000=14000,
														isPrecessionIncluded=True,
														incrementYear=3,
														save_to_csv="testing_final_positions.csv")
	star_chart_spherical_projection.plotStarPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=-14000,
														endYearSince2000=14000,
														isPrecessionIncluded=True,
														incrementYear=100,
														DecOrRA="Declination")
	# note, includes endYear (0 to 9, every three = [0, 3, 6, 9], inclusive of start, inclusive of end
	exit()
	year_to_calculate = 11500

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
