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

def checkIAUForUpdates(save_csv=False):
	user_agents = [
		'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
		'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/6.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
	]
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
	

if __name__ == '__main__':
	checkIAUForUpdates(save_csv=False) # set to True if changes require updating existing script

