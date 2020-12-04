import pickle 
import numpy as np
import sys
from cleanerData import *

from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import mutual_info_score
import matplotlib.pyplot as plt

crime_file = open("Crimes","rb")
crime_data = pickle.load(crime_file,encoding='utf-8')
crime_types = ['Crimes_against_Foreigners', 'Crimes_against_Women', 'Reported_SLL', 'SLL_Crimes_by_Jeveniles', 'Cyber_Crimes', 'Reported_IPC', 'Crimes_by_Foreigners', 'Crimes_against_STs', 'Crimes_against_SCs', 'Crimes_against_Children', 'IPC_Crimes_by_Jeveniles', 'Missing_Persons', 'Crimes_against_Senior_Citizens']

crime_map=dict()
crime_map[66] = ['ballari']
crime_map[451] = ['pune rural','pune railway','pune commr.'] 
crime_map[2] = ['w.rly ahmedabad','ahmedabad city','ahmedabad rural']
crime_map[103] = ['chamarajnagar']
crime_map[392] = ['nagpur rural','nagpur railway','nagpur commr.']
crime_map[676] = ['garo hills south west']
crime_map[65] = ['belagavi district','belagavi city']
crime_map[354] = ['mahendergarh']
crime_map[118] = ['chittorgarh']
crime_map[603] = ['villupuram']
crime_map[266] = ['bhabhua']
crime_map[470] = ['ramnathapuram']
crime_map[466] = ['rajkot rural','rajkot city'] 
crime_map[523] = ['sidharthnagar']
crime_map[280] = ['kasganj']
crime_map[330] = ['kushi nagar']
crime_map[649] = ['sambhal']
crime_map[381] = ['navi mumbai','mumbai railway','mumbai commr.']
crime_map[593] = ['subansiri upper']
crime_map[3] = ['ahmadnagar']
crime_map[127] = ['dantewara']
crime_map[554] = ['surat rural','surat city']
crime_map[453] = ['purab medinipur']
crime_map[563] = ['dang']
crime_map[42] = ['banaskantha']
crime_map[569] = ['thoothukudi']
crime_map[650] = ['amethi']
crime_map[221] = ['haridwar']
crime_map[457] = ['purulia']
crime_map[305] = ['coochbehar']
crime_map[613] = ['garo hills west']
crime_map[672] = ['khasi hills south west']
crime_map[314] = ['kollam commr.','kollam rural']
crime_map[642] = ['balodbazar']
crime_map[610] = ['wayanadu']
crime_map[545] = ['garo hills south']
crime_map[592] = ['siang upper']
crime_map[51] = ['baragarh']
crime_map[448] = ['pudukottai']
crime_map[662] = ['gariyaband']
crime_map[581] = ['tumakuru']
crime_map[571] = ['thrissur commr.','thrissur rural']
crime_map[230] = ['hooghly']
crime_map[92] = ['bulandshahar']
crime_map[238] = ['jaintia hills west','jaintia hills east']
crime_map[618] = ['siang west']
crime_map[52] = ['baramulla']
crime_map[331] = ['lahaul & spiti']
crime_map[7] = ['alapuzha']
crime_map[265] = ['kachchh west(b),kachchh east(g)']
crime_map[13] = ['ambala (urban)','ambala (rural)']
crime_map[665] = ['devbhumi dwarka']
crime_map[345] = ['ludhiana rural','cp ludhiana']
crime_map[359] = ['malda']
crime_map[160] = ['dahod']
crime_map[93] = ['buldhana']
crime_map[321] = ['kozhikode commr.','kozhikode rural']
crime_map[46] = ['bengaluru city','bengaluru district']
crime_map[299] = ['khurda']
crime_map[624] = ['kabirdham']
crime_map[288] = ['kasargod']
crime_map[666] = ['arvalli']
crime_map[319] = ['kota city','kota rural']
crime_map[616] = ['khasi hills west']
crime_map[403] = ['nasik commr.','nasik rural']
crime_map[661] = ['siliguri pc', 'siliguri g. r. p.']
crime_map[434] = []
crime_map[196] = []
crime_map[338] = ['leh']
crime_map[172] = ['siang east']
crime_map[432] = []
crime_map[656] = ['mungali']
crime_map[276] = ['kanyakumari']
crime_map[17] = ['cp amritsar']
crime_map[227] = ['hissar']
crime_map[648] = ['']
crime_map[91] = ['badaun']
crime_map[260] = ['jhunjhunu']
crime_map[585] = ['udhamsingh nagar']
crime_map[246] = ['jalore']
crime_map[355] = ['']
crime_map[491] = ['sahebganj']
crime_map[114] = ['chikkamagaluru']
crime_map[36] = ['']
crime_map[264] = ['']
crime_map[651] = ['bemetra']
crime_map[339] = ['lohardagga']
crime_map[54] = ['burdwan']
crime_map[149] = ['dholpur']
crime_map[500] = ['sant kabirnagar']
crime_map[487] = ['sabarkantha']
crime_map[575] = ['trichy city']
crime_map[652] = ['hapur']
crime_map[307] = ['koderma']
crime_map[271] = ['kanchipuram']
crime_map[657] = ['shamli']
crime_map[418] = ['']
crime_map[426] = ['panchmahal']
crime_map[667] = []
crime_map[133] = ['darjeeling']
crime_map[452] = ['']
crime_map[458] = ['raibareilly']
crime_map[511] = ['sbs nagar']
crime_map[430] = ['papum pare city']
crime_map[445] = ['prakasham']
crime_map[252] = ['janjgir']
crime_map[45] = ['bengaluru district','bengaluru city']
crime_map[223] = []
crime_map[195] = ['gautambudh nagar']
crime_map[485] = ['']
crime_map[196] = ['rudra prayag']
crime_map[170] = ['khasi hills east']
crime_map[502] = ['saraikela']
crime_map[173] = ['ernakulam rural','ernakulam commr.']
crime_map[261] = ['jodhpur east','jodhpur rural','jodhpur west','g.r.p.jodhpur']  
crime_map[534] = ['sivagangai']  
crime_map[578] = ['']  
crime_map[456] = ['purnea']  
crime_map[673] = ['jaintia hills east']  
crime_map[405] = ['nawadah']  
crime_map[382] = ['mumbai railway','mumbai commr.','navi mumbai']  
crime_map[450] = ['poonch']  
crime_map[169] = ['kameng east']  
crime_map[352] = ['mahaboob nagar']  
crime_map[635] = []  
crime_map[658] = ['kabirdham']
crime_map[537] = ['solapur rural','solapur commr.']
crime_map[239] = ['jaipur metro','jaipur east','jaipur rural','jaipur south','jaipur west','jaipur north','']
crime_map[242] = ['jalandhar rural','cp jalandhar']
crime_map[135] = []
crime_map[619] = []
crime_map[167] = ['garo hills east']
crime_map[204] = ['gondia']
crime_map[597] = ['vadodara rural','vadodara city','w.rly vadodara']
crime_map[674] = ['garo hills north']
crime_map[231] =['hyderabad city']
crime_map[343] = ['subansiri lower']
crime_map[218] = ['howrah g. r. p.','howrah pc','howrah rural']
crime_map[104] = ['chandoli']
crime_map[615] = ['kameng west']
crime_map[556] = []
crime_map[607] = ['warangal city','warangal rural']
crime_map[564] = ['nilgiris']
crime_map[180] = []
crime_map[561] = []
crime_map[414] = []
crime_map[561] = ['thane commr.','thane rural']
crime_map[15] = ['amravati rural','amravati commr.']
crime_map[659] = []

