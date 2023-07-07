# Pytest for finalPositionOfStars()
# centerline-width/: python3 -m pytest -v
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

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_finalPositionOfStars_builtInStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(builtInStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [builtInStars]: Must be a list, current type = '{0}'".format(error_output)

def test_finalPositionOfStars_builtInStarsInvalidStar(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(builtInStars=["Fake star", "VEga"])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [builtInStars]: 'Fake Star' not a star in current list of stars, please select one of the following: {0}".format(lst_of_current_stars)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_declinationMinInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_min=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Must be a int or float, current type = '{0}'".format(error_output)

def test_finalPositionOfStars_declinationMinInvalidRangeMin(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_min=-90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'"

def test_finalPositionOfStars_declinationMinInvalidRangeMax(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_min=90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_declinationMaxInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_max=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_max]: Must be a int or float, current type = '{0}'".format(error_output)

def test_finalPositionOfStars_declinationMaxInvalidRangeMin(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_max=-90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'"

def test_finalPositionOfStars_declinationMaxInvalidRangeMax(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(declination_max=90)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_yearSince2000InvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(yearSince2000=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [yearSince2000]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_finalPositionOfStars_isPrecessionIncludedInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(isPrecessionIncluded=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [isPrecessionIncluded]: Must be a bool, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_userDefinedStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(userDefinedStars=[invalid_input])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userDefinedStars]: {0} is not a valid newStar object (see: star_chart_spherical_projection.newStar)".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_finalPositionOfStars_onlyDisplayUserStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(onlyDisplayUserStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [onlyDisplayUserStars]: Must be a bool, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_finalPositionOfStars_saveToCsvInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(save_to_csv=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_csv]: Must be a str, current type = '{0}'".format(error_output)
