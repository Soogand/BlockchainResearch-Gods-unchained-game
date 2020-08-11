import requests
import time
import csv
import os
import pandas as pd

url="https://api.godsunchained.com/v0/proto?&perPage=1000"
response = requests.request("GET", url)
data2 = response.json()

proto=[]
card_name=[]
card_effect=[]
god=[]
rarity=[]
mana=[]
type=[]
set=[]

for i in range(0, 980):

    print(i)
    proto.append(data2['records'][i]['id'])
    card_name.append(data2['records'][i]['name'])
    card_effect.append(data2['records'][i]['effect'])
    god.append(data2['records'][i]['god'])
    rarity.append(data2['records'][i]['rarity'])
    mana.append(data2['records'][i]['god'])
    type.append(data2['records'][i]['type'])
    set.append(data2['records'][i]['set'])

    
dict={
    'proto':proto,
    'card_name':card_name,
    'card_effect': card_effect,
    'god':god,
    'rarity':rarity,
    'mana': mana,
    'type': type,
    'set': set
}

df = pd.DataFrame(dict)

path = 'C:\\Users\\...'
df.to_csv(os.path.join(path, "proto.csv"), index=False)



