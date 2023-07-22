import requests
import pandas as pd


data_B  = {'Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks'}
# 將data_B轉換成DataFrame
df = pd.DataFrame(data_B)



st.title("Bitcoin Frogs Holding Data")

st.table(df)
