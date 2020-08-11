import requests
import time
import csv
import os

file1 = open('Links_New_Diamond.txt', 'r')
url_list1 = file1.readlines()

#

for j in range(0, len(url_list1)-1):


    token= url_list1[j].rsplit('/', 1)

    url = "https://api.opensea.io/events/?asset_contract_address=" + "0x0e3a2a1f2146d86a604adc220b4967a898d7fe07" + "&token_id=" + token[1] + "&limit=450"

    #Use this for test on single card:
    #url = "https://api.opensea.io/events/?asset_contract_address=0x0e3a2a1f2146d86a604adc220b4967a898d7fe07&token_id=14586879&limit=450"

    headers = {'x-api-key': '1bdd409b054741deb1b7a84c9201c6c5'}
    response = requests.request("GET", url, headers=headers)

    data= response.json()

    trans=0
    for event in data['asset_events']:
        trans=trans+1



    id=[]
    #transaction happens when an asset is transacted between a user to another
    contract = []
    hash = []

    From_t=[]
    From_t_add=[]
    From_t_discord=[]

    To_t=[]
    To_t_add=[]
    To_t_discord=[]

    timestamp=[]

    ETH_price=[]

    #about the card
    token_id=[]
    num_sale=[]
    name_token=[]
    owner=[]
    link=[]
    seller=[]
    seller_add=[]
    event_type=[]
    auction_type=[]
    st_price=[]
    en_price=[]
    dur=[]
    minprice=[]
    offered_to=[]
    bid_amount=[]
    total_price=[]
    custom_event_name=[]
    quantity=[]
    payout_amount=[]
    event_timestamp=[]

    from_account=[]
    from_account_add=[]
    to_account=[]
    to_account_add=[]

    total_price=[] #price sold

    from_final=[]
    to_final=[]
    from_final_username=[]
    to_final_username=[]

    owner_add=[]

    price=[]

    crypto=[]
    crypto_price=[]

    owned_by=[]
    owned_by_username=[]

    all_owners = []
    all_owners_username = []

    i = 0
    if trans>1:
        while i < trans:
            id.append(data['asset_events'][i]['id'])
            contract.append(data['asset_events'][i]['contract_address'])

            if data['asset_events'][i]['payment_token'] != None:
                crypto.append(data['asset_events'][i]['payment_token']['name'])
                crypto_price.append(data['asset_events'][i]['payment_token']['usd_price'])
            else:
                crypto.append(0)
                crypto_price.append(0)

            if data['asset_events'][i]['transaction']!=None:
                if data['asset_events'][i]['transaction']['transaction_hash'] != None:
                    hash.append(data['asset_events'][i]['transaction']['transaction_hash'])
                else:
                    hash.append(0)

                if data['asset_events'][i]['transaction']['from_account'] != None:
                    From_t_add.append(data['asset_events'][i]['transaction']['from_account']['address'])
                    From_t_discord.append(data['asset_events'][i]['transaction']['from_account']['discord_id'])
                    if data['asset_events'][i]['transaction']['from_account']['user'] != None:
                       From_t.append(data['asset_events'][i]['transaction']['from_account']['user']['username'])
                    else:
                        From_t.append(0)
                else:
                    From_t_add.append(0)
                    From_t_discord.append(0)

                if data['asset_events'][i]['transaction']['to_account'] != None:
                    To_t_add.append(data['asset_events'][i]['transaction']['to_account']['address'])
                    To_t_discord.append(data['asset_events'][i]['transaction']['to_account']['discord_id'])
                    if data['asset_events'][i]['transaction']['to_account']['user'] != None:
                        To_t.append(data['asset_events'][i]['transaction']['to_account']['user']['username'])
                    else:
                        To_t.append(0)
                else:
                    To_t_add.append(0)
                    To_t_discord.append(0)

                timestamp.append(data['asset_events'][i]['transaction']['timestamp'])

            else:
                From_t.append(0)
                From_t_add.append(0)
                From_t_discord.append(0)
                To_t.append(0)
                To_t_add.append(0)
                To_t_discord.append(0)
                timestamp.append(0)
                hash.append(0)

            if data['asset_events'][i]['asset'] != None:
                token_id.append(data['asset_events'][i]['asset']['token_id'])
                num_sale.append(data['asset_events'][i]['asset']['num_sales'])
                name_token.append(data['asset_events'][i]['asset']['name'])

                link.append(data['asset_events'][i]['asset']['permalink'])

                if data['asset_events'][i]['asset']['owner'] != None:
                    owner_add.append(data['asset_events'][i]['asset']['owner']['address'])
                    if data['asset_events'][i]['asset']['owner']['user'] != None:
                        owner.append(data['asset_events'][i]['asset']['owner']['user']['username'])
                    else:
                        owner.append(0)
                else:
                    owner.append(0)
                    owner_add.append(0)
            else:
                token_id.append(0)
                num_sale.append(0)
                name_token.append(0)
                owner.append(0)
                link.append(0)

            if data['asset_events'][i]['seller'] != None:
                seller_add.append(data['asset_events'][i]['seller']['address'])
                if data['asset_events'][i]['seller']['user'] != None:
                   seller.append(data['asset_events'][i]['seller']['user']['username'])
                else:
                    seller.append(0)
            else:
                seller.append(0)
                seller_add.append(0)

            event_type.append(data['asset_events'][i]['event_type'])
            auction_type.append(data['asset_events'][i]['auction_type'])

            if data['asset_events'][i]['starting_price'] !=None:
                st_price.append(data['asset_events'][i]['starting_price'])
            else:
                st_price.append(0)

            if data['asset_events'][i]['ending_price'] !=None:
                en_price.append(data['asset_events'][i]['ending_price'])
            else:
                en_price.append(0)

            dur.append(data['asset_events'][i]['duration'])
            minprice.append(data['asset_events'][i]['min_price'])
            offered_to.append(data['asset_events'][i]['offered_to'])

            if data['asset_events'][i]['bid_amount'] !=None:
                bid_amount.append(data['asset_events'][i]['bid_amount'])
            else:
                bid_amount.append(0)

            if data['asset_events'][i]['total_price'] !=None:
                total_price.append(data['asset_events'][i]['total_price'])
            else:
                total_price.append(0)

            custom_event_name.append(data['asset_events'][i]['custom_event_name'])
            quantity.append(data['asset_events'][i]['quantity'])
            payout_amount.append(data['asset_events'][i]['payout_amount'])
            event_timestamp.append(data['asset_events'][i]['event_timestamp'])


            if data['asset_events'][i]['from_account'] != None:
                from_account_add.append(data['asset_events'][i]['from_account']['address'])
                if data['asset_events'][i]['from_account']['user'] != None:
                    from_account.append(data['asset_events'][i]['from_account']['user']['username'])
                else:
                    from_account.append(0)
            else:
                from_account.append(0)
                from_account_add.append(0)

            if data['asset_events'][i]['to_account'] != None:
                to_account_add.append(data['asset_events'][i]['to_account']['address'])
                if data['asset_events'][i]['to_account']['user'] != None:
                    to_account.append(data['asset_events'][i]['to_account']['user']['username'])
                else:
                    to_account.append(0)
            else:
                to_account.append(0)
                to_account_add.append(0)

            i = i + 1

        ###Correct From and To
        jj=0

        while jj < trans:
            if from_account_add[jj] !=0:
                from_final.append(from_account_add[jj])
                from_final_username.append(from_account[jj])
            else:
                from_final.append(From_t_add[jj])
                from_final_username.append(From_t[jj])

            if to_account_add[jj] != 0:
                to_final.append(to_account_add[jj])
                to_final_username.append(to_account[jj])
            else:
                to_final.append(To_t_add[jj])
                to_final_username.append(To_t[jj])

            jj=jj+1


        bid_amount=[int(x) for x in bid_amount]
        total_price=[int(x) for x in total_price]
        st_price=[int(x) for x in st_price]

        bid_amount[:] = [x / 1000000000000000000 for x in bid_amount]
        total_price[:] = [x / 1000000000000000000 for x in total_price]
        st_price[:] = [x / 1000000000000000000 for x in st_price]

        jj=0
        while jj < trans:
            if bid_amount[jj] !=0:
                price.append(bid_amount[jj])
            else:
                price.append(total_price[jj])

            if price[jj]== 0:
                price[jj]=st_price[jj]

            jj = jj + 1


    ## To create the SOLD label##
    ## run the delete row.py file as well.
        jj=0
        while jj < trans:

            if event_type[jj]=="successful":
                if jj==0:
                    if seller_add[jj] == from_final[jj + 1] and event_type[jj + 1] == "transfer":
                        event_type[jj + 1] = "sold"
                        price[jj + 1] = price[jj]
                        seller_add[jj + 1] = seller_add[jj]
                        seller[jj + 1] = seller[jj]
                        crypto[jj + 1] = crypto[jj]

                elif jj==trans-1:
                    if seller_add[jj] == from_final[jj - 1] and event_type[jj - 1] == "transfer":
                        event_type[jj - 1] = "sold"
                        price[jj - 1] = price[jj]
                        seller_add[jj - 1] = seller_add[jj]
                        seller[jj - 1] = seller[jj]
                        crypto[jj - 1] = crypto[jj]

                else:

                    if seller_add[jj] == from_final[jj + 1] and event_type[jj + 1] == "transfer":
                        event_type[jj + 1] = "sold"
                        price[jj + 1] = price[jj]
                        seller_add[jj + 1] = seller_add[jj]
                        seller[jj + 1] = seller[jj]
                        crypto[jj + 1] = crypto[jj]

                    else:
                        if seller_add[jj] == from_final[jj - 1] and event_type[jj - 1] == "transfer":
                            event_type[jj - 1] = "sold"
                            price[jj - 1] = price[jj]
                            seller_add[jj - 1] = seller_add[jj]
                            seller[jj - 1] = seller[jj]
                            crypto[jj - 1] = crypto[jj]


            jj = jj + 1

        #Make the "owned_by" column
        jj=0
        while jj<trans:
            owned_by.append(0)
            owned_by_username.append(0)

            jj=jj+1

        jj=0
        nn=0 # to see if stays 0 means that people only made offers
        while jj<trans:

            if event_type[jj] == "transfer":
                owned_by[jj]=to_final[jj]
                owned_by_username[jj]= to_final_username[jj]
                nn=nn+1

            if event_type[jj] == "sold":
                owned_by[jj]=to_final[jj]
                owned_by_username[jj]= to_final_username[jj]
                nn = nn + 1

            jj= jj+1

        jj=0
        if nn==0:
            while jj < trans:
                owned_by[jj] = owner_add[jj]
                owned_by_username[jj] = owner[jj]
                jj=jj+1

        else:
            jj=0
            all_from=[]
            all_from_username=[]

            while jj<trans:
                if owned_by[jj]!=0:
                    all_owners.append(owned_by[jj])
                    all_from.append(from_final[jj])
                    all_owners_username.append(owned_by_username[jj])
                    all_from_username.append(from_final_username[jj])
                jj=jj+1

            #print(len(all_from))
            m=len(all_from)
            #print(all_from[m-1])


            all_owners.append(all_from[m-1]) #To keep the last element of the array in place
            all_owners_username.append(all_from_username[m-1])



            jj=0
            i=0
            while jj<trans:
                if owned_by[jj]!=0:
                    i=i+1

                else:
                    owned_by[jj]= all_owners[i]
                    owned_by_username[jj]=all_owners_username[i]

                jj=jj+1





        import pandas as pd
        dict={'name_token':name_token,
              'token_id': token_id,
              'event_type':event_type,
              'auction_type':auction_type,
              'crypto'    :crypto,
              'price'  : price,
              'from_final': from_final,
              'from_final_username':from_final_username,
              'to_final': to_final,
              'to_final_username': to_final_username,
              'owned_by': owned_by,
              'owned_by_username': owned_by_username,
              #'seller': seller_add,
              #'seller_username': seller,
              'event_timestamp':event_timestamp,
              'link' : link,
              'transaction_hash': hash,
              'contract_address': contract,
              'Blockchain_from': From_t,
              'Blockchain_from_address': From_t_add,
              'Blockchain_to': To_t,
              'Blockchain_to_address': To_t_add,

            }

        df = pd.DataFrame(dict)
        df = df[df['event_type'] != "successful"] #delete the succesful row.


        path='C:\\Users\\....'

        df.to_csv(os.path.join(path, str(name_token[0]) + ".csv"), index=False)
      


        print(j)
        #time.sleep(2)
        #quit()



