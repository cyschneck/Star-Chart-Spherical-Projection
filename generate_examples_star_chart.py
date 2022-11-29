# Test generate_star_chart functions
# python3 test_generate_star_chart.py
import star_chart_spherical_projection

if __name__ == '__main__':
	## Northern Hemisphere: Without and With Precession
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North",
																displayStarNamesLabels=True,
																yearSince2000=11000,
																isPrecessionIncluded=False,
																fig_plot_color="red",
																save_plot_name="examples/north_with_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=True,
																yearSince2000=11000,
																isPrecessionIncluded=True,
																fig_plot_color="red",
																save_plot_name="examples/north_with_labels_with_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=False,
																yearSince2000=11000,
																isPrecessionIncluded=False,
																fig_plot_color="red",
																save_plot_name="examples/north_without_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=False,
																yearSince2000=11000,
																isPrecessionIncluded=True,
																fig_plot_color="red",
																save_plot_name="examples/north_without_labels_with_precession")

	## Southern Hemisphere: Without and With Precession
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=True,
																yearSince2000=11000,
																isPrecessionIncluded=False,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_with_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=True,
																yearSince2000=11000,
																isPrecessionIncluded=True,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_with_labels_with_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=False,
																yearSince2000=11000,
																isPrecessionIncluded=False,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_without_labels_without_precession")
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=False,
																yearSince2000=11000,
																isPrecessionIncluded=True,
																fig_plot_color="cornflowerblue",
																save_plot_name="examples/south_without_labels_with_precession")

