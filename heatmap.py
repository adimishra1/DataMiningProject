import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

map_df = gpd.read_file('Census_2011/2011_Dist.shp')
df = pd.read_excel('datafile.xls')
map_df = map_df[['DISTRICT', 'geometry']]
data = df[['District/ Area', 'Total Crimes against Women']]
merged = map_df.set_index('DISTRICT').join(data.set_index('District/ Area'))
merged['Total Crimes against Women'].fillna(merged['Total Crimes against Women'].mean(), inplace=True)
fig, ax = plt.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('District Wise Crime against women in India in 2015', fontdict={'fontsize': '25', 'fontweight' : '3'})
merged.plot(column='Total Crimes against Women', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
fig.savefig("District_wise.png", dpi=100)
