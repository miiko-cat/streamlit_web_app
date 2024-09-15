import streamlit as st
import pandas as pd

# データ分析関連
df = pd.read_csv('./data/平均気温.csv', index_col='月')
# st.dataframe(df)
# st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])

# matplotlib
# 動かないので、後でmatplotlibを学習
# fig, ax = plt.subplot()
# ax.plot(df.index, df['2021年'])
# ax.set_title('matplotlib graph')
# st.pyplot(fig)