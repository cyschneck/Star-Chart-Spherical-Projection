# Pytest for finalPositionOfStars()
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
star_csv_file = os.path.join(filepath_one_level_above, 'data', 'star_data.csv')  # get file's directory, up one level, /data/star_data.csv
star_dataframe = pd.read_csv(star_csv_file)
star_dataframe = star_dataframe.sort_values(by=["Star Name"])
lst_of_current_stars = star_dataframe["Star Name"].tolist()

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_finalPositionOfStars_builtInStarsInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[builtInStars]: Must be a list, current type = '{error_output}'")):
		scsp.finalPositionOfStars(builtInStars=invalid_input)

def test_finalPositionOfStars_builtInStarsInvalidStar():
	with pytest.raises(ValueError, match=re.escape(f"[builtInStars]: 'Fake Star' not a star in current list of stars, please select one of the following: {lst_of_current_stars}")):
		scsp.finalPositionOfStars(builtInStars=["Fake star", "VEga"])

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_declinationMinInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[declination_min]: Must be a int or float, current type = '{error_output}'")):
		scsp.finalPositionOfStars(declination_min=invalid_input)

def test_finalPositionOfStars_declinationMinInvalidRangeMin():
	with pytest.raises(ValueError, match=re.escape("[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'")):
		scsp.finalPositionOfStars(declination_min=-90)

def test_finalPositionOfStars_declinationMinInvalidRangeMax():
	with pytest.raises(ValueError, match=re.escape("[declination_min]: Minimum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'")):
		scsp.finalPositionOfStars(declination_min=90)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_declinationMaxInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[declination_max]: Must be a int or float, current type = '{error_output}'")):
		scsp.finalPositionOfStars(declination_max=invalid_input)

def test_finalPositionOfStars_declinationMaxInvalidRangeMin():
	with pytest.raises(ValueError, match=re.escape("[declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '-90'")):
		scsp.finalPositionOfStars(declination_max=-90)

def test_finalPositionOfStars_declinationMaxInvalidRangeMax():
	with pytest.raises(ValueError, match=re.escape(f"[declination_max]: Maximum declination must lie between -90 and +90 (-89 to 89) [recommended by default: north=-30, south=30], current minimum = '90'")):
		scsp.finalPositionOfStars(declination_max=90)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_yearSince2000InvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"yearSince2000]: Must be a int or float, current type = '{error_output}'")):
		scsp.finalPositionOfStars(yearSince2000=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_finalPositionOfStars_isPrecessionIncludedInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[isPrecessionIncluded]: Must be a bool, current type = '{error_output}'")):
		scsp.finalPositionOfStars(isPrecessionIncluded=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_finalPositionOfStars_userDefinedStarsInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[userDefinedStars]: Must be a list, current type = '{error_output}'")):
		scsp.finalPositionOfStars(userDefinedStars=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_finalPositionOfStars_userDefinedStarsInvalidStarTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[userDefinedStars]: {error_output} is not a valid newStar object (see: star_chart_spherical_projection.newStar)")):
		scsp.finalPositionOfStars(userDefinedStars=[invalid_input])

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_bool_options)
def test_finalPositionOfStars_onlyDisplayUserStarsInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[onlyDisplayUserStars]: Must be a bool, current type = '{error_output}'")):
		scsp.finalPositionOfStars(onlyDisplayUserStars=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_finalPositionOfStars_saveToCsvInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[save_to_csv]: Must be a str, current type = '{error_output}'")):
		scsp.finalPositionOfStars(save_to_csv=invalid_input)

def test_finalPositionOfStars_saveToCsvInvalidExtension():
	with pytest.raises(ValueError, match=re.escape(f"[save_to_csv]: Extension must be a .csv file, current extension = 'txt'")):
		scsp.finalPositionOfStars(save_to_csv="output_file.txt")
