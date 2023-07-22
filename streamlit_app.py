import streamlit as st
import requests
import pandas as pd

def get_data_B(url, output_file):
    # 使用requests模組取得json數據(data_A)
    response = requests.get(url)
    data_A = response.json()

    # 調整data_A成新的內容(data_B)並新增"Holding %"屬性
    data_B = [{"rank": n,
               "wallet": item["wallet"],
               "inscriptions_count": item["inscriptions_count"],
               "Holding %": round(item["inscriptions_count"] / 10000, 4)} 
              for n, item in enumerate(data_A, start=1)]

    # 將data_B寫入JSON檔案
    with open(output_file, 'w') as f:
        json.dump(data_B, f)

    

# 呼叫函數，取得data_B
url = "https://ordapi.bestinslot.xyz/v1/get_collection_snapshot/bitcoin-frogs-snapshot.json"
#data = get_data_B(url)

data_b = [
    {'rank': 4303, 'wallet': 'bc1qrxm4gqvkkwmag72eqjvmjlj97luwdrvzz8g4xm', 'inscriptions_count': 1, 'Holding %': 0.01},
    {'rank': 4304, 'wallet': 'bc1qrxm4gqvkkwmag72eqjvmjlj97luwdrvzz8g4xm', 'inscriptions_count': 1, 'Holding %': 0.01},
    {'rank': 4305, 'wallet': 'bc1qrxm4gqvkkwmag72eqjvmjlj97luwdrvzz8g4xm', 'inscriptions_count': 1, 'Holding %': 0.01},
    {'rank': 4306, 'wallet': 'bc1qrxm4gqvkkwmag72eqjvmjlj97luwdrvzz8g4xm', 'inscriptions_count': 1, 'Holding %': 0.01},
]
# 印出data_B檢查結果
#print(data_B)
output_file = "data_c.json"
get_data_B(url, output_file)

with open("data_c.json", 'r') as f:
    data_f = json.load(f)



# 將data_B轉換成DataFrame
df = pd.DataFrame(data_f)



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
st.dataframe(df,height=630,use_container_width =True,hide_index=True)
