import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit基礎をやってみる。ワクワク')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}) # データフレームの作成

st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

st.table(df.style.highlight_max(axis=0))