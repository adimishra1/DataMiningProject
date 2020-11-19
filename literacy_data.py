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
map_df = map_df[['DISTRICT', 'geometry']]


districts = list(map_df["DISTRICT"])

global_dict_file = open("global_map.pkl","rb")
global_map = pickle.load(global_dict_file,encoding='utf-8')
global_dict_file.close()

def get_district_code(dist_name):
	for dist in global_map:
		if "_" in dist:
			if dist_name == dist.split("_")[0]:
				return global_map[dist]
		else:
			if dist_name == dist:
				return global_map[dist]
	return -1

literacy_dict = dict()
literacy_dict['District'] = districts
literacy_dict['Literacy'] = [0]*len(districts)
count = 0
for i in range(len(literacy_data['District'])):
	code = get_district_code(literacy_data['District'][i].lower())
	if code == -1:
		count = count + 1
		print(literacy_data['District'][i])
	else:
		if code < len(districts):
			literacy_dict['Literacy'][code] = literacy_data['literacy_rate'][i]

if count > 0:
	print(count,"not found in global map")
dataframe = pd.DataFrame.from_dict(literacy_dict)
dataframe.to_excel("output.xlsx")

df = pd.read_excel('output.xlsx')
merged = map_df.set_index('DISTRICT').join(df.set_index('District'))
merged = merged[['Literacy', 'geometry']]

fig, ax = plt.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('District Wise Literacy Rate in 2013-14', fontdict={'fontsize': '25', 'fontweight' : '3'})
merged.plot(column='Literacy', cmap='Oranges', linewidth=0.8, ax=ax, edgecolor='0.8', legend=False, categorical=False)
fig.savefig("District_wise_literacy.png", dpi=100)