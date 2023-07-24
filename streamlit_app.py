import streamlit as st
import requests
import pandas as pd
import json
import requests
import pandas as pd


# Streamlit App
def main():
     # 呼叫函數，取得holding_output
    #url = "https://ordapi.bestinslot.xyz/v1/get_collection_snapshot/bitcoin-frogs-snapshot.json"
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