def pearson_coefficient(vec):
    crime_mean = 0
    edu_mean = 0
    for item in vec:
        edu_mean += item[0]
        crime_mean += item[1]
    num = 0 
    den1 = 0
    den2 = 0 
    crime_mean/=len(vec)
    edu_mean/=len(vec)
    for i in range(0,len(vec)):
        x = vec[i][0]-edu_mean
        y = vec[i][1]-crime_mean
        num+=x*y
        den1+=(x*x)
        den2+=y*y

    z = (np.sqrt(den1*den2))
    ans = num/z
    return ans


def spearman_coefficient(vec):
    def rank(ind,val):
        cnt=1
        for i in range(0,len(vec)):
            if vec[i][ind]<val:
                cnt+=1
        return cnt
    ans=0
    for i in range(0,len(vec)):
        ans += (rank(0,vec[i][0]) - rank(1,vec[i][1]) )**2
    n= len(vec)
    ans=ans*6/((n**2-1)*n)
    return 1-ans



# dic = dict()
not_found = [577, 641, 223, 135, 617, 624, 25, 511, 82, 81, 41]
for YEAR in range(2013,2017):
    CRIME_YEAR = YEAR+1
    vec=[]
    # dic[YEAR]=set()
    for code in range(0,683):
        try:
            if code not in not_found:
                pop = quer(YEAR,code,"TotalPopulation")
                schools = quer(YEAR,code,"GovtSchoolE")
                crime_total=0
                for crime in crime_types:
                    if CRIME_YEAR not in crime_data[crime].keys():
                        continue
                    if code in crime_map.keys():
                        for item in crime_data[crime][CRIME_YEAR][crime_dis].keys():
                            if crime_data[crime][CRIME_YEAR][crime_dis][item]=='':
                                continue
                            crime_total+=int(crime_data[crime][CRIME_YEAR][crime_dis][item])
                        continue
                    for crime_dis in crime_data[crime][CRIME_YEAR].keys():
                        if getDistrictCode(crime_dis)!=-1:
                            if getDistrictCode(crime_dis) == code:
                                for item in crime_data[crime][CRIME_YEAR][crime_dis].keys():
                                    if crime_data[crime][CRIME_YEAR][crime_dis][item]=='':
                                        continue
                                    crime_total+=int(crime_data[crime][CRIME_YEAR][crime_dis][item])
                                break
            if pop > 0:
                vec.append((schools*1000/pop,crime_total*1000/pop))
            # print(vec[-1])
        except:
            pass
            
    print("Pearson correlation coefficient for year "+str(YEAR)+" = "+str(pearson_coefficient(vec)))
    print("Spearman correlation coefficient for year "+str(YEAR)+" = "+str(spearman_coefficient(vec)))



