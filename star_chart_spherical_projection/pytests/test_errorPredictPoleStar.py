# Pytest for predict_pole_star()
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
    with pytest.raises(ValueError, match=re.escape("[year_since_2000]: year_since_2000 is required")):
        scsp.predict_pole_star(year_since_2000=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_predictPoleStar_yearSince2000InvalidType( invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[year_since_2000]: Must be a int or float, current type = '{error_output}'")):
        scsp.predict_pole_star(year_since_2000=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_predictPoleStar_poleInvalidType(invalid_input, error_output):
    with pytest.raises(ValueError, match=re.escape(f"[pole]: Must be a str, current type = '{error_output}'")):
        scsp.predict_pole_star(year_since_2000=0, pole=invalid_input)

def test_predictPoleStar_poleInvalidOptions():
    with pytest.raises(ValueError, match=re.escape("[pole]: Must be a 'North' or 'South', currently = 'Invalid'")):
        scsp.predict_pole_star(year_since_2000=0, pole="Invalid")
