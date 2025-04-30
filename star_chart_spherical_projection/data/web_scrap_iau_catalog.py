import re
from bs4 import BeautifulSoup
import pandas as pd
from urllib import request, error
import numpy as np

import random

import logging

## Logging set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

user_agents = [
		'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
		'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/6.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

def IAU_CSN(save_csv=False):
	# get all valid named stars
	random_agent = random.choice(user_agents)
	iau_catalog_url = "https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt"
	req_with_headers = request.Request(url=iau_catalog_url, headers={'User-Agent': random_agent})

	catalog_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(catalog_html, 'html.parser')
	full_body_text = (full_body.text).split("\n")

	star_data = []
	for i, line in enumerate(full_body_text):
		iau_named_stars = {}
		if line != "" and line[0] != "#" and line[0] != "$":
			full_line = line.split("  ") # split on double space
			full_line = (list(filter(None, full_line))) # remove empty strings
			full_line = [x.replace("_", "") for x in full_line] # remove underscores
			full_line = [x.strip() for x in full_line] # strip leading/trailing whitespace
			if "Asellus Australis" in full_line[0] or "Polaris Australis" in full_line[0]: 
				# edge case where a long name is not splitting based on double space
				names = full_line[0].split(" ")
				first = names[0] + " " + names[1]
				second = names[2] + " " + names[3]
				third = names[4] + " " + names[5]
				split_elements = [first, second, third]
				full_line = split_elements + full_line[1:]
			iau_named_stars["Common Name"] = full_line[0]
			iau_named_stars["Designation"] = full_line[2]
			star_data.append(iau_named_stars)

	iau_stars = pd.DataFrame(star_data)
	if save_csv:
		iau_stars.to_csv("1_iau_stars.csv", index=False)
	return iau_stars
	

def inTheSkyAllPages():
	# return a link to all pages that contain objects
	random_agent = random.choice(user_agents)
	iau_catalog_url = "https://in-the-sky.org/search.php?s=&searchtype=Objects&obj1Type=17&const=1&objorder=1&distunit=0&magmin=&magmax=4&distmin=&distmax=&lyearmin=1957&lyearmax=2025&satorder=0&satgroup=0&satdest=0&satsite=0&satowner=0&feed=DFAN&ordernews=asc&maxdiff=7&startday=1&startmonth=3&startyear=2025&endday=30&endmonth=12&endyear=2035&news_view=normal&page=1"
	req_with_headers = request.Request(url=iau_catalog_url, headers={'User-Agent': random_agent})

	catalog_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(catalog_html, 'html.parser')
	table = full_body.find("div", "pager")
	links = table.find_all("a")
	page_links = [iau_catalog_url]
	for i in range(len(links)+1):
		base_url = "https://in-the-sky.org/search.php?s=&searchtype=Objects&obj1Type=17&const=1&objorder=1&distunit=0&magmin=&magmax=4&distmin=&distmax=&lyearmin=1957&lyearmax=2025&satorder=0&satgroup=0&satdest=0&satsite=0&satowner=0&feed=DFAN&ordernews=asc&maxdiff=7&startday=1&startmonth=3&startyear=2025&endday=30&endmonth=12&endyear=2035&news_view=normal&page="
		page_links.append(base_url + str(i+1))
	return page_links


def inTheSkyAllStars(page_links=None, iau_names=None, save_csv=False):
	random_agent = random.choice(user_agents)
	# iterate through all pages
	star_data = []
	for page_num, num_page in enumerate(page_links):
		#print(num_page)
		req_with_headers = request.Request(url=num_page, headers={'User-Agent': random_agent})
		catalog_html = request.urlopen(req_with_headers).read()
		full_body = BeautifulSoup(catalog_html, 'html.parser')
		table = full_body.find("div", "scrolltable_tbody")
		links = table.find_all("a")
		all_stars_links = re.findall(r'"([^"]*)"', str(links))
		for i, star_link in enumerate(all_stars_links):
			if "object" in star_link and "constellation" not in star_link:
				#print(star_link)
				star_property_dict = inTheSkyStarPage(star_link, iau_names, page_num+1, len(page_links))
				#print(star_property_dict)
				if star_property_dict is not None:
					star_data.append(star_property_dict)
		
	star_dataframe = pd.DataFrame(star_data)
	#print(len(star_dataframe.index))
	if save_csv:
		star_dataframe.to_csv("2_inthesky_star_data.csv", index=False)

def inTheSkyStarPage(page_link=None, iau_names=None, page_number=None, total_pages=None):
	# retrieve star data by iterating through all possible InTheSky pages
	random_agent = random.choice(user_agents)
	req_with_headers = request.Request(url=page_link, headers={'User-Agent': random_agent})
	star_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(star_html, 'html.parser')

	star_values = {}
	all_divs = full_body.find_all("div", "objinfo")
	all_names = []
	for div in all_divs:
		# get all alternative names
		span = div.find("span", "formlabel")
		if span.text == "Other names":
			# get all alternative names
			other_names = div.find("div")
			names = other_names.get_text("\n").split("\n")
			for name in names:
				if name[0] != " " and name[0] != "[":
					all_names.append(name)
				if name[0] == " ":
					all_names[-1] = all_names[-1] + name
	
	# if either the common name is found or the desgination is found in the list of possible
	common_name = list(set(iau_names["Common Name"]).intersection(all_names))
	designation = list(set(iau_names["Designation"]).intersection(all_names))
	
	# if star is a valid IAU star, with a value shared name
	data = []
	if len(common_name) == 1 or len(designation) == 1: 
		if len(common_name) == 1:
			common_name = common_name[0]
			print(f"(Page {page_number}/{total_pages}) Retrieving from in-the-sky = {common_name} ({designation[0]})")
		else:
			# get common name used by IAU, not used in website
			iau_name = iau_names.loc[iau_names["Designation"] == designation[0]]["Common Name"]
			common_name = iau_name.item()
			print(f"(Page {page_number}/{total_pages}) Retrieving from in-the-sky = {common_name} ({designation[0]})")
			
		star_values["Common Name"] = common_name
		star_values["Alternative Names"] = str(", ".join(all_names))

		# star position properties
		table_body = full_body.find("table", "objinfo stripy")
		rows = table_body.find_all("tr")

		for row in rows:
			name_value = row.find_all("td")
			value = re.sub(r"\[.*?\]","",name_value[1].text) # remove links in brackets
			value = value.replace("\\", "") # replace random string in declination
			value = value.replace("−", "-")
			value = value.strip()
			header = name_value[0].text.lower()
			if "right ascension" in header:
				ra_text = value.replace("h", ".") # remove hour marker
				ra_text = ra_text.replace("m", ".") # remove minute marker
				ra_text = ra_text.replace("s", "") # remove second marker
				star_values["Right Ascension"] = ra_text
			if "declination" in header:
				dec_text = value.replace("°", ".") # remove degree marker
				dec_text = dec_text.replace("'", "") # remove degree minute marker
				dec_text = dec_text.replace("\"", "") # remove degree second marker
				star_values["Declination"] = dec_text
			if "magnitude" in header:
				# if multiple magnitudes, gets Visual (V)
				all_mag = value.split(" ")
				star_values["Magnitude (Visual)"] = all_mag[all_mag.index("(V)") - 1]
			if "proper motion (speed)" in header:
				pm_sp = value.lower().split(" ")[0]
				units = value.lower().split(" ")[1]
				if "arcsec/yr" in units:
					# convert arcsec/yr to mas/yr
					pm_sp = str(float(pm_sp) * 1000)
				elif "mas/yr" in units:
					pass
				else:
					print(f"Invalid units: {units}")
					exit()
				star_values["Proper Motion (Speed, mas/yr)"] = pm_sp
			if "proper motion (pos ang)" in header:
				pm_angle = value.replace("°", "") # remove degree mark
				star_values["Proper Motion (Angle, Degrees)"] = pm_angle
		star_values["URL"] = page_link
		return star_values
	else:
		return None
		
def backupStars(backup_links_csv=None, save_csv=False):
	# add stars not found inTheSky to stars, from a list of backup links manually created
	backup_links_df = pd.read_csv(backup_links_csv)
	print("Collecting from backup links")

	star_data = []
	
	# iterate through backup links
	# collect data from Wikipedia links
	for index, row in backup_links_df.iterrows():
		if not pd.isnull(row["URL"]): # if URL is not empty
			if "wikipedia" in row["URL"]:
				print(f"({index+1}/{len(backup_links_df.index)}) Retrieving from Wikipedia = {row["Common Name"]} ({row["Designation"]})")
				# collect data from wikipedia
				wiki_star_data_dict = wikipediaLinks(row)
				star_data.append(wiki_star_data_dict)
		else:
			print(f"({index+1}/{len(backup_links_df.index)}) Unknown Star = {row["Common Name"]} ({row["Designation"]})")


	star_dataframe = pd.DataFrame(star_data)
	if save_csv:
		star_dataframe.to_csv("3_backup_star_data.csv", index=False)
	return star_dataframe

def wikipediaLinks(row_data=None):
	# process wikiepdia links
	random_agent = random.choice(user_agents)
	req_with_headers = request.Request(url=row_data["URL"], headers={'User-Agent': random_agent})
	star_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(star_html, 'html.parser')
		
	star_values = {}
	star_values["Common Name"] = row_data["Common Name"]
	star_values["URL"] = row_data["URL"]
	#print(row_data["URL"])
	
	# star position properties
	info_box = full_body.find("table", "infobox")
	rows = info_box.find_all("tr")
	for i, row in enumerate(rows):
		if "right ascension" in row.text.lower():
			ra_text = row.text.replace("\n", "")
			ra_text = ra_text.split("ascension")[1]
			ra_text = re.sub(r"\[.*?\]","",ra_text) # remove links in brackets
			if len(ra_text.split(" ")[0]) != 3:
				# add additional 0 at the start of the string if does not already include
				ra_text = "0" + ra_text
			ra_text = ra_text.replace(" ", "") # remove whitespace
			ra_text = ra_text.replace(".", "") # remove microseconds mark
			ra_text = ra_text.replace("h", ".") # remove hours marker
			ra_text = ra_text.replace("m", ".") # remove minute marker
			ra_text = ra_text.replace("s", "") # remove minute marker
			star_values["Right Ascension"] = ra_text
		if "declination" in row.text.lower():
			dec_text = row.text.replace("\n", "")
			dec_text = dec_text.lower().split("declination")[1]
			dec_text = re.sub(r"\[.*?\]","",dec_text) # remove links in brackets
			dec_text = dec_text.replace(u'\xa0', u' ')# remove non-breaking space in string
			if len(dec_text.split(" ")[0]) != 4:
				# add additional postive sign if does not already include
				dec_text = "+" + dec_text
			dec_text = dec_text.replace(" ", "") # remove whitespace
			dec_text = dec_text.replace(".", "") # remove microseconds mark
			dec_text = dec_text.replace("+", "") # remove postive mark
			dec_text = dec_text.replace("−", "-") # replace negative mark
			dec_text = dec_text.replace(u'\u2013', '-') # replace negative sign
			dec_text = dec_text.replace(u'\u2212', '-') # replace negative sign
			dec_text = dec_text.replace("°",".") # remove degree marks
			dec_text = dec_text.replace("′","") # remove degree minute marks
			dec_text = dec_text.replace("″","") # remove degree second marks
			star_values["Declination"] = dec_text
		if "apparent magnitude" in row.text.lower():
			mag_text = row.text.strip("\n")
			mag_text = mag_text.replace("\n", "$") # find split point
			mag_text = mag_text.split("$$")[1]
			mag_text = re.sub(r"\[.*?\]","",mag_text) # remove links in brackets
			# TODO: fix magntiude when a range of values is present
			star_values["Magnitude"] = mag_text
		if "proper motion" in row.text.lower():
			pm_text = row.text.lower()
			pm_text = pm_text.replace(u'\xa0', u' ')# remove non-breaking space in string
			pm_text = re.sub(r"\[.*?\]","",pm_text) # remove links in brackets
			pm_text = re.sub(r"\(.*?\)","",pm_text) # remove links in paraenthesis
			pm_ra_text = pm_text.split(":")[1].split("dec")[0].strip(" ")
			pm_dec_text = pm_text.split(":")[2].strip(" ")
			pm_ra_text = pm_ra_text.replace("+", "") # remove postive sign
			pm_dec_text = pm_dec_text.replace("+", "") # remove postive sign
			pm_ra_text = pm_ra_text.replace(u'\u2013', '-') # replace negative sign
			pm_ra_text = pm_ra_text.replace(u'\u2212', '-') # replace negative sign
			pm_dec_text = pm_dec_text.replace(u'\u2013', '-') # replace negative sign
			pm_dec_text = pm_dec_text.replace(u'\u2212', '-') # replace negative sign
			pm_ra_text = pm_ra_text.split(" ")[0]
			pm_dec_text = pm_dec_text.split(" ")[0]
			if "±" in pm_ra_text:
				pm_ra_text = pm_ra_text.split("±")[0]
			if "±" in pm_dec_text:
				pm_dec_text = pm_dec_text.split("±")[0]
			star_values["Proper Motion RA (mas/yr)"] = pm_ra_text.split(" ")[0]
			star_values["Proper Motion DEC (mas/yr)"] = pm_dec_text.split(" ")[0]
			ra_value = pm_ra_text.split(" ")[0]
			dec_value = pm_dec_text.split(" ")[0]
			# ignore plus/minus (use middle value)
			if "±" in ra_value:
				ra_value = ra_value.split("±")[0]
			if "±" in dec_value:
				dec_value = dec_value.split("±")[0]
			ra_value = float(ra_value)
			dec_value = float(dec_value)
			pm_speed = np.sqrt(ra_value**2 + dec_value**2)
			star_values["Proper Motion (Speed, mas/yr)"]= pm_speed
			pm_angle = np.rad2deg(np.arctan(ra_value/dec_value))
			if ra_value < 0 and dec_value > 0: # 90-180
				pm_angle += 90
			if ra_value < 0 and dec_value < 0: # 180-270
				pm_angle += 180
			if ra_value > 0 and dec_value < 0: # 270-360
				pm_angle += 270
			if pm_angle < 0:
				print(ra_value)
				print(dec_value)
				print(pm_angle)
				exit()
			star_values["Proper Motion (Angle, Degrees)"] = pm_angle		
		if "other designations" in row.text.lower():
			des_text = rows[i+1].text
			des_text = re.sub(r"\[.*?\]","",des_text) # remove links in brackets
			star_values["Alternative Names"] = des_text
	return star_values

def setupFinalCSV():
	# set up a single csv with all star data
	inthesky_df = pd.read_csv("2_inthesky_star_data.csv")
	backup_df = pd.read_csv("3_backup_star_data.csv")
	
	print(list(inthesky_df))
	print(list(backup_df))
	
	# Headers: Common Name, Right Ascension, Declination, PM Speed, PM Angle, Magnitude, Alternative Names, URL
	
	
def compareOutputs():
	# compare number of stars with offical names to number of stars found with full list of properties
	sky_stars = pd.read_csv("star_properties.csv")["Common Name"]
	iau_stars = pd.read_csv("iau_stars.csv")["Common Name"]
	diff_stars = list(set(iau_stars) - set(sky_stars))
	#print(len(diff_stars))
	print(f"IAU - Website = {len(iau_stars)} - {len(sky_stars)} = {len(iau_stars) - len(sky_stars)}")
	'''
	temp = []
	for star in diff_stars:
		print(star)
		new_star = {}
		new_star["Common Name"] = star
		des = IAU_CSN().loc[IAU_CSN()["Common Name"] == star]["Designation"].item()
		new_star["Designation"] = des
		new_star["URL"] = ""
		temp.append(new_star)
	_stars = pd.DataFrame(temp)
	_stars.to_csv("backup_links2.csv", index=False)
	'''
	#first = IAU_CSN().loc[IAU_CSN()["Common Name"] == diff_stars[0]]
	#print(first)
	
if __name__ == '__main__':
	#iau_dataframe = IAU_CSN(save_csv=True)                          # retrieve offical list of IAU names -> saved to iau_stars.csv
	#all_inthesky_pages = inTheSkyAllPages()                         # returns links to all pages in InTheSky
	#inTheSkyAllStars(page_links=all_inthesky_pages,
	#				iau_names=iau_dataframe,
	#				save_csv=True)                                   # iterate through InTheSky for IAU stars, saves stars to star_properties.csv
	backupStars(backup_links_csv="backup_links.csv",
				save_csv=True)              					     # iterate through backup list of stars
	# combine csv into a single star data
	setupFinalCSV()
	#compareOutputs()

