import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門') # タイトル

st.write('画像の表示') #画像の表示

img = Image.open('pic/main_img_202108.jpeg') # 画像の読み込み
#st.image(img, caption='main_img_202108', use_column_width=True) # 
st.image(img, caption='main_img_202108', use_container_width=True) # 

#use_column_widthは今後削除される予定
#https://chatgpt.com/share/67550beb-8f28-8008-9ac3-c752984c1caf