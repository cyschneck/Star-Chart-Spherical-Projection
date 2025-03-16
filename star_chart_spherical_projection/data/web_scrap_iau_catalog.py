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

def checkIAU_CSN(save_csv=False):
	# return text data from IAU-CSN list
	random_agent = random.choice(user_agents)
	iau_catalog_url = "https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt"
	req_with_headers = request.Request(url=iau_catalog_url, headers={'User-Agent': random_agent})

	catalog_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(catalog_html, 'html.parser')
	full_body_text = (full_body.text).split("\n")

	iau_named_stars = []
	full_named_star_row = []
	for line in full_body_text:
		if line != "" and line[0] != "#" and line[0] != "$":
			iau_named_stars.append(line.split()[0])
			if save_csv:
				full_named_star_row.append(line.split())

	current_stars = []
	with open("star_data.csv") as current_star_data:
		for i, row in enumerate(current_star_data):
			if i != 0:
				current_stars.append(row.split(",")[0])

	compare_current_iau_stars = sorted(list(set(iau_named_stars) - set(current_stars)))
	if len(compare_current_iau_stars) != 0:
		print(f"current stars do not match IAU-CSN stars, current list does not include {len(compare_current_iau_stars)} stars:")
		print(compare_current_iau_stars)

	if save_csv:  ## TODO
		saveUpdatesAsCSV(all_named_stars_row=iau_named_stars)

def saveUpdatesAsCSV(all_named_stars_row=None):
	headers = ['Name/ASCII',
			'Name/Diacritics',
			'Designation',
			'ID',
			'ID',
			'Con',
			'#',
			'WDS_J',
			'mag', 
			'bnd',
			'HIP',
			'HD',
			'RA(J2000)',
			'Dec(J2000)',
			'Date',
			'Notes']

	df = pd.DataFrame(all_named_stars_row, columns=headers)
	df = df.sort_values(by=["Name/ASCII"])
	df.to_csv('iau_csn_named_stars_catalog.csv', header=headers, index=False)

def inTheSkyAllPages():
	# return a link to all pages that contain objects
	random_agent = random.choice(user_agents)
	iau_catalog_url = "https://in-the-sky.org/search.php?s=&searchtype=Objects&obj1Type=17&const=1&objorder=1&distunit=0&magmin=&magmax=4&distmin=&distmax=&lyearmin=1957&lyearmax=2025&satorder=0&satgroup=0&satdest=0&satsite=0&satowner=0&feed=DFAN&ordernews=asc&maxdiff=7&startday=1&startmonth=3&startyear=2025&endday=30&endmonth=12&endyear=2035&news_view=normal"
	req_with_headers = request.Request(url=iau_catalog_url, headers={'User-Agent': random_agent})

	catalog_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(catalog_html, 'html.parser')
	table = full_body.find("div", "pager")
	links = table.find_all("a")
	page_links = [iau_catalog_url]
	for link in links:
		page_links.append(re.findall(r'"([^"]*)"', str(link))[0])
	return page_links


def inTheSkyAllStars(page_links=None, save_csv=False):
	random_agent = random.choice(user_agents)
	# iterate through all pages
	for num_page in page_links:
		print(num_page)
		req_with_headers = request.Request(url=num_page, headers={'User-Agent': random_agent})
		catalog_html = request.urlopen(req_with_headers).read()
		full_body = BeautifulSoup(catalog_html, 'html.parser')
		table = full_body.find("div", "scrolltable_tbody")
		links = table.find_all("a")
		all_stars_links = re.findall(r'"([^"]*)"', str(links))
		for star_link in all_stars_links:
			if "object" in star_link and "constellation" not in star_link:
				print(star_link)
				inTheSkyStarPage(star_link)
			break
		break

def inTheSkyStarPage(page_link=None):
	random_agent = random.choice(user_agents)
	req_with_headers = request.Request(url=page_link, headers={'User-Agent': random_agent})
	star_html = request.urlopen(req_with_headers).read()
	full_body = BeautifulSoup(star_html, 'html.parser')
	#print(full_body.find("p", "widetitle").text)
	all_divs = full_body.find_all("div", "objinfo")
	for div in all_divs:
		span = div.find("span", "formlabel")
		if span.text == "Other names":
			other_names = div.find("div")
			names = other_names.get_text("\n").split("\n")
			all_names = []
			for name in names:
				if name[0] != " " and name[0] != "[":
					all_names.append(name)
				if name[0] == " ":
					all_names[-1] = all_names[-1] + name
			print(all_names)
	
if __name__ == '__main__':
	#checkIAU_CSN(save_csv=False) # set to True if changes require updating existing script
	all_pages = inTheSkyAllPages()
	inTheSkyAllStars(page_links=all_pages, save_csv=False)

