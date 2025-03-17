import re
from bs4 import BeautifulSoup
import pandas as pd
from urllib import request, error

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


def IAU_CSN():
	# get all valid named stars
	random_agent = random.choice(user_agents)
	iau_catalog_url = "https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt"
	req_with_headers = request.Request(url=iau_catalog_url, headers={'User-Agent': random_agent})

	catalog_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(catalog_html, 'html.parser')
	full_body_text = (full_body.text).split("\n")

	star_data = []
	for line in full_body_text:
		iau_named_stars = {}
		if line != "" and line[0] != "#" and line[0] != "$":
			common_name = line.split()[0]
			hr_designation = line.split()[2]
			if hr_designation == "HR":
				hr_designation += " " + line.split()[3]
			iau_named_stars["Common Name"] = common_name
			iau_named_stars["HR"] = hr_designation
			star_data.append(iau_named_stars)
	iau_stars = pd.DataFrame(star_data)
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
	print(len(star_dataframe.index))
	if save_csv:
		star_dataframe.to_csv("star_properties.csv", index=False)
	return star_dataframe

def inTheSkyStarPage(page_link=None, iau_names=None, page_number=None, total_pages=None):
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
	
	common_name = list(set(iau_names).intersection(all_names))
	#hip_designation = 
	# if star is a valid IAU star, with a value shared name
	data = []
	if len(common_name) == 1:
		common_name = common_name[0]
		print(f"Retrieving Star Data (Page {page_number}/{total_pages}) = {common_name}")
		star_values["Common Name"] = common_name
		star_values["Alternative Names"] = all_names

		# star position properties
		table_body = full_body.find("table", "objinfo stripy")
		rows = table_body.find_all("tr")

		for row in rows:
			name_value = row.find_all("td")
			value = re.sub(r"\[.*?\]","",name_value[1].text) # remove links in brackets
			value = value.replace("\\", "") # replace random string in declination
			value = value.replace("−", "-")
			value = value.strip()
			if "Right ascension" in name_value[0].text:
				star_values["Right Ascension"] = value
			if "Declination" in name_value[0].text:
				star_values["Declination"] = value
			if "Magnitude" in name_value[0].text:
				# if multiple magnitudes, gets Visual (V)
				all_mag = value.split(" ")
				star_values["Magnitude"] = all_mag[all_mag.index("(V)") - 1]
			if "Proper Motion (speed)" in name_value[0].text:
				star_values["Proper Motion (Speed)"] = value
			if "Proper Motion (pos ang)" in name_value[0].text:
				star_values["Proper Motion (Angle)"] = value
		return star_values
	else:
		return None
	
def compareOutputs():
	found_stars = pd.read_csv("star_properties.csv")
	sky_stars = found_stars["Common Name"]
	print(len(IAU_CSN()))
	print(len(sky_stars))
	print(list(set(IAU_CSN()) - set(sky_stars)))
	
if __name__ == '__main__':
	all_iau_named_stars = IAU_CSN()
	print(all_iau_named_stars)
	#print(len(all_iau_named_stars))
	#all_pages = inTheSkyAllPages()
	#inTheSkyAllStars(all_pages, all_iau_named_stars, True)
	#compareOutputs()

