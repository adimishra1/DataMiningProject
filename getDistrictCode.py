import pickle


global_dict_file = open("global_map.pkl","rb")
global_map = pickle.load(global_dict_file,encoding='utf-8')
global_dict_file.close()

def getDistrictCode(dist_name):
	for dist in global_map:
		if "_" in dist:
			if dist_name.strip().lower() == dist.split("_")[0]:
				return global_map[dist]
		else:
			if dist_name.strip().lower() == dist:
				return global_map[dist]
	return -1



