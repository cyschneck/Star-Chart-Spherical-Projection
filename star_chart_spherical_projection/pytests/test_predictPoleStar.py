# Pytest for predictPoleStar()
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

invalid_non_num_options = [([], "<class 'list'>"),
						("string", "<class 'str'>"),
						(False, "<class 'bool'>")]

def test_predictPoleStar_yearSince2000Required(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.predictPoleStar(yearSince2000=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [yearSince2000]: yearSince2000 is required"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_predictPoleStar_yearSince2000InvalidType(caplog, invalid_input, error_output):
	with pytest.raises(SystemExit):
		scsp.predictPoleStar(yearSince2000=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [yearSince2000]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_predictPoleStar_northOrSouthInvalidType(caplog, invalid_input, error_output):
	with pytest.raises(SystemExit):
		scsp.predictPoleStar(yearSince2000=0, northOrSouth=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [northOrSouth]: Must be a str, current type = '{0}'".format(error_output)

def test_predictPoleStar_northOrSouthInvalidOptions(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.predictPoleStar(yearSince2000=0, northOrSouth="Invalid")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [northOrSouth]: Must be a 'North' or 'South', currently = 'Invalid'"
