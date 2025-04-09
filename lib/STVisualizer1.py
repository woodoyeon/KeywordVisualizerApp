import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import pandas as pd
import matplotlib.font_manager as fm  # 폰트 설정용

# ✅ 한글 폰트 설정 (matplotlib 그래프용)
font_path = "NanumGothic-Regular.ttf"  # 업로드한 한글 폰트
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()

# ✅ 단어 수평 막대 그래프 그리기
def plot_freq_bar(df, top_n=20):
    word_freq = df.sum().sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    word_freq.plot(kind='barh')
    plt.gca().invert_yaxis()
    plt.title('Top Words by TF-IDF Score')
    st.pyplot(plt)

# ✅ 워드클라우드 그리기
def plot_wordcloud(df):
    word_freq = df.sum(axis=0).to_dict()

    wc = WordCloud(
        font_path="NanumGothic-Regular.ttf",  # 워드클라우드에도 한글 폰트 지정
        background_color='white',
        width=800,
        height=400
    ).generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    st.pyplot(plt)
