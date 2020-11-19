import sys
import pickle
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

edu_file = open("Education","rb")
edu_data = pickle.load(edu_file,encoding='utf-8')
edu_file.close()

year_data = edu_data["2013-14"]

literacy_data = dict()
literacy_data['District'] = []
literacy_data['literacy_rate'] = []
for district in year_data:
	literacy_data['District'].append(district.strip())
	literacy_data['literacy_rate'].append(year_data[district]['Overall Literacy'])

literacy_data = pd.DataFrame.from_dict(literacy_data)

map_df = gpd.read_file('Census_2011/2011_Dist.shp')
map_df = map_df[['DISTRICT', 'ST_NM', 'geometry']]

districts = list(map_df["DISTRICT"])
dist_in_map = []
states = list(map_df["ST_NM"])
for i in districts:
	dist_in_map.append(i.lower())

total = 0
in_map = 0
for dist in literacy_data['District']:
	total = total + 1
	if dist.lower() in dist_in_map:
		in_map = in_map + 1

for i in range(len(dist_in_map)):
	print(i,dist_in_map[i], states[i])