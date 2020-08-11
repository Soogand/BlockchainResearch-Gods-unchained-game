import requests
import time
import csv
import os
import pandas as pd

col_list = ["CardType","OwnerName_Opensea", "owned_by"]
df = pd.read_csv("SELLERS.csv", usecols=col_list)

for j in range(0,len(df)): #remember that the text file should not have an enter at the end

    url = "https://api.godsunchained.com/v0/user/" + df["owned_by"][j]
    print (url)
    response = requests.request("GET", url)
    data= response.json()

    cardtype.append(df["CardType"][j])
    username_opensea.append(df["OwnerName_Opensea"][j])
    address.append(df["owned_by"][j])

    print(response.status_code)

    if response.status_code==500:
        username_game.append(None)
    else:
        username_game.append(data['username'])

    print (j)

dict={
    'cardtype': cardtype,
    'username_opensea': username_opensea,
    'address':address,
    'username_game':username_game
}

df = pd.DataFrame(dict)

path = 'C:\\Users\\...'
df.to_csv(os.path.join(path, "Username_Game.csv"), index=False)





