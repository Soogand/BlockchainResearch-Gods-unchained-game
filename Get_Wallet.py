import requests
import time
import csv
import os
import pandas as pd

col_list1 = ["cardtype","username_opensea", "address", "username_game"]
df1 = pd.read_csv("profiles.csv", usecols=col_list1)



#
for j in range(0,len(df1) ): #usernames in opensea
    print(j)
    user=[]
    proto=[]
    purity=[]
    card_name=[]
    card_effect=[]
    god=[]
    rarity=[]
    mana=[]
    type=[]
    set=[]

    print(df1['address'][j])

    url1 = "https://api.godsunchained.com/v0/card?user="+df1['address'][j]+"&perPage=150000"
    print (url1)
    response = requests.request("GET", url1)
    data = response.json()


    number_cards=data['total']
    if number_cards!=0:
        for i in range(0, number_cards):
            user.append(data['records'][i]['user'])
            proto.append(data['records'][i]['proto'])
            url2 = "https://api.godsunchained.com/v0/proto/" + str(proto[i])
    
            purity.append(data['records'][i]['purity'])
    
            # response2 = requests.request("GET", url2)
            # data2 = response2.json()
    
            # if data2['name']!=None:
            #     card_name.append(data2['name'])
            #     card_effect.append(data2['effect'])
            #     god.append(data2['god'])
            #     rarity.append(data2['rarity'])
            #     mana.append(data2['god'])
            #     type.append(data2['type'])
            #     set.append(data2['set'])
            # else:
            #     card_name.append(None)
            #     card_effect.append(None)
            #     god.append(None)
            #     rarity.append(None)
            #     mana.append(None)
            #     type.append(None)
            #     set.append(None)
    
    
        dict={
            'user': user,
            'proto_number': proto,
            # 'card_name':card_name,
            'purity': purity,
            # 'card_effect': card_effect,
            # 'god':god,
            # 'rarity':rarity,
            # 'mana': mana,
            # 'type': type,
            # 'set': set
        }
    
        df = pd.DataFrame(dict)
    
        path = 'C:\\Users\\...'
        df.to_csv(os.path.join(path, str(user[0]) + ".csv"), index=False)

