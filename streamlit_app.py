import streamlit as st
import requests
import pandas as pd

import requests
import pandas as pd



def get_average_cost(item):
    total_cost = 0

    for inscription_number in item["inscriptions"]:
        url = f"https://ordapi.bestinslot.xyz/v1/get_inscription_with_number/{inscription_number}"
        response = requests.get(url)
        inscription_data = response.json()

        transfers = inscription_data.get("transfers", [])
        last_transfer = transfers[-1] if transfers else None

        if last_transfer and last_transfer["to"] == item["wallet"]:
            if last_transfer["from"] is None:
                total_cost += 0
            else:
                total_cost += last_transfer["psbt_sale"]

    average_cost = total_cost / len(item["inscriptions"]) if len(item["inscriptions"]) > 0 else 0
    print(average_cost)
    return average_cost


def get_holding_output(url):
    # 使用requests模組取得json數據(holding_input)
    response = requests.get(url)
    holding_input = response.json()
    holding_output = []
    # 調整holding_input成新的內容(holding_output)並新增"Holding %"屬性
    holding_output = [{"Rank": n,
                       "Wallet": item["wallet"],
                       "Inscriptions Count": item["inscriptions_count"],
                       "average cost": average_cost,
                       "Holding %": round(item["inscriptions_count"] / 100, 4)} 
                      for n, item in enumerate(holding_input, start=1)]

    return holding_output





# Streamlit App
def main():
     # 呼叫函數，取得holding_output
    url = "https://ordapi.bestinslot.xyz/v1/get_collection_snapshot/bitcoin-frogs-snapshot.json"
    data_holding_output = get_holding_output(url)
    
    # 印出holding_output檢查結果
    #print(data_holding_output)

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
