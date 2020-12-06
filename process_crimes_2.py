import os
import csv
import pickle

Crimes_against_Children=dict()
Crimes_against_Foreigners=dict()
Crimes_against_SCs=dict()
Crimes_against_Senior_Citizens=dict()
Crimes_against_STs=dict()
Crimes_against_Women=dict()
Crimes_by_Foreigners=dict()
Reported_IPC=dict()
Reported_SLL=dict()
Cyber_Crimes=dict()
IPC_Crimes_by_Jeveniles=dict()
SLL_Crimes_by_Jeveniles=dict()
Missing_Persons=dict()

for i in range(2014,2020):
    year = str(i)
    try:   
        reader = csv.reader(open(year+'/Crimes_against_Children_'+year+'.csv'))
        Crimes_against_Children[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_Children[i].pop("District")
        for j in Crimes_against_Children[i].keys():
            Crimes_against_Children[i][j] = dict(zip(new_keys, list(Crimes_against_Children[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_against_Foreigners_'+year+'.csv'))
        Crimes_against_Foreigners[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_Foreigners[i].pop("District")
        for j in Crimes_against_Foreigners[i].keys():
            Crimes_against_Foreigners[i][j] = dict(zip(new_keys, list(Crimes_against_Foreigners[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_against_SCs_'+year+'.csv'))
        Crimes_against_SCs[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_SCs[i].pop("District")
        for j in Crimes_against_SCs[i].keys():
            Crimes_against_SCs[i][j] = dict(zip(new_keys, list(Crimes_against_SCs[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_against_Senior_Citizens_'+year+'.csv'))
        Crimes_against_Senior_Citizens[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_Senior_Citizens[i].pop("District")
        for j in Crimes_against_Senior_Citizens[i].keys():
            Crimes_against_Senior_Citizens[i][j] = dict(zip(new_keys, list(Crimes_against_Senior_Citizens[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_against_STs_'+year+'.csv'))
        Crimes_against_STs[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_STs[i].pop("District")
        for j in Crimes_against_STs[i].keys():
            Crimes_against_STs[i][j] = dict(zip(new_keys, list(Crimes_against_STs[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_against_Women_'+year+'.csv'))
        Crimes_against_Women[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_against_Women[i].pop("District")
        for j in Crimes_against_Women[i].keys():
            Crimes_against_Women[i][j] = dict(zip(new_keys, list(Crimes_against_Women[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Crimes_by_Foreigners_'+year+'.csv'))
        Crimes_by_Foreigners[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Crimes_by_Foreigners[i].pop("District")
        for j in Crimes_by_Foreigners[i].keys():
            Crimes_by_Foreigners[i][j] = dict(zip(new_keys, list(Crimes_by_Foreigners[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Reported_IPC_'+year+'.csv'))
        Reported_IPC[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Reported_IPC[i].pop("District")
        for j in Reported_IPC[i].keys():
            Reported_IPC[i][j] = dict(zip(new_keys, list(Reported_IPC[i][j])))
    except:
        s=1
    try:
        reader = csv.reader(open(year+'/Reported_SLL_'+year+'.csv'))
        Reported_SLL[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Reported_SLL[i].pop("District")
        for j in Reported_SLL[i].keys():
            Reported_SLL[i][j] = dict(zip(new_keys, list(Reported_SLL[i][j])))
    except:
        s=1
    try:   
        reader = csv.reader(open(year+'/Cyber_Crimes_'+year+'.csv'))
        Cyber_Crimes[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Cyber_Crimes[i].pop("District")
        for j in Cyber_Crimes[i].keys():
            Cyber_Crimes[i][j] = dict(zip(new_keys, list(Cyber_Crimes[i][j])))
    except:
        s=1
    try:   
        reader = csv.reader(open(year+'/IPC_Crimes_by_Jeveniles_'+year+'.csv'))
        IPC_Crimes_by_Jeveniles[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = IPC_Crimes_by_Jeveniles[i].pop("District")
        for j in IPC_Crimes_by_Jeveniles[i].keys():
            IPC_Crimes_by_Jeveniles[i][j] = dict(zip(new_keys, list(IPC_Crimes_by_Jeveniles[i][j])))
    except:
        s=1
    try:   
        reader = csv.reader(open(year+'/SLL_Crimes_by_Jeveniles_'+year+'.csv'))
        SLL_Crimes_by_Jeveniles[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = SLL_Crimes_by_Jeveniles[i].pop("District")
        for j in SLL_Crimes_by_Jeveniles[i].keys():
            SLL_Crimes_by_Jeveniles[i][j] = dict(zip(new_keys, list(SLL_Crimes_by_Jeveniles[i][j])))
    except:
        s=1
    try:   
        reader = csv.reader(open(year+'/Missing_Persons_'+year+'.csv'))
        Missing_Persons[i] = {row[0]:row[1:] for row in reader if row and row[0]}
        new_keys = Missing_Persons[i].pop("District")
        for j in Missing_Persons[i].keys():
            Missing_Persons[i][j] = dict(zip(new_keys, list(Missing_Persons[i][j])))
    except:
        s=1

db=dict()
db["Crimes_against_Children"] = Crimes_against_Children
db["Crimes_against_Foreigners"] = Crimes_against_Foreigners
db["Crimes_against_SCs"] = Crimes_against_SCs
db["Crimes_against_Senior_Citizens"] = Crimes_against_Senior_Citizens
db["Crimes_against_STs"] = Crimes_against_STs
db["Crimes_against_Women"] = Crimes_against_Women
db["Crimes_by_Foreigners"] = Crimes_by_Foreigners
db["Reported_IPC"] = Reported_IPC
db["Reported_SLL"] = Reported_SLL
db["Cyber_Crimes"] = Cyber_Crimes
db["IPC_Crimes_by_Jeveniles"] = IPC_Crimes_by_Jeveniles
db["SLL_Crimes_by_Jeveniles"] = SLL_Crimes_by_Jeveniles
db["Missing_Persons"] = Missing_Persons
dbfile = open('Crimes', 'ab')
pickle.dump(db, dbfile)                      
dbfile.close()