# Pytest for starClass()
# star_chart_spherical_projection/: python -m pytest -v
import re

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

def test_starClass_starNameRequired():
	with pytest.raises(ValueError, match=re.escape("[starName]: starName is required")):
		scsp.newStar(starName=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_starNameInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[starName]: Must be a str, current type = '{error_output}'")):
		scsp.newStar(starName=invalid_input)

def test_starClass_RARequired():
	with pytest.raises(ValueError, match=re.escape("[ra]: Right Ascension is required")):
		scsp.newStar(starName="testing Star",
					ra=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_RAInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[ra]: Must be a str, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra=invalid_input)

def test_starClass_RAInvalidFormat():
	with pytest.raises(ValueError, match=re.escape("[ra]: Right Ascension must be three parts '[HH, MM, SS]' (Hours, Minutes, Seconds), currently  = '['1', '2', '3', '4']'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3.4")

def test_starClass_RAInvalidTimeFormat():
	with pytest.raises(ValueError, match=re.escape("[ra]: Each part of the Right Ascension must be an integar, 'a' current type = <class 'str'>")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.a")

def test_starClass_DecRequired():
	with pytest.raises(ValueError, match=re.escape("[dec]: Declination is required")):
		scsp.newStar(starName="testing Star",
					ra="1.2.3",
					dec=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_DECInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[dec]: Must be a int or float, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[properMotionSpeed]: Must be a int or float, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeed=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionAngleInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[properMotionAngle]: Must be a int or float, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeed=123.4,
					properMotionAngle=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedRAInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[properMotionSpeedRA]: Must be a int or float, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeedRA=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedDecInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[properMotionSpeedDec]: Must be a int or float, current type = '{error_output}'")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					properMotionSpeedDec=invalid_input)

def test_starClass_properMotionSpeedAngleOrRADecRequired():
	with pytest.raises(ValueError, match=re.escape("Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)

def test_starClass_properMotionSpeedAngleOrRADecOnlyOneRequired():
	with pytest.raises(ValueError, match=re.escape("Either properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle is required, not both")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)

def test_starClass_properMotionSpeedDecExtra():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeedDec]: With properMotionSpeed/properMotionAngle set, properMotionSpeedDec should be None")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=None)

def test_starClass_properMotionSpeedRAExtra():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeedRA]: With properMotionSpeed/properMotionAngle set, properMotionSpeedRA should be None")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=32.1,
					properMotionSpeedDec=None,
					properMotionSpeedRA=65.4)

def test_starClass_properMotionSpeedExtra():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeed]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionSpeed should be None")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)

def test_starClass_properMotionAngleExtra():
	with pytest.raises(ValueError, match=re.escape("[properMotionAngle]: With properMotionSpeedRA/properMotionSpeedDec set, properMotionAngle should be None")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=32.1,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=65.4)

def test_starClass_properMotionSpeedDecRequiredWithRA():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeedDec]: With properMotionSpeedRA set, properMotionSpeedDec is required")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=65.4)

def test_starClass_properMotionSpeedDecRequiredWithRA():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeedRA]: With properMotionSpeedDec set, properMotionSpeedRA is required")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=None,
					properMotionSpeedDec=45.6,
					properMotionSpeedRA=None)

def test_starClass_properMotionAngleRequiredWithSpeed():
	with pytest.raises(ValueError, match=re.escape("[properMotionAngle]: With properMotionSpeed set, properMotionAngle is required")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)

def test_starClass_properMotionSpeedRequiredWithAngle():
	with pytest.raises(ValueError, match=re.escape("[properMotionSpeed]: With properMotionAngle set, properMotionSpeed is required")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=32.1,
					properMotionSpeedDec=None,
					properMotionSpeedRA=None)

def test_starClass_properMotionSpeedvsDec():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedDec")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=34.5,
					properMotionSpeedRA=None)

def test_starClass_properMotionSpeedvsRA():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionSpeed/properMotionSpeedRA")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=12.3,
					properMotionAngle=None,
					properMotionSpeedDec=None,
					properMotionSpeedRA=34.5)

def test_starClass_properMotionAnglevsDec():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedDec")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=12.3,
					properMotionSpeedDec=34.5,
					properMotionSpeedRA=None)

def test_starClass_properMotionAnglevsRA():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of properMotionSpeedRA/properMotionSpeedDec or properMotionSpeed/properMotionAngle, not properMotionAngle/properMotionSpeedRA")):
		scsp.newStar(starName="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitudeVisual=1.2,
					properMotionSpeed=None,
					properMotionAngle=12.3,
					properMotionSpeedDec=None,
					properMotionSpeedRA=34.5)
