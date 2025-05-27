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
	with pytest.raises(ValueError, match=re.escape("[star_name]: star_name is required")):
		scsp.add_new_star(star_name=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_starNameInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[star_name]: Must be a str, current type = '{error_output}'")):
		scsp.add_new_star(star_name=invalid_input)

def test_starClass_RARequired():
	with pytest.raises(ValueError, match=re.escape("[ra]: Right Ascension is required")):
		scsp.add_new_star(star_name="testing Star",
					ra=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_str_options)
def test_starClass_RAInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[ra]: Must be a str, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra=invalid_input)

def test_starClass_RAInvalidFormat():
	with pytest.raises(ValueError, match=re.escape("[ra]: Right Ascension must be three parts '[HH, MM, SS]' (Hours, Minutes, Seconds), currently  = '['1', '2', '3', '4']'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3.4")

def test_starClass_RAInvalidTimeFormat():
	with pytest.raises(ValueError, match=re.escape("[ra]: Each part of the Right Ascension must be an integar, 'a' current type = <class 'str'>")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.a")

def test_starClass_DecRequired():
	with pytest.raises(ValueError, match=re.escape("[dec]: Declination is required")):
		scsp.add_new_star(star_name="testing Star",
					ra="1.2.3",
					dec=None)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_DECInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[dec]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[pm_speed]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					pm_speed=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionAngleInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[pm_angle]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					pm_speed=123.4,
					pm_angle=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedRAInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[pm_speed_ra]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					pm_speed_ra=invalid_input)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_properMotionSpeedDecInvalidTypes(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[pm_speed_dec]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					pm_speed_dec=invalid_input)

def test_starClass_properMotionSpeedAngleOrRADecRequired():
	with pytest.raises(ValueError, match=re.escape("Either pm_speed_ra/pm_speed_dec or pm_speed/pm_angle is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=None,
					pm_speed_dec=None,
					pm_speed_ra=None)

def test_starClass_properMotionSpeedAngleOrRADecOnlyOneRequired():
	with pytest.raises(ValueError, match=re.escape("Either pm_speed_ra/pm_speed_dec or pm_speed/pm_angle is required, not both")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=32.1,
					pm_speed_dec=45.6,
					pm_speed_ra=65.4)

def test_starClass_properMotionSpeedDecExtra():
	with pytest.raises(ValueError, match=re.escape("[pm_speed_dec]: With pm_speed/pm_angle set, pm_speed_dec should be None")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=32.1,
					pm_speed_dec=45.6,
					pm_speed_ra=None)

def test_starClass_properMotionSpeedRAExtra():
	with pytest.raises(ValueError, match=re.escape("[pm_speed_ra]: With pm_speed/pm_angle set, pm_speed_ra should be None")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=32.1,
					pm_speed_dec=None,
					pm_speed_ra=65.4)

def test_starClass_properMotionSpeedExtra():
	with pytest.raises(ValueError, match=re.escape("[pm_speed]: With pm_speed_ra/pm_speed_dec set, pm_speed should be None")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=None,
					pm_speed_dec=45.6,
					pm_speed_ra=65.4)

def test_starClass_properMotionAngleExtra():
	with pytest.raises(ValueError, match=re.escape("[pm_angle]: With pm_speed_ra/pm_speed_dec set, pm_angle should be None")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=32.1,
					pm_speed_dec=45.6,
					pm_speed_ra=65.4)

def test_starClass_properMotionSpeedDecRequiredWithRA():
	with pytest.raises(ValueError, match=re.escape("[pm_speed_dec]: With pm_speed_ra set, pm_speed_dec is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=None,
					pm_speed_dec=None,
					pm_speed_ra=65.4)

def test_starClass_properMotionSpeedDecRequiredWithRA():
	with pytest.raises(ValueError, match=re.escape("[pm_speed_ra]: With pm_speed_dec set, pm_speed_ra is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=None,
					pm_speed_dec=45.6,
					pm_speed_ra=None)

def test_starClass_properMotionAngleRequiredWithSpeed():
	with pytest.raises(ValueError, match=re.escape("[pm_angle]: With pm_speed set, pm_angle is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=None,
					pm_speed_dec=None,
					pm_speed_ra=None)

def test_starClass_properMotionSpeedRequiredWithAngle():
	with pytest.raises(ValueError, match=re.escape("[pm_speed]: With pm_angle set, pm_speed is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=32.1,
					pm_speed_dec=None,
					pm_speed_ra=None)

def test_starClass_properMotionSpeedvsDec():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_speed/pm_speed_dec")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=None,
					pm_speed_dec=34.5,
					pm_speed_ra=None)

def test_starClass_properMotionSpeedvsRA():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_speed/pm_speed_ra")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=12.3,
					pm_angle=None,
					pm_speed_dec=None,
					pm_speed_ra=34.5)

def test_starClass_properMotionAnglevsDec():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_angle/pm_speed_dec")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=12.3,
					pm_speed_dec=34.5,
					pm_speed_ra=None)

def test_starClass_properMotionAnglevsRA():
	with pytest.raises(ValueError, match=re.escape("Should be a pair of pm_speed_ra/pm_speed_dec or pm_speed/pm_angle, not pm_angle/pm_speed_ra")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=1.2,
					pm_speed=None,
					pm_angle=12.3,
					pm_speed_dec=None,
					pm_speed_ra=34.5)

def test_starClass_magnitudeRequired():
	with pytest.raises(ValueError, match=re.escape("[magnitude]: magnitude is required")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=None,
					pm_speed=12.3,
					pm_angle=32.1)

@pytest.mark.parametrize("invalid_input, error_output", invalid_non_num_options)
def test_starClass_magnitudeRequired(invalid_input, error_output):
	with pytest.raises(ValueError, match=re.escape(f"[magnitude]: Must be a int or float, current type = '{error_output}'")):
		scsp.add_new_star(star_name="Testing Star",
					ra="1.2.3",
					dec=12.3,
					magnitude=invalid_input,
					pm_speed=12.3,
					pm_angle=32.1)
