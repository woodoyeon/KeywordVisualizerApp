import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import pandas as pd

# ✅ 단어 수평 막대 그래프 그리기
def plot_freq_bar(df, top_n=20):
    word_freq = df.sum().sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    word_freq.plot(kind='barh')
    plt.gca().invert_yaxis()  # 가장 많은 단어가 위로 오도록
    plt.title('Top Words by TF-IDF Score')
    st.pyplot(plt)

# ✅ 워드클라우드 그리기
def plot_wordcloud(df, top_n=50):
    word_freq = df.sum().sort_values(ascending=False).head(top_n)
    wordcloud = WordCloud(
        font_path="./NanumGothic.ttf",  # 한글 폰트 경로 필요
        background_color='white',
        width=800,
        height=400
    ).generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
