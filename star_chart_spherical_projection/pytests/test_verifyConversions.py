# Pytest for converting right acension values
# star_chart_spherical_projection/: python -m pytest
# python -m pytest -k test_verifyConversions.py -xv
from pathlib import Path
import os

# External Python libraries (installed via pip install)
import pytest
import pandas as pd

# Internal star_chart_spherical_projection reference to access functions, global variables, and error handling
import star_chart_spherical_projection as scsp

filepath_one_level_above = os.path.dirname(os.path.dirname(__file__))
star_csv_file = os.path.join(filepath_one_level_above, 'data', 'stars_with_data.csv')  # get file's directory, up one level, /data/star_data.csv
star_dataframe = pd.read_csv(star_csv_file)

def test_convertRAtoRadiansAndBack():
    # test converting back and forth between hours and radians with built-in functions

    for index, row in star_dataframe.iterrows(): # compare output to starting backend data (stars_with_data.csv)
        star_ra = row["Right Ascension (HH.MM.SS)"]
        ra_in_radians = scsp._ra_to_radians([list(row)])[0]
        ra_in_hours = scsp._radians_to_ra(ra_in_radians[1])
        
        data_h, data_m, data_s = star_ra.split(".")
        star_h, star_m, star_s = ra_in_hours.split(".")
        
        
        assert data_h == star_h
        assert data_m == star_m
        try:
            assert data_s == star_s
        except Exception:
            # check that any changes in seconds are minor
            data_s = float("0." + data_s)
            star_s = float("0." + star_s)
            assert (abs(data_s - star_s) < 0.000001)

def test_starting_year_0_with_builtin_data():
    # verify data generated for Year 0 (RA and Declination) matches current star_with_data.csv within expected range
    starting_csv = (Path(__file__).parent).joinpath('examples',
                                                    "year_0_stars_pos.csv")
    current_csv = (Path(__file__).parent.parent).joinpath('data',
                                                    "stars_with_data.csv")

    start_pos = pd.read_csv(starting_csv)
    current_pos = pd.read_csv(current_csv)
    for index, row in current_pos.iterrows():
        start = list(start_pos.iloc[index])
        current = list(current_pos.iloc[index])[:3]
        
        assert start[0] == current[0] # compare Common Names
        
        assert abs(start[2] - current[2]) < 0.0001 # compare Declination values

        # Compare Right Acensions
        hours, minutes, seconds = start[1].split(".")
        star_h, star_m, star_s = current[1].split(".")
        # convert seconds to a float
        seconds = float("0." + str(seconds))
        star_s = float("0." + str(star_s))

        assert star_h == hours
        assert star_m == minutes

        try:
            assert star_s == seconds
        except Exception:
            # account for minor differences in seconds based on converting to radians and back for some stars
            edge_cases = ["Ceibo", "Polaris", "Polaris Australis", "Yildun"] # some stars are rounded when converting from degrees to radians and back (TODO: research potential fix)
            if start[0] not in edge_cases:
                assert (abs(star_s - seconds) < 0.006)
            else:
                assert (abs(star_s - seconds) < 0.045)
