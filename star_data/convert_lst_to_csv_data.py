import pandas as pd

if __name__ == '__main__':
	aldebaran_star = ["Aldebaran", "04.35.55", 16.30, 199.3, 161.4, 0.99]
	algol_star = ["Algol", "03.08.10", 40.57, 3.4, 119.0, 2.11]
	alioth_star = ["Alioth", "12.54.01", 55.57, 112.2, 94.2, 1.76] # Big Dipper
	alkaid_star = ["Alkaid", "13.47.32", 49.18, 122.1, 263.0, 1.86] # Big Dipper
	alphecca_star = ["Alphecca", "15.34.41", 26.42, 147.8, 126.4, 2.22]
	alpheratz_star = ["Alpheratz", "00.08.23", 29.05, 213.6, 139.9, 2.06]
	altair_star = ["Altair", "19.50.46", 8.52, 660.3, 54.3, 0.93]
	arcturus_star = ["Arcturus", "14.15.39", 19.10, 2279.4, 208.7, 0.16]
	barnards_star = ["Barnard's Star", "17.57.47", 4.44, 10393.3, 355.6, 9.6]
	bellatrix_star = ["Bellatrix", "05.25.07", 6.20, 15.2, 212.2, 1.66]
	betelgeuse_star = ["Betelgeuse", "05.55.10", 7.24, 29.8, 67.7, 0.57]
	chara_star = ["Chara", "12.33.43", 41.21, 762.9, 292.5, 4.25]
	caph_star = ["Caph", "00.09.10", 59.08, 553.5, 109.0, 2.28] # Beta Cassiopeiae
	capella_star = ["Capella", "05.16.41", 45.59, 433.5, 170.0, 0.08]
	castor_star = ["Castor", "07.34.35", 31.53, 240.3, 232.8, 1.58]
	cor_caroli_star = ["Cor-Caroli", "12.56.01", 38.19, 240.2, 283.2, 2.89]
	deneb_star = ["Deneb", "20.41.25", 45.16, 2.7, 47.4, 1.33]
	denebola_star = ["Denebola", "11.49.03", 14.34, 510.7, 257.0, 2.13]
	dubhe_star = ["Dubhe", "11.03.43", 61.45, 138.5, 255.5, 1.82] # Big Dipper
	hamal_star = ["Hamal", "02.07.10", 23.27, 239.7, 128.1, 2.02]
	megrez_star = ["Megrez", "12.15.25", 57.01, 104.3, 85.5, 3.30] # Big Dipper
	merak_star = ["Merak", "11.01.50", 56.22, 88.0, 67.6, 2.35] # Big Dipper
	muphrid_star = ["Muphrid", "13.54.41", 18.23, 361.5, 189.7, 2.68]
	mizar_star = ["Mizar", "13.23.55", 54.55, 124.6, 100.5, 2.22] # Big Dipper
	navi_star = ["Navi", "00.56.42", 60.43, 25.5, 98.9, 2.18] # Gamma Cassiopeiae
	pleiades_celaeno_star = ["Celaeno", "03.44.48", 24.17, 49.2, 156.2, 5.45]
	polaris_star = ["Polaris", "02.31.49", 89.15, 46.0, 104.9, 2.0]
	pollux_star = ["Pollux", "07.45.18", 28.01, 628.2, 265.8, 1.22]
	phecda_star = ["Phecda", "11.53.49", 53.41, 108.2, 84.2, 2.39] # Big Dipper
	procyon_star = ["Procyon", "07.39.18", 5.13, 1259.2, 214.6, 0.40]
	rasalhague_star = ["Rasalhague", "17.34.56", 12.33, 246.5, 154.0, 2.09]
	regulus_star = ["Regulus", "10.08.22", 11.58, 248.8, 271.3, 1.41]
	ruchbah_star = ["Ruchbah", "01.25.49", 60.14, 300.5, 99.4, 2.68] # Delta Cassiopeiae
	schedar_star = ["Schedar", "00.40.30", 56.32, 58.4, 122.7, 2.25] # Alpha Cassiopeiae
	segin_star = ["Segin", "01.54.23", 63.4, 37.3, 120.5, 3.35] # Epsilon Cassiopeiae
	seginus_star = ["Seginus", "14.32.04", 38.18, 190.4, 322.6, 3.04]
	spica_star = ["Spica", "13.25.11", -11.09, 52.3, 234.1, 1.06]
	vega_star = ["Vega", "18.36.56", 38.47, 349.7, 35.1, 0.03]

	#Southern stars (- declination)
	achernar_star = ["Achernar", "01.37.42", -57.14, 95.0, 113.7, 0.54]
	acamar_star = ["Acamar", "02.58.15", -40.18, 57.1, 293.8, 3.22]
	acrux_star = ["Acrux", "12.26.35", -63.05, 38.8, 247.5, 1.28] # Southern Cross
	alphard_star = ["Alphard", "09.27.35", -8.39, 37.6, 336.1, 1.98]
	alnilam_star = ["Alnilam", "05.36.12", -1.12, 1.6, 118.4, 1.72]
	alnitak_star = ["Alnitak", "05.40.45", -1.56, 3.8, 57.5, 1.90]
	ankaa_star = ["Ankaa", "00.26.17", -42.18, 425.7, 146.8, 2.38]
	antares_star = ["Antares", "16.29.24", -26.25, 26.3, 207.5, 1.07]
	beta_hydri_star = ["Beta Hydri", "00.25.45", -77.15, 2242.9, 81.6, 2.79]
	beta_phoenicis_star = ["Beta Phoenicis", "01.06.05", -46.43, 88.1, 293.4, 3.37]
	canopus_star = ["Canopus", "06.23.57", -51.41, 30.6, 40.6, -0.63]
	delta_crucis_star = ["Delta Crucis", "12.15.08", -58.44, 38.6, 253.0, 2.74] # Southern Cross
	diphda_star = ["Diphda", "00.43.35", -17.59, 234.7, 82.2, 2.05]
	formalhaut_star = ["Formalhaut", "22.57.38", -29.37, 367.9, 116.6, 1.23]
	gacrux_star = ["Gacrux", "12.31.09", -57.06, 266.6, 173.9, 1.65] # Southern Cross
	gamma_phoenicis_star = ["Gamma Phoenicis", "01.28.21", -43.19, 207.6, 184.9, 3.44]
	hadar_star = ["Hadar", "14.03.49", -60.22, 40.5, 235.2, 0.64]
	meissa_star = ["Meissa", "05.35.08", -9.56, 3.0, 186.6, 3.53]
	mintaka_star = ["Mintaka", "05.32.00", -0.18, 0.9, 137.2, 2.23]
	mimosa_star = ["Mimosa", "12.47.43", -59.41, 45.9, 249.4, 1.31] # Southern Cross
	rigel_star = ["Rigel", "05.14.32", -8.12, 1.4, 69.1, 0.28]
	sadalmelik_star = ["Sadalmelik", "22.05.47", -0.19, 21.3, 119.3, 2.93]
	saiph_star = ["Saiph", "05.47.45", -9.4, 1.9, 131.2, 2.06]
	sirius_star = ["Sirius", "06.45.08", -16.42, 1339.4, 204.1, -1.44]
	zubeneschamali_star = ["Zubeneschamali", "15.17.00", -9.22, 100.0, 258.7, 2.61]

	# add stars to total star list
	northern_star_chart_list = [aldebaran_star,
								algol_star,
								alioth_star,
								alkaid_star,
								alphecca_star,
								alpheratz_star,
								altair_star,
								arcturus_star,
								#barnards_star,
								bellatrix_star,
								betelgeuse_star,
								chara_star,
								caph_star,
								capella_star,
								castor_star,
								cor_caroli_star,
								deneb_star,
								denebola_star,
								dubhe_star,
								hamal_star,
								megrez_star,
								merak_star,
								muphrid_star,
								mizar_star,
								navi_star,
								pleiades_celaeno_star,
								polaris_star,
								pollux_star,
								phecda_star,
								procyon_star,
								rasalhague_star,
								regulus_star,
								ruchbah_star,
								schedar_star,
								segin_star,
								seginus_star,
								spica_star,
								vega_star
								]

	southern_star_chart_list = [achernar_star,
								acamar_star,
								acrux_star,
								alphard_star,
								alnilam_star,
								alnitak_star,
								ankaa_star,
								antares_star,
								beta_hydri_star,
								beta_phoenicis_star,
								canopus_star,
								delta_crucis_star,
								diphda_star,
								formalhaut_star,
								gacrux_star,
								gamma_phoenicis_star,
								hadar_star,
								meissa_star,
								mintaka_star,
								mimosa_star,
								rigel_star,
								saiph_star,
								sirius_star,
								zubeneschamali_star
								]

	star_chart_list = northern_star_chart_list + southern_star_chart_list
	header_options = ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)", "Proper Motion Speed (mas/yr)", "Proper Motion Angle (DD.SS)", "Magnitude (V, Visual)"]
	my_df = pd.DataFrame(star_chart_list, columns=header_options)
	my_df = my_df.sort_values(by=["Star Name"])
	print(my_df)
	my_df.to_csv("star_data.csv", header=header_options, index=False)
