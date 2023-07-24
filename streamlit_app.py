import streamlit as st
import requests
import pandas as pd
import json
import requests
import pandas as pd



def get_average_cost(item):
    total_cost = 0

    for i in item["inscriptions"]:
        inscription_number = i["inscription_number"]
        print(inscription_number)
        url = f"https://ordapi.bestinslot.xyz/v1/get_inscription_with_number/{inscription_number}"
        response = requests.get(url)
        
        try:
            response.raise_for_status()  # Check if the request was successful
            inscription_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching inscription data for {inscription_number}: {e}")
            continue

        transfers = inscription_data.get("transfers", [])
        last_transfer = transfers[-1] if transfers else None

        if last_transfer and last_transfer["to"] == item["wallet"]:
            if last_transfer["from"] is None:
                total_cost += 0
            else:
                total_cost += last_transfer["psbt_sale"]

    average_cost = total_cost / item["inscriptions_count"] if item["inscriptions_count"] > 0 else 0
    return average_cost

def get_holding_output(url):
    # 使用requests模組取得json數據(holding_input)
    response = requests.get(url)

    try:
        response.raise_for_status()  # Check if the request was successful
        holding_input = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching holding data: {e}")
        return []

    # 調整holding_input成新的內容(holding_output)並新增"Holding %"和"average cost"屬性
    holding_output = []
    for n, item in enumerate(holding_input, start=1):
        average_cost = get_average_cost(item)
        holding_output.append({
            "Rank": n,
            "Wallet": item["wallet"],
            "Inscriptions Count": item["inscriptions_count"],
            "Holding %": round(item["inscriptions_count"] / 10000, 4),
            "Average Cost": average_cost
        })
    return holding_output

# Streamlit App
def main():
     # 呼叫函數，取得holding_output
    url = "https://ordapi.bestinslot.xyz/v1/get_collection_snapshot/bitcoin-frogs-snapshot.json"
    data_holding_output =[]
    file_path = "holding_output.json"
    # 印出holding_output檢查結果
    #print(data_holding_output)
    with open(file_path, "r") as file:
        data_holding_output = json.load(file)


    
    st.set_page_config(layout="wide")

    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    
    st.title("Bitcoin Frogs Holding Data")
    
    #row size 35 px
    st.dataframe(data_holding_output,height=630,use_container_width =True,column_config={
            "Rank": st.column_config.Column(
                "Rank",
                width=None,
                help="Show rank order",
            ),
            "Holding %": st.column_config.ProgressColumn(
                "Holding %",
                width = "small",
                help="Show Holding Percentage",
                format=" %.2f%%",
                min_value=0,
                max_value=100,
            ),
           
        },hide_index=True,)






  
if __name__ == "__main__":
    main()
