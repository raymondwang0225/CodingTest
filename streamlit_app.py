import requests
import pandas as pd

def get_data_B(url):
    # 使用requests模組取得json數據(data_A)
    response = requests.get(url)
    data_A = response.json()

    # 調整data_A成新的內容(data_B)
    data_B = [{"Rank": n,"Wallet": item["wallet"],"Inscriptions Count": item["Inscriptions_count"],"Holding %": round(item["inscriptions_count"] / 100, 4)} for n, item in enumerate(data_A, start=1)]

    return data_B


# Streamlit App
def main():
    # 呼叫函數，取得data_B
    url = "https://ordapi.bestinslot.xyz/v1/get_collection_snapshot/bitcoin-frogs-snapshot.json"
    #data_B = get_data_B(url)
    
    # 印出data_B檢查結果
    #print(data_B)
    data_B =[{'rank': 4367, 'wallet': 'bc1qzs85dl3q7pmvnju20wngzu3czcurul4qhehn2q', 'inscriptions_count': 1, 'Holding %': 0.01}]
    # 將data_B轉換成DataFrame
    df = pd.DataFrame(data_B)
    
    # 顯示DataFrame
    #print(df)

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
    st.dataframe(df,height=630,use_container_width =True,column_config={
            "Rank": st.column_config.Column(
                "Rank",
                width = "small",
                help="Show rank order",
            ),
            "Holding %": st.column_config.ProgressColumn(
                "Holding %",
                width = "large",
                help="Show Holding Percentage",
                format=" %.4f%%",
                min_value=0,
                max_value=10,
            ),
           
        },hide_index=True,)






  
if __name__ == "__main__":
    main()
