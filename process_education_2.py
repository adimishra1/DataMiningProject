import pandas
import pickle
import csv

db = {}

for k in range(2002,2017):
    year = str(k)+"-"
    if(k<2009):
        year += "0"+str((k%100)+1)
    else:
        year += str((k%100)+1)

    df_dict = {}
    if k==2004 or k==2010 or k==2011:
        try:
            reader = csv.reader(open(year+'.csv'))
            df_dict = {row[0]:row[1:] for row in reader if row and row[0]}
            new_keys = df_dict.pop("District Name")
            temp_dic = {}
            for j in df_dict.keys():
                temp_dic[j] = dict(zip(new_keys, list(df_dict[j])))
            db[year] = temp_dic
            print(year)
        except:
            s=1
        continue
    if k<2011:
        if k<2005:
            try:
                df_dict = dict(pandas.read_excel(year+".xls", header=[0,1,2,3], sheet_name="Basic Data"))
            except:
                continue
        else:
            try:
                df_dict = dict(pandas.read_excel(year+".xls", header=[0,1,2], sheet_name="Basic Data"))
            except:
                continue
    else:
        try:
            df_dict = dict(pandas.read_excel(year+".xlsx", header=[0,1,2], sheet_name="Basic Data"))
        except:
            continue

    new_keys = []
    final_dic = {}

    for i in df_dict.keys():
        temp = ""
        for j in i:
            if j[0:7]=="Unnamed":
                continue
            temp += j
            temp += ' '
        temp = temp[:-1]
        new_keys.append(temp)

    final_dic = dict(zip(new_keys, list(df_dict.values())))

    out_dic = {}

    for i in final_dic:
        for j in final_dic[i].keys():
            out_dic[j] = {}

    for i in final_dic:
        for j in final_dic[i].keys():
            out_dic[j][i] = final_dic[i][j]

    db[year] = out_dic
    print(year)

dbfile = open('Education', 'wb')
pickle.dump(db, dbfile)
dbfile.close()