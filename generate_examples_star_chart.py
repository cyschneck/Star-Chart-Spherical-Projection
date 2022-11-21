# Test generate_star_chart functions
# python3 test_generate_star_chart.py
import star_chart_spherical_projection

if __name__ == '__main__':
	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="North", 
																displayStarNamesLabels=False,
																yearSince2000=-31,
																fig_plot_color="red",
																save_plot_name="examples/north_testing")

	star_chart_spherical_projection.plotStereographicProjection(northOrSouth="South", 
																displayStarNamesLabels=False,
																yearSince2000=-31,
																fig_plot_color="royalblue",
																save_plot_name="examples/south_testing")
