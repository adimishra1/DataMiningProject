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
warnings.filterwarnings("ignore")

map_data = gpd.read_file('Census_2011/2011_Dist.shp')
temp = map_data["geometry"]
district_coords = temp.to_crs("crs").centroid
max_district_code = len(temp)
year = 2016

def get_coordinates(dist_code): #returns [longitude, latitude] for the corresponding district
	return [district_coords[dist_code].xy[0][0], district_coords[dist_code].xy[1][0]]

def get_distance(dist1_code, dist2_code):
	d1_cs = get_coordinates(dist1_code)
	d2_cs = get_coordinates(dist2_code)
	return math.sqrt((d1_cs[0] - d2_cs[0])**2 + (d1_cs[1] - d2_cs[1])**2)

def are_neighbours(dist1_code, dist2_code):
	distance = get_distance(dist1_code, dist2_code)
	threshold = 2.5
	return (distance < threshold)


for i in range(max_district_code):

# print(get_distance(89, 474)) #Bokaro & Ranchi
# print(get_distance(474, 225)) #Ranchi & Hazaribagh
# print(get_distance(279, 344)) #Kanpur & Lucknow
# print(get_distance(240, 56))
# print(get_distance(240, 84))
# print(are_neighbours(89, 1))