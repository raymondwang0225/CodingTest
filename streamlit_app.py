import streamlit as st
import requests
import pandas as pd

import requests
import pandas as pd

def get_holding_output(url):
    # 使用requests模組取得json數據(holding_input)
    response = requests.get(url)
    holding_input = response.json()

    # 調整holding_input成新的內容(holding_output)並新增"Holding %"屬性
    holding_output = [{"rank": n,
                       "wallet": item["wallet"],
                       "inscriptions_count": item["inscriptions_count"],
                       "Holding List": [i["inscription_number"] for i in item["inscriptions"]]},
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
            "rank": st.column_config.Column(
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
