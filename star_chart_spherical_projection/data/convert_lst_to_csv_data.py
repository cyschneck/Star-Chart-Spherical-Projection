import pandas as pd

if __name__ == '__main__':
	# stars: ["name", "RA: HH.MM.SS", Declination DD.SS, Proper Motion Speed (mas/yr), Proper Motion Angle (DD.SS), Magnitude (V, Visual)]
	# Northern stars (+ declination)
	aldebaran_star = ["Aldebaran", "04.35.55", 16.30, 199.3, 161.4, 0.99]
	alderamin_star = ["Alderamin", "21.18.34", 62.35, 158.4, 71.9, 2.47]
	algieba_star = ["Algieba", "10.19.58", 19.50, 341.2, 116.9, 2.23]
	algol_star = ["Algol", "03.08.10", 40.57, 3.4, 119.0, 2.11]
	alhena_star = ["Alhena", "06.37.42", 16.24, 56.7, 165.9, 1.93]
	alioth_star = ["Alioth", "12.54.01", 55.57, 112.2, 94.2, 1.76] # Big Dipper
	alkaid_star = ["Alkaid", "13.47.32", 49.18, 122.1, 263.0, 1.86] # Big Dipper
	almach_star = ["Almach", "02.03.53", 42.19, 65.0, 139.4, 2.17]
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
	cebalrai_star = ["Cebalrai", "17.43.28", 4.34, 164.8, 345.3, 2.75]
	cor_caroli_star = ["Cor-Caroli", "12.56.01", 38.19, 240.2, 283.2, 2.89]
	deneb_star = ["Deneb", "20.41.25", 45.16, 2.7, 47.4, 1.33]
	denebola_star = ["Denebola", "11.49.03", 14.34, 510.7, 257.0, 2.13]
	dubhe_star = ["Dubhe", "11.03.43", 61.45, 138.5, 255.5, 1.82] # Big Dipper
	elnath_star = ["Elnath", "28.36.28", 28.36, 175.1, 172.5, 1.68]
	eltanin_star = ["Eltanin", "17.56.36", 51.29, 24.3, 200.4, 2.23]
	enif_star = ["Enif", "21.44.11", 9.52, 26.9, 89.1, 2.39]
	hamal_star = ["Hamal", "02.07.10", 23.27, 239.7, 128.1, 2.02]
	kochab_star = ["Kochab", "14.50.42", 74.09, 34.6, 289.3, 2.06]
	kornephoros_star = ["Kornephoros", "16.30.13", 21.29, 99.9, 261.4, 2.78]
	markab_star = ["Markab", "23.04.45", 15.12, 73.2, 124.4, 2.49]
	megrez_star = ["Megrez", "12.15.25", 57.01, 104.3, 85.5, 3.30] # Big Dipper
	menkar_star = ["Menkar", "03.02.16", 4.05, 77.6, 187.7, 2.54]
	menkalinan_star = ["Menkalinan", "05.59.31", 44.57, 56.4, 269.0, 1.90]
	merak_star = ["Merak", "11.01.50", 56.22, 88.0, 67.6, 2.35] # Big Dipper
	mirfak_star = ["Mirfak", "03.24.19", 49.51, 35.4, 137.8, 1.81]
	mirach_star = ["Mirach", "01.09.43", 35.37, 208.6, 122.5, 2.07]
	muphrid_star = ["Muphrid", "13.54.41", 18.23, 361.5, 189.7, 2.68]
	mizar_star = ["Mizar", "13.23.55", 54.55, 124.6, 100.5, 2.22] # Big Dipper
	navi_star = ["Navi", "00.56.42", 60.43, 25.5, 98.9, 2.18] # Gamma Cassiopeiae
	pleiades_celaeno_star = ["Celaeno", "03.44.48", 24.17, 49.2, 156.2, 5.45]
	polaris_star = ["Polaris", "02.31.49", 89.15, 46.0, 104.9, 2.0]
	pollux_star = ["Pollux", "07.45.18", 28.01, 628.2, 265.8, 1.22]
	phecda_star = ["Phecda", "11.53.49", 53.41, 108.2, 84.2, 2.39] # Big Dipper
	procyon_star = ["Procyon", "07.39.18", 5.13, 1259.2, 214.6, 0.40]
	rasalhague_star = ["Rasalhague", "17.34.56", 12.33, 246.5, 154.0, 2.09]
	rastaban_star = ["Rastaban", "17.30.25", 52.18, 18.7, 305.2, 2.80]
	regulus_star = ["Regulus", "10.08.22", 11.58, 248.8, 271.3, 1.41]
	ruchbah_star = ["Ruchbah", "01.25.49", 60.14, 300.5, 99.4, 2.68] # Delta Cassiopeiae
	sadr_star = ["Sadr", "20.22.13", 40.15, 2.6, 110.8, 2.20]
	scheat_star = ["Scheat", "23.03.46", 28.04, 232.3, 53.9, 2.48]
	schedar_star = ["Schedar", "00.40.30", 56.32, 58.4, 122.7, 2.25] # Alpha Cassiopeiae
	segin_star = ["Segin", "01.54.23", 63.4, 37.3, 120.5, 3.35] # Epsilon Cassiopeiae
	seginus_star = ["Seginus", "14.32.04", 38.18, 190.4, 322.6, 3.04]
	sheraton_star = ["Sheratan", "01.54.38", 20.48, 148.1, 138.2, 2.66]
	spica_star = ["Spica", "13.25.11", -11.09, 52.3, 234.1, 1.06]
	tarazed_star = ["Tarazed", "19.46.15", 10.36, 16.3, 94.8, 2.69]
	unukalhai_star = ["Unukalhai", "15.44.16", 6.25, 141.5, 71.2, 2.63]
	vega_star = ["Vega", "18.36.56", 38.47, 349.7, 35.1, 0.03]
	zosma_star = ["Zosma", "11.14.06", 20.31, 193.5, 132.2, 2.56]

	#Southern stars (- declination)
	# stars: ["name", "RA: HH.MM.SS", Declination, PM Speed, PM Angle, Magnitude (V, Visual)]
	achernar_star = ["Achernar", "01.37.42", -57.14, 95.0, 113.7, 0.54]
	acamar_star = ["Acamar", "02.58.15", -40.18, 57.1, 293.8, 3.22]
	acrab_star = ["Acrab", "16.05.26", -19.48, 24.6, 192.2, 2.62]
	acrux_star = ["Acrux", "12.26.35", -63.05, 38.8, 247.5, 1.28] # Southern Cross
	adhara_star = ["Adhara", "06.58.37", -28.58, 3.5, 67.7, 1.53]
	alphard_star = ["Alphard", "09.27.35", -8.39, 37.6, 336.1, 1.98]
	alnilam_star = ["Alnilam", "05.36.12", -1.12, 1.6, 118.4, 1.72]
	alnitak_star = ["Alnitak", "05.40.45", -1.56, 3.8, 57.5, 1.90]
	aludra_star = ["Aludra", "07.24.05", -29.18, 7.1, 324.5, 2.46]
	ankaa_star = ["Ankaa", "00.26.17", -42.18, 425.7, 146.8, 2.38]
	arneb_star = ["Arneb", "05.32.43", -17.49, 3.7, 66.2, 2.59]
	ascella_star = ["Ascella", "19.02.36", -29.52, 23.7, 27.1, 2.61]
	aspidiske_star = ["Aspidiske", "09.17.05", -59.16, 22.3, 302.4, 2.25]
	atria_star = ["Atria", "16.48.39", -69.01, 36.3, 150.3, 1.90]
	avior_star = ["Avior", "08.22.30", -59.30, 33.7, 310.8, 1.95]
	antares_star = ["Antares", "16.29.24", -26.25, 26.3, 207.5, 1.07]
	beta_hydri_star = ["Beta Hydri", "00.25.45", -77.15, 2242.9, 81.6, 2.79]
	beta_phoenicis_star = ["Beta Phoenicis", "01.06.05", -46.43, 88.1, 293.4, 3.37]
	canopus_star = ["Canopus", "06.23.57", -51.41, 30.6, 40.6, -0.63]
	cursa_star = ["Cursa", "05.07.51", -5.05, 112.0, 227.7, 2.79]
	delta_crucis_star = ["Delta Crucis", "12.15.08", -58.44, 38.6, 253.0, 2.74] # Southern Cross
	diphda_star = ["Diphda", "00.43.35", -17.59, 234.7, 82.2, 2.05]
	dschubba_star = ["Dschubba", "16.00.20", -22.37, 36.9, 196.1, 2.30]
	formalhaut_star = ["Formalhaut", "22.57.38", -29.37, 367.9, 116.6, 1.23]
	gacrux_star = ["Gacrux", "12.31.09", -57.06, 266.6, 173.9, 1.65] # Southern Cross
	gamma_phoenicis_star = ["Gamma Phoenicis", "01.28.21", -43.19, 207.6, 184.9, 3.44]
	gienah_star = ["Gienah", "12.15.48", -17.32, 160.1, 277.8, 2.59]
	hadar_star = ["Hadar", "14.03.49", -60.22, 40.5, 235.2, 0.64]
	lesath_star = ["Lesath", "17.20.45", -37.17, 30.2, 184.5, 2.64]
	meissa_star = ["Meissa", "05.35.08", -9.56, 3.0, 186.6, 3.53]
	menkent_star = ["Menkent", "14.06.40", -36.22, 734.4, 225.1, 2.05]
	miaplacidus_star = ["Miaplacidus", "09.13.12", -69.43, 190.7, 304.8, 1.67]
	mintaka_star = ["Mintaka", "05.32.00", -0.18, 0.9, 137.2, 2.23]
	mimosa_star = ["Mimosa", "12.47.43", -59.41, 45.9, 249.4, 1.31] # Southern Cross
	mirzam_star = ["Mirzam", "06.22.41", -17.57, 3.3, 256.4, 1.96]
	naos_star = ["Naos", "08.03.35", -40.0, 34.1, 299.3, 2.22]
	nunki_star = ["Nunki", "18.55.15", -26.17, 55.5, 164.2, 2.07]
	peacock_star = ["Peacock", "20.25.38", -56.44, 86.3, 175.4, 1.92]
	phact_star = ["Phact", "05.39.38", -34.04, 24.4, 176.0, 2.66]
	rigel_star = ["Rigel", "05.14.32", -8.12, 1.4, 69.1, 0.28]
	sabik_star = ["Sabik", "17.10.22", -15.43, 107.0, 22.0, 2.43]
	sadalmelik_star = ["Sadalmelik", "22.05.47", -0.19, 21.3, 119.3, 2.93]
	saiph_star = ["Saiph", "05.47.45", -9.4, 1.9, 131.2, 2.06]
	sargas_star = ["Sargas", "17.37.19", -42.59, 6.4, 119.4, 1.86]
	shaula_star = ["Shaula", "17.33.36", -37.06, 32.0, 195.5, 1.63]
	sirius_star = ["Sirius", "06.45.08", -16.42, 1339.4, 204.1, -1.44]
	suhail_star = ["Suhail", "09.07.59", -43.26, 27.6, 299.4, 2.20]
	wezen_star = ["Wezen", "07.08.23", -26.23, 4.5, 316.7, 1.84]
	zubeneschamali_star = ["Zubeneschamali", "15.17.00", -9.22, 100.0, 258.7, 2.61]

	# add stars to total star list
	northern_star_chart_list = [aldebaran_star,
								alderamin_star,
								algieba_star,
								algol_star,
								alhena_star,
								alioth_star,
								alkaid_star,
								almach_star,
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
								cebalrai_star,
								cor_caroli_star,
								deneb_star,
								denebola_star,
								dubhe_star,
								elnath_star,
								eltanin_star,
								enif_star,
								hamal_star,
								kochab_star,
								kornephoros_star,
								markab_star,
								megrez_star,
								menkar_star,
								menkalinan_star,
								merak_star,
								mirfak_star,
								mirach_star,
								muphrid_star,
								mizar_star,
								navi_star,
								pleiades_celaeno_star,
								polaris_star,
								pollux_star,
								phecda_star,
								procyon_star,
								rasalhague_star,
								rastaban_star,
								regulus_star,
								ruchbah_star,
								sadr_star,
								scheat_star,
								schedar_star,
								segin_star,
								seginus_star,
								sheraton_star,
								spica_star,
								tarazed_star,
								unukalhai_star,
								vega_star,
								zosma_star
								]

	southern_star_chart_list = [achernar_star,
								acamar_star,
								acrab_star,
								acrux_star,
								adhara_star,
								alphard_star,
								alnilam_star,
								alnitak_star,
								aludra_star,
								ankaa_star,
								arneb_star,
								ascella_star,
								aspidiske_star,
								atria_star,
								avior_star,
								antares_star,
								beta_hydri_star,
								beta_phoenicis_star,
								canopus_star,
								cursa_star,
								delta_crucis_star,
								diphda_star,
								dschubba_star,
								formalhaut_star,
								gacrux_star,
								gamma_phoenicis_star,
								gienah_star,
								hadar_star,
								lesath_star,
								meissa_star,
								menkent_star,
								miaplacidus_star,
								mintaka_star,
								mimosa_star,
								mirzam_star,
								naos_star,
								nunki_star,
								peacock_star,
								phact_star,
								rigel_star,
								sabik_star,
								saiph_star,
								sargas_star,
								shaula_star,
								sirius_star,
								suhail_star,
								wezen_star,
								zubeneschamali_star
								]

	star_chart_list = northern_star_chart_list + southern_star_chart_list
	print("Total stars = {0}".format(len(star_chart_list)))
	for star in star_chart_list:
		if len(star) != 6:
			print("ERROR: MISSING A VALUE = {0}".format(star[0])) # ensure that all stars have features
			exit()
	header_options = ["Star Name", "Right Ascension (HH.MM.SS)", "Declination (DD.SS)", "Proper Motion Speed (mas/yr)", "Proper Motion Angle (DD.SS)", "Magnitude (V, Visual)"]
	df = pd.DataFrame(star_chart_list, columns=header_options)
	df = df.sort_values(by=["Star Name"])
	print(df)
	df.to_csv("star_data.csv", header=header_options, index=False)
