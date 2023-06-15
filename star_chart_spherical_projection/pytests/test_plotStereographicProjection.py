# Pytest for plotStereographicProjection()
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
def test_plotStereographicProjection_userListOfStarsInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", userListOfStars=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userListOfStars]: Must be a list, current type = '{0}'".format(error_output)

def test_plotStereographicProjection_userListOfStarsInvalidStar(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.plotStereographicProjection(northOrSouth="North", userListOfStars=["Fake star", "VEga"])
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [userListOfStars]: 'Fake Star' not a star in current list of stars, please select one of the following: ['Acamar', 'Achernar', 'Acrab', 'Acrux', 'Adhara', 'Aldebaran', 'Alderamin', 'Algieba', 'Algol', 'Alhena', 'Alioth', 'Alkaid', 'Almach', 'Alnilam', 'Alnitak', 'Alphard', 'Alphecca', 'Alpheratz', 'Altair', 'Aludra', 'Ankaa', 'Antares', 'Arcturus', 'Arneb', 'Ascella', 'Aspidiske', 'Atria', 'Avior', 'Bellatrix', 'Beta Hydri', 'Beta Phoenicis', 'Betelgeuse', 'Canopus', 'Capella', 'Caph', 'Castor', 'Cebalrai', 'Celaeno', 'Chara', 'Cor-Caroli', 'Cursa', 'Delta Crucis', 'Deneb', 'Denebola', 'Diphda', 'Dschubba', 'Dubhe', 'Elnath', 'Eltanin', 'Enif', 'Formalhaut', 'Gacrux', 'Gamma Phoenicis', 'Gienah', 'Hadar', 'Hamal', 'Kochab', 'Kornephoros', 'Lesath', 'Markab', 'Megrez', 'Meissa', 'Menkalinan', 'Menkar', 'Menkent', 'Merak', 'Miaplacidus', 'Mimosa', 'Mintaka', 'Mirach', 'Mirfak', 'Mirzam', 'Mizar', 'Muphrid', 'Naos', 'Navi', 'Nunki', 'Peacock', 'Phact', 'Phecda', 'Polaris', 'Pollux', 'Procyon', 'Rasalhague', 'Rastaban', 'Regulus', 'Rigel', 'Ruchbah', 'Sabik', 'Sadr', 'Saiph', 'Sargas', 'Scheat', 'Schedar', 'Segin', 'Seginus', 'Shaula', 'Sheratan', 'Sirius', 'Spica', 'Suhail', 'Tarazed', 'Unukalhai', 'Vega', 'Wezen', 'Zosma', 'Zubeneschamali']"

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
