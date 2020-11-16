import streamlit as st
import pandas as pd
import base64
import webbrowser
from PIL import Image

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="jaist_lecture_calendar.csv">Download csv file</a>'
    return href

df = pd.read_csv('jaist-lecture.csv')
img1 = Image.open('jl1.png')
img2 = Image.open('jl2.png')
img3 = Image.open('jl3.png')
img4 = Image.open('jl4.png')
img5 = Image.open('jl5.png')

# 以下コンテンツ
st.title('JAIST東京 授業カレンダー登録 2020')
st.markdown('## 1. 授業を選択する')
## 講義選択
lectures = st.multiselect('', df['Subject'].unique().tolist(), ['I214-システム最適化'])
## 選択したデータを表示
data = df[df['Subject'].isin(lectures)]
st.table(data)

st.markdown('## 2. csvをダウンロードする')
st.markdown(get_table_download_link(data), unsafe_allow_html=True)

st.markdown('## 3. グーグルカレンダーを開く')
st.markdown('[Google calendar](https://calendar.google.com/calendar/)', unsafe_allow_html=True)

st.markdown('## 4. 新しいカレンダーを作成する')
st.markdown('サイドバーの+ボタン -> 新しいカレンダーを作成')
st.image(img1)
st.image(img2)
st.markdown('カレンダーに名前を付けて保存')
st.image(img3)

st.markdown('## 5. カレンダーに登録する')
st.markdown('サイドバーの+ボタン -> インポート')
st.image(img4)
st.markdown('作ったカレンダーを選択し、csvをアップロード')
st.image(img5)
st.markdown('おわり')