# Test generate_star_chart functions
# python3 test_generate_star_chart.py
import pandas as pd

import star_chart_spherical_projection

if __name__ == '__main__':
	"""
	chart_stars = ["Vega",
					"Arcturus",
					"Altair",
					"Spica",
					"Sirius",
					"Procyon",
					"Alnilam",
					"Pollux",
					"Alnitak",
					"Mintaka",
					"Castor",
					"Rigel",
					"Betelgeuse",
					"Capella",
					"Saiph",
					"Meissa",
					"Deneb",
					"Formalhaut",
					"Zubeneschamali",
					"Alphard",
					"Bellatrix",
					"Achernar",
					"Canopus",
					"Hadar",
					"Dubhe",
					"Sabik",
					"Alkaid",
					"Merak",
					"Polaris",
					"Hamal",
					"Diphda",
					"Alpheratz",
					"Muphrid",
					"Wezen",
					"Arneb",
					"Mirzam",
					"Navi",
					"Ruchbah"]
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																builtInStars=chart_stars,
																yearSince2000=-31,
																displayStarNamesLabels=True,
																displayDeclinationNumbers=True,
																fig_plot_title=None,
																fig_plot_color="darkorchid",
																save_plot_name="rete_2.png")
	exit()
	#star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
	#				builtInStars=["Vega", "Arcturus", "Altair"],
	#				userDefinedStars=[exalibur_star, karaboudjan_star],
	#				displayStarNamesLabels=True,
	#				fig_plot_color="red",
	#				yearSince2000=-44000,
	#				showPlot=True)
	#exit()
	"""
	#star_chart_spherical_projection.plotStereographicProjection(builtInStars=["Polaris", "Vega", "Thuban", "Altair"],
	#						northOrSouth="North",
	#						displayStarNamesLabels=True,
	#						yearSince2000=13500,
	#						isPrecessionIncluded=True,
	#						fig_plot_color="red")
	#exit()
	#star_final_pos_dict = star_chart_spherical_projection.finalPositionOfStars(builtInStars=["Vega"], yearSince2000=11500, save_to_csv="final_star_positions.csv")
	#print(star_final_pos_dict)
	next_pole_star = star_chart_spherical_projection.predictPoleStar(yearSince2000=2000, northOrSouth="North")
	print(next_pole_star)
	exit()
	startYear = -15000
	endYear = 15000
	incrementYear = 5
	star_chart_spherical_projection.starPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=startYear,
														endYearSince2000=endYear,
														isPrecessionIncluded=True,
														incrementYear=incrementYear,
														save_to_csv=None)
	star_chart_spherical_projection.plotStarPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=startYear,
														endYearSince2000=endYear,
														isPrecessionIncluded=True,
														incrementYear=incrementYear,
														DecOrRA="D",
														save_plot_name="examples/plot_star_vega_declination_with_precession.png")
	star_chart_spherical_projection.plotStarPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=startYear,
														endYearSince2000=endYear,
														isPrecessionIncluded=True,
														incrementYear=incrementYear,
														DecOrRA="R",
														save_plot_name="examples/plot_star_vega_right_ascension_with_precession.png")
	star_chart_spherical_projection.plotStarPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=startYear,
														endYearSince2000=endYear,
														isPrecessionIncluded=False,
														incrementYear=incrementYear,
														DecOrRA="D",
														save_plot_name="examples/plot_star_vega_declination_without_precession.png")
	star_chart_spherical_projection.plotStarPositionOverTime(builtInStarName="Vega",
														newStar=None,
														startYearSince2000=startYear,
														endYearSince2000=endYear,
														isPrecessionIncluded=False,
														incrementYear=incrementYear,
														DecOrRA="R",
														save_plot_name="examples/plot_star_vega_right_ascension_without_precession.png")
	# note, includes endYear (0 to 9, every three = [0, 3, 6, 9], inclusive of start, inclusive of end
	exit()
	# Quickstart Graphs
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South",
																displayStarNamesLabels=False,
																yearSince2000=23,
																save_plot_name="examples/quickstart_south_2023.png")
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
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																builtInStars=["Vega", "Arcturus", "Altair"],
																userDefinedStars=[exalibur_star, karaboudjan_star],
																displayStarNamesLabels=True,
																fig_plot_color="red",
																yearSince2000=-39,
																save_plot_name="examples/quickstart_newstar_example.png")
	## Graphs for each plot Arguments
	# northOrSouth
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																save_plot_name="examples/northOrSouth_north.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South",
																displayStarNamesLabels=False,
																save_plot_name="examples/northOrSouth_south.png")
	# builtInStars
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																builtInStars=[],
																save_plot_name="examples/builtInStars_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																builtInStars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"],
																save_plot_name="examples/builtInStars_subset.png")
	# declination_min
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																declination_min=-30,
																save_plot_name="examples/declination_min_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																declination_min=10,
																save_plot_name="examples/declination_min_10.png")
	# yearSince2000
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																yearSince2000=0,
																save_plot_name="examples/yearSince2000_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																yearSince2000=-3100,
																save_plot_name="examples/yearSince2000_negative_3100.png")
	# displayStarNamesLabels
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=True,
																save_plot_name="examples/displayStarNamesLabels_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																save_plot_name="examples/displayStarNamesLabels_false.png")
	# displayDeclinationNumbers
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																displayDeclinationNumbers=True,
																save_plot_name="examples/displayDeclinationNumbers_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																displayDeclinationNumbers=False,
																save_plot_name="examples/displayDeclinationNumbers_false.png")
	# incrementBy
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																incrementBy=10,
																save_plot_name="examples/incrementBy_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=False,
																incrementBy=5,
																save_plot_name="examples/incrementBy_5.png")
	# isPrecessionIncluded
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																isPrecessionIncluded=True,
																yearSince2000=11500,
																save_plot_name="examples/isPrecessionIncluded_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																isPrecessionIncluded=False,
																yearSince2000=11500,
																save_plot_name="examples/isPrecessionIncluded_false.png")
	# maxMagnitudeFilter
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																maxMagnitudeFilter=None,
																save_plot_name="examples/maxMagnitudeFilter_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																maxMagnitudeFilter=1,
																save_plot_name="examples/maxMagnitudeFilter_1.png")
	# userDefinedStars
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
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																builtInStars=["Vega"],
																userDefinedStars=[],
																save_plot_name="examples/userDefinedStars_none.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																builtInStars=["Vega"],
																userDefinedStars=[exalibur_star, karaboudjan_star],
																save_plot_name="examples/userDefinedStars_included.png")
	# onlyDisplayUserStars
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																onlyDisplayUserStars=False,
																userDefinedStars=[exalibur_star, karaboudjan_star],
																save_plot_name="examples/onlyDisplayUserStars_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																onlyDisplayUserStars=True,
																userDefinedStars=[exalibur_star, karaboudjan_star],
																save_plot_name="examples/onlyDisplayUserStars_true.png")
	# fig_plot_title
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																fig_plot_title=None,
																save_plot_name="examples/fig_plot_title_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																fig_plot_title="This is a Example Title for a Star Chart",
																save_plot_name="examples/fig_plot_title_example.png")
	# fig_plot_color
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																fig_plot_color="C0",
																displayStarNamesLabels=False,
																save_plot_name="examples/fig_plot_color_default.png")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																fig_plot_color="darkorchid",
																displayStarNamesLabels=False,
																save_plot_name="examples/fig_plot_color_darkorchid.png")
	# Example Outputs:
	year_to_calculate = 11500

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
