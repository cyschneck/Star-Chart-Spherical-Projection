# Pytest for starClass()
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

invalid_non_num_options = [([], "<class 'list'>"),
						("string", "<class 'str'>"),
						(False, "<class 'bool'>")]

def test_starClass_starNameRequired(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [starName]: starName is required"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_starNameInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [starName]: Must be a str, current type = '{0}'".format(error_output)

def test_starClass_RARequired(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="testing Star",
					ra=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [ra]: Right Ascension is required"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_RAInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [ra]: Must be a str, current type = '{0}'".format(error_output)

def test_starClass_RAInvalidFormat(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3.4")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [ra]: Right Ascension must be three parts '[HH, MM, SS]' (Hours, Minutes, Seconds), currently  = '['1', '2', '3', '4']'"

def test_starClass_RAInvalidTimeFormat(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.a")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [ra]: Each part of the Right Ascension must be an integar, 'a' current type = <class 'str'>"


def test_starClass_DecRequired(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="testing Star",
					ra="1.2.3",
					dec=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [dec]: Declination is required"

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_DECInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [dec]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeed=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeed]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionAngleInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeed=123.4,
					properMotionAngle=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionAngle]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedRAInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeedRA=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedRA]: Must be a int or float, current type = '{0}'".format(error_output)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedDecInvalidTypes(caplog, invalid_input, error_output):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeedDec=invalid_input)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedDec]: Must be a int or float, current type = '{0}'".format(error_output)

def test_starClass_properMotionSpeedAngleOrRADecRequired(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required"

def test_starClass_properMotionSpeedAngleOrRADecOnlyOneRequired(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required, not both"

def test_starClass_properMotionSpeedDecExtra(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedDec]: With properMotionSpeed/properMotionAngle set, properMotionSpeedDec should be None"

def test_starClass_properMotionSpeedRAExtra(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=None,
					properMotionSpeedRA=65.4)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedRA]: With properMotionSpeed/properMotionAngle set, properMotionSpeedRA should be None"

def test_starClass_properMotionSpeedExtra(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeed]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionSpeed should be None"

def test_starClass_properMotionAngleExtra(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionAngle]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionAngle should be None"

def test_starClass_properMotionSpeedDecRequiredWithRA(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=65.4)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedDec]: With properMotionSpeedRA set, properMotionSpeedDec is required"

def test_starClass_properMotionSpeedDecRequiredWithRA(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeedRA]: With properMotionSpeedDec set, properMotionSpeedRA is required"

def test_starClass_properMotionAngleRequiredWithSpeed(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionAngle]: With properMotionSpeed set, properMotionAngle is required"

def test_starClass_properMotionSpeedRequiredWithAngle(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=32.1,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [properMotionSpeed]: With properMotionAngle set, properMotionSpeed is required"

def test_starClass_properMotionSpeedvsDec(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=34.5,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedDec"

def test_starClass_properMotionSpeedvsRA(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=34.5)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedRA"

def test_starClass_properMotionAnglevsDec(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=12.3,
					properMotionSpeedDec=34.5,
					properMotionSpeedRA=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedDec"

def test_starClass_properMotionAnglevsRA(caplog):
	# Test:
	with pytest.raises(SystemExit):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=12.3,
					properMotionSpeedDec=None,
					properMotionSpeedRA=34.5)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedRA"
