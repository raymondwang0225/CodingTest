import requests
import pandas as pd


data_B  =  {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
# 將data_B轉換成DataFrame
df = pd.DataFrame(data_B)



st.title("Bitcoin Frogs Holding Data")

st.table(df)
