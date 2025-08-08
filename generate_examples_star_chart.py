# Generate chart examples plots
# python test_generate_star_chart.py

import star_chart_spherical_projection

if __name__ == '__main__':
    startYear = -15000
    endYear = 15000
    increment = 5
    year_since_example = 25  # 2025
    show_plt = False

    # compare stars_with_data.csv with a generated list for year 0 (to check RA and declination values)
    all_common_names = [
        name[0] for name in star_chart_spherical_projection._get_stars()
    ]
    star_chart_spherical_projection.final_position(
        included_stars=all_common_names,
        year_since_2000=0,
        is_precession=True,
        save_to_csv=
        "star_chart_spherical_projection/pytests/examples/year_0_stars_pos.csv"
    )
    # star plots
    star_chart_spherical_projection.position_over_time(
        star="Vega",
        added_star=None,
        start_year_since_2000=startYear,
        end_year_since_2000=endYear,
        is_precession=True,
        increment=increment,
        save_to_csv=None)
    star_chart_spherical_projection.plot_position(
        star="Vega",
        added_star=None,
        start_year_since_2000=startYear,
        end_year_since_2000=endYear,
        is_precession=True,
        increment=increment,
        dec_ra="D",
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/plot_star_vega_declination_with_precession.png"
    )
    star_chart_spherical_projection.plot_position(
        star="Vega",
        added_star=None,
        start_year_since_2000=startYear,
        end_year_since_2000=endYear,
        is_precession=True,
        increment=increment,
        dec_ra="R",
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/plot_star_vega_right_ascension_with_precession.png"
    )
    star_chart_spherical_projection.plot_position(
        star="Vega",
        added_star=None,
        start_year_since_2000=startYear,
        end_year_since_2000=endYear,
        is_precession=False,
        increment=increment,
        dec_ra="D",
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/plot_star_vega_declination_without_precession.png"
    )
    star_chart_spherical_projection.plot_position(
        star="Vega",
        added_star=None,
        start_year_since_2000=startYear,
        end_year_since_2000=endYear,
        is_precession=False,
        increment=increment,
        dec_ra="R",
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/plot_star_vega_right_ascension_without_precession.png"
    )
    # note, includes endYear (0 to 9, every three = [0, 3, 6, 9], inclusive of start, inclusive of end

    # Quickstart Graphs
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="South",
        display_labels=False,
        year_since_2000=year_since_example,
        max_magnitude=3,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/quickstart_south_years.png"
    )
    exalibur_star = star_chart_spherical_projection.add_new_star(
        star_name="Exalibur",
        ra="14.04.23",
        dec=64.22,
        pm_speed=12.3,
        pm_angle=83,
        magnitude=1.2)
    karaboudjan_star = star_chart_spherical_projection.add_new_star(
        star_name="Karaboudjan",
        ra="3.14.15",
        dec=10.13,
        pm_speed_ra=57.6,
        pm_speed_dec=60.1,
        magnitude=0.3)
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=["Vega", "Arcturus", "Altair"],
        added_stars=[exalibur_star, karaboudjan_star],
        display_labels=True,
        fig_plot_color="red",
        year_since_2000=-39,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/quickstart_newstar_example.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=[
            "Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alkaid"
        ],
        display_labels=False,
        year_since_2000=-39,
        declination_min=40,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/quickstart_bigDipper.png"
    )

    ## Graphs for each plot Arguments
    # pole
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/pole_north.png")
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="South",
        display_labels=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/pole_south.png")
    # included_stars
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=[],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/includedStars_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=["Vega", "Arcturus", "Enif", "Caph", "Mimosa"],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/includedStars_subset.png"
    )
    # declination_min
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        declination_min=-30,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/declination_min_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        declination_min=10,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/declination_min_10.png"
    )
    # year_since_2000
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        year_since_2000=0,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/yearSince2000_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        year_since_2000=-3100,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/yearSince2000_negative_3100.png"
    )
    # display_labels
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=True,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/displayLabels_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/displayLabels_false.png"
    )
    # display_dec
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        display_dec=True,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/displayDeclinationNumbers_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        display_dec=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/displayDeclinationNumbers_false.png"
    )
    # increment
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        increment=10,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/increment_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        display_labels=False,
        increment=5,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/increment_5.png")
    # is_precession
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        is_precession=True,
        year_since_2000=11500,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/isPrecession_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        is_precession=False,
        year_since_2000=11500,
        show_plot=show_plt,
        display_labels=False,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/isPrecession_false.png"
    )
    # max_magnitude
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        max_magnitude=None,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/maxMagnitudeFilter_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        max_magnitude=1,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/maxMagnitudeFilter_1.png"
    )
    # added_stars
    exalibur_star = star_chart_spherical_projection.add_new_star(
        star_name="Exalibur",
        ra="14.04.23",
        dec=64.22,
        pm_speed=12.3,
        pm_angle=83,
        magnitude=1.2)
    karaboudjan_star = star_chart_spherical_projection.add_new_star(
        star_name="Karaboudjan",
        ra="3.14.15",
        dec=10.13,
        pm_speed_ra=57.6,
        pm_speed_dec=60.1,
        magnitude=0.3)
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=["Vega"],
        added_stars=[],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/added_stars_none.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        included_stars=["Vega"],
        added_stars=[exalibur_star, karaboudjan_star],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/added_stars_included.png"
    )
    # only_added_stars
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        only_added_stars=False,
        added_stars=[exalibur_star, karaboudjan_star],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/only_added_stars_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        only_added_stars=True,
        added_stars=[exalibur_star, karaboudjan_star],
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/only_added_stars_true.png"
    )
    # fig_plot_title
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        fig_plot_title=None,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/fig_plot_title_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        fig_plot_title="This is a Example Title for a Star Chart",
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/fig_plot_title_example.png"
    )
    # fig_plot_color
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        fig_plot_color="C0",
        display_labels=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/fig_plot_color_default.png"
    )
    star_chart_spherical_projection.plot_stereographic_projection(
        pole="North",
        fig_plot_color="darkorchid",
        display_labels=False,
        show_plot=show_plt,
        save_plot_name=
        "star_chart_spherical_projection/pytests/examples/fig_plot_color_darkorchid.png"
    )
