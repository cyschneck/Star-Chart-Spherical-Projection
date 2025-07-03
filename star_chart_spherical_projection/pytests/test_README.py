# Pytest for README.md page
# star_chart_spherical_projection/: python -m pytest
# python -m pytest -k test_README.py -xv

# Pytests to Compare and Verify Expected Outputs
from pathlib import Path
import os

# External Python libraries (installed via pip install)
import pytest
import matplotlib.testing.compare
import matplotlib.pyplot as plt

# Internal star_chart_spherical_projection reference to access functions, global variables, and error handling
import star_chart_spherical_projection as scsp

@pytest.fixture(scope="session")
def generate_plot_image(tmp_path_factory):
    plt_file_path = tmp_path_factory.mktemp("data") / "pytest.png"
    return plt_file_path

################### plot_centerline() ##########################################################

def test_readme_quickstart_plots(generate_plot_image):
    # quickstart_south_years.png
    scsp.plot_stereographic_projection(pole="South",
                display_labels=False,
                max_magnitude=3,
                year_since_2000=25,
                show_plot=False,
                save_plot_name=str(generate_plot_image))

    expected_png = (Path(__file__).parent.parent).joinpath('../examples',
                                                    "quickstart_south_years.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_quickstart_add_stars(generate_plot_image):
    # quickstart_newstar_example.png
    exalibur_star = scsp.add_new_star(star_name="Exalibur",
                                      ra="14.04.23",
                                      dec=64.22,
                                      pm_speed=12.3,
                                      pm_angle=83,
                                      magnitude=1.2)
    karaboudjan_star = scsp.add_new_star(star_name="Karaboudjan",
                                         ra="3.14.15",
                                         dec=10.13,
                                         pm_speed_ra=57.6,
                                         pm_speed_dec=60.1,
                                         magnitude=0.3)
    scsp.plot_stereographic_projection(pole="North",
                                       included_stars=["Vega", "Arcturus", "Altair"],
                                       userDefinedStars=[exalibur_star, karaboudjan_star],
                                       display_labels=True,
                                       fig_plot_color="red",
                                       year_since_2000=-39,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent.parent).joinpath('../examples',
                                                    "quickstart_newstar_example.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_quickstart_final_position():
    star_final_pos_dict = scsp.final_position(included_stars=["Vega"],
                        year_since_2000=11500)
    assert star_final_pos_dict == {'Vega': {'Declination': 83.6899118156341, 'RA': '05.13.54'}}
