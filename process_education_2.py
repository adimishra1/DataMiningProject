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
            # print(year)
            reader = csv.reader(open(year+'.csv'))
            df_dict = {}
            for row in reader:
                if row and row[0]:
                    df_dict[row[0]] = []
                    for j in range(1,len(row)):
                        try:
                            df_dict[row[0]].append(int(row[j]))
                        except:
                            try:
                                df_dict[row[0]].append(float(row[j]))
                            except:
                                df_dict[row[0]].append(row[j])
            # df_dict = {row[0]:row[1:] for row in reader if row and row[0]}
            new_keys = df_dict.pop("District Name")
            temp_dic = {}
            for j in df_dict.keys():
                temp_dic[j] = dict(zip(new_keys, list(df_dict[j])))
            db[year] = temp_dic
            print(year)
            for district in temp_dic.keys():
                for key in temp_dic[district].keys():
                    # if 'Uniform' in key or 'uniform' in key or 'Textbook' in key or 'textbook' in key or 'TextBook' in key or 'Text Book' in key or 'text Book' in key or 'Text book' in key or 'text book' in key:
                    if 'Enrolment' in key and 'Grade' not in key and 'SC ' not in key and 'ST ' not in key and 'OBC ' not in key and 'Madarsas' not in key and 'Medium' not in key and '<=' not in key and 'Muslim' not in key and 'medium of instructions' not in key and 'building' not in key and 'blackboard' not in key:
                        print(key)
                break
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
            # if j=="BALRAMPUR                                         ":
            #     print(type(out_dic[j][i]))
            # if(isinstance(out_dic[j][i], str)):
            #     out_dic[j][i] = int(out_dic[j][i].split(' ')[-1])
            # out_dic[j][i] = str(out_dic[j][i]).split(' ')[-1]

    # print(year)

    # if k==2013:
    #     print(out_dic["BALRAMPUR                                         "])

    db[year] = out_dic
    print(year)
    for district in out_dic.keys():
        for key in out_dic[district].keys():
            # if 'Uniform' in key or 'uniform' in key or 'Textbook' in key or 'textbook' in key or 'TextBook' in key or 'Text Book' in key or 'text Book' in key or 'Text book' in key or 'text book' in key:
            if 'Enrolment' in key and 'Grade' not in key and 'SC ' not in key and 'ST ' not in key and 'OBC ' not in key and 'Madarsas' not in key and 'Medium' not in key and '<=' not in key and 'Muslim' not in key and 'medium of instructions' not in key and 'building' not in key and 'blackboard' not in key:
                print(key)
        break

# print(db["2004-05"])
dbfile = open('Education', 'wb')
pickle.dump(db, dbfile)
dbfile.close()