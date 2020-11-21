import sys
import pickle
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# map_df = gpd.read_file('Census_2011/2011_Dist.shp')
# map_df = map_df[['DISTRICT', 'ST_NM', 'geometry']]

# districts = list(map_df["DISTRICT"])
# states = list(map_df["ST_NM"])
# global_map = dict()

# for i in range(len(districts)):
# 	global_map[districts[i].lower() + "_" + states[i].lower()] = i

# global_file = open("global_map.pkl","wb")
# pickle.dump(global_map, global_file)
# global_file.close()

global_dict_file = open("global_map.pkl","rb")
global_map = pickle.load(global_dict_file,encoding='utf-8')
global_dict_file.close()

old_id = -1
for district in global_map:
	old_id = max(old_id, global_map[district])
new_id = old_id+1
not_present = open('Not_Present', 'r')
for line in not_present:
	line_split = line.strip().split(',')
	if line_split[1] == '': #Assign new id
		global_map[line_split[0].lower()] = new_id
		new_id = new_id + 1
	else:
		global_map[line_split[0].lower()] = int(line_split[1])

print(old_id, new_id,len(global_map))

global_file = open("global_map.pkl","wb")
pickle.dump(global_map, global_file)
global_file.close()