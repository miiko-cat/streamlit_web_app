import streamlit as st
from PIL import Image

# テキスト関連
st.title('商品管理')
st.caption('Shohinテーブルの中身を確認')

# 画像
Image = Image.open('./data/Lenna.bmp')
st.image(Image, width=200)