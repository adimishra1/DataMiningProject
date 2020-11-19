import sys
import pickle
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

map_df = gpd.read_file('Census_2011/2011_Dist.shp')
map_df = map_df[['DISTRICT', 'ST_NM', 'geometry']]

districts = list(map_df["DISTRICT"])
states = list(map_df["ST_NM"])
global_map = dict()

for i in range(len(districts)):
	global_map[districts[i].lower() + "_" + states[i].lower()] = i

global_file = open("global_map.pkl","wb")
pickle.dump(global_map, global_file)
global_file.close()