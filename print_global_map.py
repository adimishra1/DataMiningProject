import sys
import pickle

global_dict_file = open("global_map.pkl","rb")
global_map = pickle.load(global_dict_file,encoding='utf-8')
global_dict_file.close()

for district in global_map:
	print(district, " -> ", global_map[district])
