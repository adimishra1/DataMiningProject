import sys
import pickle
import shapely
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from cleanerData import *
import math
from getDistrictCode import *
import warnings
from matplotlib.colors import LinearSegmentedColormap

warnings.filterwarnings("ignore")

map_data = gpd.read_file('Census_2011/2011_Dist.shp')
temp = map_data["geometry"]
district_coords = temp.to_crs("crs").centroid
max_district_code = len(temp)
year = 2007

def get_coordinates(dist_code): #returns [longitude, latitude] for the corresponding district
	return [district_coords[dist_code].xy[0][0], district_coords[dist_code].xy[1][0]]

def get_distance(dist1_code, dist2_code):
	d1_cs = get_coordinates(dist1_code)
	d2_cs = get_coordinates(dist2_code)
	return math.sqrt((d1_cs[0] - d2_cs[0])**2 + (d1_cs[1] - d2_cs[1])**2)

def are_neighbours(dist1_code, dist2_code):
	distance = get_distance(dist1_code, dist2_code)
	threshold = 2
	return (distance < threshold)

def same_literacy_class(rate1, rate2):
	if rate1 < 50 and rate2 < 50:
		return True
	elif (rate1 > 50 and rate1 < 65) and (rate2 > 50 and rate2 < 65):
		return True
	elif (rate1 > 65 and rate1 < 80) and (rate2 > 65 and rate2 < 80):
		return True
	elif rate1 > 80 and rate2 > 80:
		return True
	else:
		return False

def get_cluster_name(rate):
	if rate < 50:
		return "Very Low"
	elif rate < 65:
		return "Mid Low"
	elif rate < 80:
		return "Mid High"
	else:
		return "Very High"

literacy_data = dict()
districts = []
for dist_code in range(max_district_code):
	if dist_code in small_edu_data[year]:
		literacy_data[dist_code] = small_edu_data[year][dist_code]["LiteracyRate"]
		districts.append(dist_code)

clusters = [
[173], #Kerela
[474], #Ranchi
[139], #Dehradun
[239], #Jaipur
[381], #Mumbai
[233], #Imphal
[45] #Banglore 
]

NUM_CLUSTERS = 7

for cluster in clusters:
	for dist_code in cluster:
		districts.remove(dist_code)

added_new = True
while len(districts) > 0 and added_new:
	added_new = False
	to_remove = []
	to_append = []
	for i in range(NUM_CLUSTERS):
		to_append.append([])
	for dist_code in districts:
		dist_added = 0
		for i in range(len(clusters)):
			for dist in clusters[i]:
				if are_neighbours(dist, dist_code) and same_literacy_class(literacy_data[dist], literacy_data[dist_code]):
					# clusters[i].append(dist_code)
					to_append[i].append(dist_code)
					dist_added = 1
					to_remove.append(dist_code)
					added_new = True
					break
			if dist_added == 1:
				break
	for i in range(len((to_append))):
		for dist in to_append[i]:
			clusters[i].append(dist)
	for i in to_remove:
		districts.remove(i)

for cluster in clusters:
	avg_literacy = 0
	for dist in cluster:
		avg_literacy = avg_literacy + literacy_data[dist]
	avg_literacy = avg_literacy/len(cluster)
	print(len(cluster), get_cluster_name(literacy_data[cluster[0]]), avg_literacy)

map_df = gpd.read_file('Census_2011/2011_Dist.shp')
cluster_dict = dict()
cluster_dict['District'] = list(map_df["DISTRICT"])
cluster_dict['Cluster_Num'] = [0]*len(list(map_df["DISTRICT"]))
cluster_dict['color'] = [0]*len(list(map_df["DISTRICT"]))
for i in range(len(cluster_dict['District'])):
	code = getDistrictCode(cluster_dict['District'][i])
	if code == -1:
		print(cluster_dict['District'][i])
	else:
		#find the cluster_number:
		for cluster_num in range(len(clusters)):
			if code in clusters[cluster_num]:
				cluster_dict['Cluster_Num'][code] = (cluster_num + 1)
				cluster_dict['color'][code] = (cluster_num + 1)/NUM_CLUSTERS
				break

dataframe = pd.DataFrame.from_dict(cluster_dict)
# print(dataframe)
dataframe.to_excel("output.xlsx")

df = pd.read_excel('output.xlsx')
merged = map_df.set_index('DISTRICT').join(df.set_index('District'))
merged = merged[['Cluster_Num', 'geometry', 'color']]
# print(len(color_list))
# merged['color'] = color_list
my_cmap = LinearSegmentedColormap.from_list(
    'mycmap', [(0, 'white'), (1/NUM_CLUSTERS, 'firebrick'), (2/NUM_CLUSTERS, 'chocolate'), (3/NUM_CLUSTERS, 'gold'), (4/NUM_CLUSTERS, 'lightgreen'), (5/NUM_CLUSTERS, 'turquoise'), (6/NUM_CLUSTERS, 'blue'), (7/NUM_CLUSTERS, 'purple')])
# print(merged)
fig, ax = plt.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Literacy Clusters in 2007-2008', fontdict={'fontsize': '25', 'fontweight' : '3'})
merged.plot(column='Cluster_Num', cmap=my_cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=False, categorical=False)
# fig.savefig("District_wise_literacy.png", dpi=100)
plt.show()