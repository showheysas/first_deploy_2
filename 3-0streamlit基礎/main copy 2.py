import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Hello World') # タイトル

st.write('DataFrame') # テキストの表示

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)   # データフレームの作成

st.write(df)

st.line_chart(df) # 折れ線グラフの表示
st.area_chart(df) # エリアグラフの表示

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df) # 地図の表示