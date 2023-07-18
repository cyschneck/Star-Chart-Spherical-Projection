# Pytest for plotStereographicProjection()
# star_chart_spherical_projection/: python3 -m pytest -v
import logging
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
star_csv_file = os.path.join(filepath_one_level_above, 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
star_dataframe = pd.read_csv(star_csv_file)
star_dataframe = star_dataframe.sort_values(by=["Star Name"])
lst_of_current_stars = star_dataframe["Star Name"].tolist()

def test_plotStereographicProjection_northOrSouthInvalidOptions(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="Invalid")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [northOrSouth]: Hemisphere options are ['North', 'South'], current option = 'Invalid'"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_northOrSouthInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [northOrSouth]: Must be a str, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_plotStereographicProjection_builtInStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", builtInStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [builtInStars]: Must be a list, current type = '{0}'".format(error_output)

def test_plotStereographicProjection_builtInStarsInvalidStar(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", builtInStars=["Fake star", "VEga"])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [builtInStars]: 'Fake Star' not a star in current list of stars, please select one of the following: {0}".format(lst_of_current_stars)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_declinationMinInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", declination_min=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Must be a int or float, current type = '{0}'".format(error_output)

def test_plotStereographicProjection_declinationMinInvalidRangeMin(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", declination_min=-90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'"

def test_plotStereographicProjection_declinationMinInvalidRangeMax(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", declination_min=90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_yearSince2000InvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", yearSince2000=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [yearSince2000]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_displayStarNamesLabelsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", displayStarNamesLabels=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [displayStarNamesLabels]: Must be a bool, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_displayDeclinationNumbersInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", displayDeclinationNumbers=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [displayDeclinationNumbers]: Must be a bool, current type = '{0}'".format(error_output)

def test_plotStereographicProjection_incrementByInvalidOptions(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", incrementBy=2)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [incrementBy]: Must be one of the options [1, 5, 10], current value = '2'"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_int_options)
def test_plotStereographicProjection_incrementByInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", incrementBy=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [incrementBy]: Must be a int, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_isPrecessionIncludedInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", isPrecessionIncluded=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [isPrecessionIncluded]: Must be a bool, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_maxMagnitudeFilterInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", maxMagnitudeFilter=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [maxMagnitudeFilter]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_showPlotInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", showPlot=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [showPlot]: Must be a bool, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_figPlotTitleInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", fig_plot_title=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [fig_plot_title]: Must be a string, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_figPlotColorInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", fig_plot_color=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [fig_plot_color]: Must be a string, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_figsizeNInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", figsize_n=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_figsizeDPIInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", figsize_dpi=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_plotStereographicProjection_savePlotNameInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", save_plot_name=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_plot_name]: Must be a string, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_plotStereographicProjection_userDefinedStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", userDefinedStars=[invalid_input])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userDefinedStars]: {0} is not a valid newStar object (see: star_chart_spherical_projection.newStar)".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_plotStereographicProjection_onlyDisplayUserStarsInvalidTypes(caplog, invalid_input, error_output):
	#userDefinedStars
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", onlyDisplayUserStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [onlyDisplayUserStars]: Must be a bool, current type = '{0}'".format(error_output)
