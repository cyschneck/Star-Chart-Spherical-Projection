import pandas as pd

csv_data_url = "https://raw.githubusercontent.com/cyschneck/iau-star-names/refs/heads/main/stars_with_data.csv"

# Update README.md and run generate_examples_star_chart.py.py to update example plots

if __name__ == '__main__':
    # Download a copy of star data for all named stars (via iau-star-names)
    print("Retrieving Star Data CSV. from iau-star-names..")
    iau_star_dataframe = pd.read_csv(csv_data_url, encoding="utf-8")
    iau_star_dataframe.to_csv("stars_with_data.csv", index=False)
    print(f"README Stars: \n{list(iau_star_dataframe["Common Name"])}")
