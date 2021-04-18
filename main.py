import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
import time

st.title('streamlit 超入門')

st.write('DataFrame')

st.write('DisplayImage')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

option2 = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味: ', option2

option = st.selectbox(
    'あなたが好きな数字を教えてください: ',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

condition = st.slider('今の調子は？', 0, 100, 50)
'調子: ', condition

if st.checkbox('Show Image'):
    img = Image.open('nazoX.jpeg')
    st.image(img, caption='Nazo X', use_column_width=True)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#st.table(df.style.highlight_max(axis=0))

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#st.map(df2)
"""
# 章
## 節
### 項
"""