# Pytest for finalPositionOfStars()
# centerline-width/: python3 -m pytest -v
import logging

# External Python libraries (installed via pip install)
import pytest

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

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_list_options)
def test_finalPositionOfStars_userListOfStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(userListOfStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userListOfStars]: Must be a list, current type = '{0}'".format(error_output)

def test_finalPositionOfStars_userListOfStarsInvalidStar(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.finalPositionOfStars(userListOfStars=["Fake star", "VEga"])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userListOfStars]: 'Fake Star' not a star in current list of stars, please select one of the following: ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']"

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
