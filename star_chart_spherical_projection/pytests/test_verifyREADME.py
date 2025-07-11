# Pytest for README.md page
# star_chart_spherical_projection/: python -m pytest
# python -m pytest -k test_verifyREADME.py -xv

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

################### Test Plots on README ##########################################################

def test_readme_quickstart_plots(generate_plot_image):
    # quickstart_south_years.png
    scsp.plot_stereographic_projection(pole="South",
                display_labels=False,
                max_magnitude=3,
                year_since_2000=25,
                show_plot=False,
                save_plot_name=str(generate_plot_image))

    expected_png = (Path(__file__).parent).joinpath('examples',
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
                                       added_stars=[exalibur_star, karaboudjan_star],
                                       display_labels=True,
                                       fig_plot_color="red",
                                       year_since_2000=-39,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "quickstart_newstar_example.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

@pytest.mark.skip(reason="Current Version invalid declination, fix with updated version")
def test_readme_quickstart_final_position():
    star_final_pos_dict = scsp.final_position(included_stars=["Vega"],
                        year_since_2000=11500)
    assert star_final_pos_dict == {'Vega': {'Declination': 83.6899118156341, 'RA': '05.13.54'}}

def test_readme_north_pole(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "pole_north.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_south_pole(generate_plot_image):
    scsp.plot_stereographic_projection(pole="South",
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "pole_south.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_included_stars_none(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       included_stars=[],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "includedStars_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_included_stars_subsets(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       included_stars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "includedStars_subset.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_declination_min_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       declination_min=-30,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "declination_min_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_declination_min_10(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       declination_min=10,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "declination_min_10.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_years_since_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       year_since_2000=0,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "yearSince2000_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_years_since_3100(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       year_since_2000=-3100,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "yearSince2000_negative_3100.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_display_labels_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=True,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "displayLabels_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_display_labels_false(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "displayLabels_false.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_display_dec_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       display_dec=True,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "displayDeclinationNumbers_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_display_dec_false(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       display_dec=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "displayDeclinationNumbers_false.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None


def test_readme_increment_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       increment=10,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "increment_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_increment_5(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       display_labels=False,
                                       increment=5,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "increment_5.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_is_precession_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       is_precession=True,
                                       year_since_2000=11500,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "isPrecession_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_is_precession_false(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       is_precession=False,
                                       year_since_2000=11500,
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "isPrecession_false.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_max_magnitude_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       max_magnitude=None,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "maxMagnitudeFilter_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_max_magnitude_1(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       max_magnitude=1,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "maxMagnitudeFilter_1.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_added_stars_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       included_stars=["Vega"],
                                       added_stars=[],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "added_stars_none.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_added_stars_additional_stars(generate_plot_image):
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
                                       included_stars=["Vega"],
                                       added_stars=[exalibur_star, karaboudjan_star],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "added_stars_included.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_only_display_user_stars_false(generate_plot_image):
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
                                       only_added_stars=False,
                                       added_stars=[exalibur_star, karaboudjan_star],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "only_added_stars_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_only_display_user_stars_true(generate_plot_image):
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
                                       only_added_stars=True,
                                       added_stars=[exalibur_star, karaboudjan_star],
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "only_added_stars_true.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_fig_plot_title_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       fig_plot_title=None,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "fig_plot_title_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_fig_plot_title_example(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       fig_plot_title="This is a Example Title for a Star Chart",
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "fig_plot_title_example.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_fig_plot_color_default(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       fig_plot_color="C0",
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "fig_plot_color_default.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_fig_plot_color_darkorchid(generate_plot_image):
    scsp.plot_stereographic_projection(pole="North",
                                       fig_plot_color="darkorchid",
                                       display_labels=False,
                                       save_plot_name=str(generate_plot_image),
                                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "fig_plot_color_darkorchid.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_vega_declination_with_precession(generate_plot_image):
    # plot_star_vega_declination_with_precession.png
    scsp.plot_position(star="Vega",
                       added_star=None,
                       start_year_since_2000=-15000,
                       end_year_since_2000=15000,
                       is_precession=True,
                       increment=5,
                       dec_ra="D",
                       save_plot_name=str(generate_plot_image),
                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "plot_star_vega_declination_with_precession.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_vega_declination_without_precession(generate_plot_image):
    scsp.plot_position(star="Vega",
                       added_star=None,
                       start_year_since_2000=-15000,
                       end_year_since_2000=15000,
                       increment=5,
                       is_precession=False,
                       dec_ra="D",
                       save_plot_name=str(generate_plot_image),
                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "plot_star_vega_declination_without_precession.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_vega_right_ascension_with_precession(generate_plot_image):
    scsp.plot_position(star="Vega",
                       added_star=None,
                       start_year_since_2000=-15000,
                       end_year_since_2000=15000,
                       is_precession=True,
                       increment=5,
                       dec_ra="R",
                       save_plot_name=str(generate_plot_image),
                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "plot_star_vega_right_ascension_with_precession.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_vega_right_ascension_without_precession(generate_plot_image):
    scsp.plot_position(star="Vega",
                       added_star=None,
                       start_year_since_2000=-15000,
                       end_year_since_2000=15000,
                       is_precession=False,
                       increment=5,
                       dec_ra="R",
                       save_plot_name=str(generate_plot_image),
                       show_plot=False)

    expected_png = (Path(__file__).parent).joinpath('examples',
                                                    "plot_star_vega_right_ascension_without_precession.png")
    plt.close()
    assert os.path.exists(expected_png)
    assert matplotlib.testing.compare.compare_images(
        expected_png, str(generate_plot_image), tol=0.001,
        in_decorator=False) is None

def test_readme_future_star_no_max_magnitude():
    future_north_star = scsp.predict_pole_star(year_since_2000=20000, pole="North", max_magnitude=None)
    assert future_north_star == "Thuban"

def test_readme_future_star_one_max_magnitude():
    future_north_star = scsp.predict_pole_star(year_since_2000=20000, pole="North", max_magnitude=1)
    assert future_north_star == "Vega"

def test_readme_final_position():
    fin_pos = scsp.final_position(included_stars=["Thuban", "Vega"], year_since_2000=20000)
    assert str(fin_pos) == "{'Thuban': {'Declination': np.float64(87.7600158821428), 'RA': '02.43.17'}, 'Vega': {'Declination': np.float64(45.59902976977015), 'RA': '15.24.09'}}"

def test_readme_position_over_time():
    fin_pos = scsp.position_over_time(star="Altair",
                                    start_year_since_2000=0,
                                    end_year_since_2000=20000,
                                    increment=10000,
                                    is_precession=True)
    assert str(fin_pos) == "{2000: {'RA (radians)': -1.0874854843260338, 'RA (hours)': '19.50.46', 'Dec (degrees)': np.float64(8.520199531975353)}, 12000: {'RA (radians)': 1.4428565057434115, 'RA (hours)': '05.30.41', 'Dec (degrees)': np.float64(52.1248474708539)}, 22000: {'RA (radians)': -2.197776589553731, 'RA (hours)': '15.36.18', 'Dec (degrees)': np.float64(13.075954490463758)}}"
