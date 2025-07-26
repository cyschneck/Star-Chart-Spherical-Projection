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
    # test converting back and forth between hours and radians
    # list of known edge cases with less than 2 minutes difference:
    edge_case_names = ["Atlas", "Bellatrix", "Cervantes", "Chechia", "Danfeng", "Diya", "Funi", "Gacrux", "Gomeisa", "Imai", "Jishui", "Khambalia", "La Superba", "Larawag", "Markeb", "Matar", "Meissa", "Mekbuda", "Mintaka", "Nikawiy", "Pincoya", "Pipoltr", "Rasalnaqa", "Sadalbari", "Sirius", "Subra", "Syrma", "Sāmaya", "Tianfu", "Wasat", "Wouri", "Zembra", "Zosma", "Zubeneschamali"]
    found_edge_case = []

    for index, row in star_dataframe.iterrows():
        star_ra = row["Right Ascension (HH.MM.SS)"]
        print("\n")
        print(list(row))
        print(star_ra)
        ra_in_radians = scsp._ra_to_radians([list(row)])[0]
        print(ra_in_radians[1])
        ra_in_hours = scsp._radians_to_ra(ra_in_radians[1])
        print(ra_in_hours)

        star_h, star_m, star_s = star_ra.split(".")
        second_degrees = 10**(len(str(int(star_s)))-2) # convert seconds to a float
        star_s = float(star_s)/second_degrees
        hours, minutes, seconds = ra_in_hours.split(".")
        second_degrees = 10**(len(str(seconds))-2)
        seconds = float(seconds)/second_degrees # convert seconds to a float

        assert star_h == hours
        # minutes and seconds can vary due to precession errors
        try:
            assert star_m == minutes
            # seconds can be off due to precession errors when converting back and forth between hours and radians
            assert star_s  == pytest.approx(seconds)
        except Exception:
            # some edge cases round  minutes (for example: 49.09 to 50.3)
            # combine minutes and seconds to a float to compare
            found_edge_case.append(row["Common Name"])
            if row["Common Name"] not in edge_case_names:
                assert False
            star_ms = float(".".join(star_ra.split(".")[1:]))
            full_ms = float(".".join(ra_in_hours.split(".")[1:]))
            assert abs(star_ms - full_ms) < 2

    assert found_edge_case == edge_case_names # verify that edge cases do not change

def test_starting_year_0_data():
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
        print(f"\n{index}")
        print(current)
        print(start)
        
        assert start[0] == current[0] # compare Common Names
        
        assert abs(start[2] - current[2]) < 0.0001 # compare Declination values

        # compare Right Acensions
        star_h, star_m, star_s = start[1].split(".")
        second_degrees = 10**(len(str(int(star_s)))-2) # convert seconds to a float
        star_s = float(star_s)/second_degrees
        hours, minutes, seconds = current[1].split(".")
        second_degrees = 10**(len(str(seconds))-2)
        seconds = float(seconds)/second_degrees # convert seconds to a float

        assert star_h == hours
        # minutes and seconds can vary due to precession errors
        try:
            assert star_m == minutes
            # seconds can be off due to precession errors when converting back and forth between hours and radians
            assert star_s  == pytest.approx(seconds)
        except Exception:
            # some edge cases round  minutes (for example: 49.09 to 50.3)
            # combine minutes and seconds to a float to compare
            star_ms = float(".".join(start[1].split(".")[1:]))
            full_ms = float(".".join(current[1].split(".")[1:]))
            assert abs(star_ms - full_ms) < 2
