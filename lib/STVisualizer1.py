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
def plot_wordcloud(df):
    word_freq = df.sum(axis=0).to_dict()

    # 폰트 경로 지정 (예: 프로젝트에 업로드된 폰트)
    font_path = "NanumGothic-Regular"

    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400
    ).generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
