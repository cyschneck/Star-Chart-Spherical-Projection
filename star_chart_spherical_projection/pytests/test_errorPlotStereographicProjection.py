# Pytest for plotStereographicProjection()
# star_chart_spherical_projection/: python3 -m pytest -v
import re
import os

# External Python libraries (installed via pip install)
import pytest
import pandas as pd

# Internal star_chart_spherical_projection reference to access functions, global variables, and error handling
import star_chart_spherical_projection as scsp

invalid_non_str_options = [(1961, "<class 'int'>"),
                        (3.1415, "<class 'float'>"),
                        ([], "<class 'list'>"),
                        (False, "<class 'bool'>")]

invalid_non_bool_options = [(1961, "<class 'int'>"),
                        (3.1415, "<class 'float'>"),
                        ([], "<class 'list'>"),
                        ("string", "<class 'str'>")]

invalid_non_list_options = [(1961, "<class 'int'>"),
                        (3.1415, "<class 'float'>"),
                        ("string", "<class 'str'>"),
                        (False, "<class 'bool'>")]

invalid_non_int_options = [([], "<class 'list'>"),
                        ("string", "<class 'str'>"),
                        (3.1415, "<class 'float'>"),
                        (False, "<class 'bool'>")]

invalid_non_num_options = [([], "<class 'list'>"),
                        ("string", "<class 'str'>"),
                        (False, "<class 'bool'>")]

filepath_one_level_above = os.path.dirname(os.path.dirname(__file__))
star_csv_file = os.path.join(filepath_one_level_above, 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/star_data.csv
star_dataframe = pd.read_csv(star_csv_file)
star_dataframe = star_dataframe.sort_values(by=["Common Name"])
lst_of_current_stars = star_dataframe["Common Name"].tolist()

def test_plotStereographicProjection_poleInvalidOptions():
    with pytest.raises(ValueError, match=re.escape("[pole]: Pole options are ['North', 'South'], current option = 'Invalid'")):
        scsp.plot_stereographic_projection(pole="Invalid")

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_poleInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[pole]: Must be a str, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_plotStereographicProjection_includedStarsInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[included_stars]: Must be a list, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", included_stars=invalid_input)

def test_plotStereographicProjection_includedStarsInvalidStar():
    with pytest.raises(ValueError, match=re.escape(f"[included_stars]: 'Fake Star' not a star in current list of stars, please select one of the following: {lst_of_current_stars}")):
        scsp.plot_stereographic_projection(pole="North", included_stars=["Fake star", "VEga"])

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_declinationMinInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[declination_min]: Must be a int or float, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", declination_min=invalid_input)

def test_plotStereographicProjection_declinationMinInvalidRangeMin():
    with pytest.raises(ValueError, match=re.escape("[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'")):
        scsp.plot_stereographic_projection(pole="North", declination_min=-90)

def test_plotStereographicProjection_declinationMinInvalidRangeMax():
    with pytest.raises(ValueError, match=re.escape("[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'")):
        scsp.plot_stereographic_projection(pole="North", declination_min=90)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_yearSince2000InvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[year_since_2000]: Must be a int or float, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", year_since_2000=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_displayLabelInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[display_labels]: Must be a bool, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", display_labels=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_displayDeclinationNumbersInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[display_dec]: Must be a bool, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", display_dec=invalid_input)

def test_plotStereographicProjection_incrementInvalidOptions():
    with pytest.raises(ValueError, match=re.escape("[increment]: Must be one of the options [1, 5, 10], current value = '2'")):
        scsp.plot_stereographic_projection(pole="North", increment=2)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_int_options)
def test_plotStereographicProjection_incrementInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[increment]: Must be a int, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", increment=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_isPrecessionInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[is_precession]: Must be a bool, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", is_precession=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_maxMagnitudeInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[max_magnitude]: Must be a int or float, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", max_magnitude=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_showPlotInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[show_plot]: Must be a bool, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", show_plot=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_figPlotTitleInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[fig_plot_title]: Must be a string, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", fig_plot_title=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_figPlotColorInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[fig_plot_color]: Must be a string, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", fig_plot_color=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_figsizeNInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[figsize_n]: Must be a int or float, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", figsize_n=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_figsizeDPIInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[figsize_dpi]: Must be a int or float, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", figsize_dpi=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_savePlotNameInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[save_plot_name]: Must be a string, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", save_plot_name=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_addedStarsInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[added_stars]: {error_output} is not a valid new star object (see: star_chart_spherical_projection.add_new_star)")):
        scsp.plot_stereographic_projection(pole="North", added_stars=[invalid_input])

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_onlyAddedStarsInvalidTypes(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[only_added_stars]: Must be a bool, current type = '{error_output}'")):
        scsp.plot_stereographic_projection(pole="North", only_added_stars=invalid_input)
