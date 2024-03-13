# Pytest for predictPoleStar()
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

invalid_non_num_options = [([], "<class 'list'>"),
						("string", "<class 'str'>"),
						(False, "<class 'bool'>")]

def test_predictPoleStar_yearSince2000Required():
	with pytest.raises(ValueError, match=re.escape("[yearSince2000]: yearSince2000 is required")):
		scsp.predictPoleStar(yearSince2000=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_predictPoleStar_yearSince2000InvalidType( invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[yearSince2000]: Must be a int or float, current type = '{error_output}'")):
		scsp.predictPoleStar(yearSince2000=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_predictPoleStar_northOrSouthInvalidType(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[northOrSouth]: Must be a str, current type = '{error_output}'")):
		scsp.predictPoleStar(yearSince2000=0, northOrSouth=invalid_input)

def test_predictPoleStar_northOrSouthInvalidOptions():
	with pytest.raises(ValueError, match=re.escape("[northOrSouth]: Must be a 'North' or 'South', currently = 'Invalid'")):
		scsp.predictPoleStar(yearSince2000=0, northOrSouth="Invalid")
