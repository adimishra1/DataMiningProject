from matplotlib import pyplot as plt
from cleanerData import *
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

global_max = -1
global_min = 200

for year in small_edu_data:
    if year < 2007:
        continue
    data = []
    for district in small_edu_data[year]:
        try:
            try:
                LiteracyRate = float(small_edu_data[year][district]["LiteracyRate"])
            except:
                print(small_edu_data[year][district]["LiteracyRate"])
            if LiteracyRate==0:
                continue
            data.append(LiteracyRate)
            if LiteracyRate>global_max:
                global_max = LiteracyRate
            if LiteracyRate<global_min:
                global_min = LiteracyRate
        except KeyError:
            print(year, district)
    legend = ['distribution']
    fig, axs = plt.subplots(1, 1, figsize =(7, 5), tight_layout = True)
    for s in ['top', 'bottom', 'left', 'right']:  
        axs.spines[s].set_visible(False)
    axs.xaxis.set_ticks_position('none')
    axs.yaxis.set_ticks_position('none')
    axs.xaxis.set_tick_params(pad = 5)
    axs.yaxis.set_tick_params(pad = 10)
    axs.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.6)
    N, bins, patches = axs.hist(data, bins = [30, 40, 50, 60, 70, 80, 90, 100])
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches): 
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    plt.xlabel("Literacy Rate")
    plt.ylabel("Number of Districts")
    # plt.legend(legend)
    interval = str(year)+"-"
    if(year<2009):
        interval += "0"+str((year%100)+1)
    else:
        interval += str((year%100)+1)
    plt.title(interval)
    plt.show()

print(global_max, global_min)
# print(quer(2016,"Bokaro",'LiteracyRate'))