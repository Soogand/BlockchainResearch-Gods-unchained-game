import csv
import os
import pandas as pd

cardtype=[]
username_opensea=[]
address=[]
username_game=[]

col_list1 = ["OwnerName","NoName", "address"]
col_list2 = ["user_id", "username_game","match_count", "total_wins", "total_losses", "max_mmr", "min_mmr",	"xp_level",	"rating","rank","rank_name","unique_opponents",	"opp_avg_mmr",	"average_rounds"]
df1 = pd.read_csv("Addresses_Update.csv", usecols=col_list1)
df2 = pd.read_csv("allplayers.csv", usecols=col_list2)

m=0

with open(r'FINAL_PROFILES_OPENSEA.csv', 'a',  newline='', encoding="utf-8") as f:
    fields=['cardtype', 'username_opensea', 'address', 'username_game1','matched','user_id','username_game', 'match_count','total_wins','total_losses', 'max_mmr', 'min_mmr', 'xp_level', 'rating', 'rank', 'rank_name', 'unique_opponents', 'opp_avg_mmr','average_rounds']
    writer = csv.writer(f)
    writer.writerow(fields)

    for j in range(0,10):
        print(j)

        m=0

        for i in range (0, len(df2)):
            if df1['username_game'][j]==df2['username_game'][i]: #if username matched
                cardtype= df1['cardtype'][j]
                username_opensea= df1['username_opensea'][j]
                address= df1['address'][j]
                username_game1= df1['username_game'][j]
                matched="yes"
                user_id= df2['user_id'][i]
                username_game= df2['username_game'][i]
                match_count= df2['match_count'][i]
                total_wins= df2['total_wins'][i]
                total_losses= df2['total_losses'][i]
                max_mmr = df2['max_mmr'][i]
                min_mmr = df2['min_mmr'][i]
                xp_level=df2['xp_level'][i]
                rating=df2['rating'][i]
                rank= df2['rank'][i]
                rank_name=df2['rank_name'][i]
                unique_opponents= df2['unique_opponents'][i]
                opp_avg_mmr= df2['opp_avg_mmr'][i]
                average_rounds= df2['average_rounds'][i]

                fields = [cardtype, username_opensea, address, username_game1,matched, user_id, username_game, match_count,
                          total_wins, total_losses, max_mmr, min_mmr, xp_level, rating, rank, rank_name,
                          unique_opponents, opp_avg_mmr, average_rounds]
                writer = csv.writer(f)
                writer.writerow(fields)

                m=m+1 #incase we have multiple similar usernames this will be more than 2


        if m==0: #after going through all player usernames if nothing matched
            cardtype= df1['cardtype'][j]
            username_opensea= df1['username_opensea'][j]
            address= df1['address'][j]
            username_game1= df1['username_game'][j]
            matched="no"
            user_id= None
            username_game= None
            match_count= None
            total_wins= None
            total_losses= None
            max_mmr = None
            min_mmr = None
            xp_level= None
            rating=None
            rank= None
            rank_name= None
            unique_opponents= None
            opp_avg_mmr= None
            average_rounds= None
            fields = [cardtype, username_opensea, address, username_game1,matched, user_id, username_game, match_count,
                      total_wins, total_losses, max_mmr, min_mmr, xp_level, rating, rank, rank_name,
                      unique_opponents, opp_avg_mmr, average_rounds]
            writer = csv.writer(f)
            writer.writerow(fields)




