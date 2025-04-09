import streamlit as st
import pandas as pd
from lib.NaverNewsCrawler1 import search_naver_news
from lib.myTextMining1 import get_tfidf_vectorizer
from lib.STVisualizer1 import plot_freq_bar, plot_wordcloud
import jpype

# JVM이 아직 시작되지 않았으면 시작
if not jpype.isJVMStarted():
    jpype.startJVM(jpype.getDefaultJVMPath())

st.title("🔍 키워드 기반 뉴스 분석 대시보드")

# ✅ 데이터 입력 방식 선택
option = st.radio("데이터 입력 방식 선택", ('뉴스 검색', 'CSV 파일 업로드'))

if option == '뉴스 검색':
    keyword = st.text_input("검색어 입력")
    if st.button("뉴스 검색") and keyword:
        news_data = search_naver_news(keyword)
        vectorizer, tfidf_matrix = get_tfidf_vectorizer(news_data)
        df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
        st.success("뉴스 수집 및 분석 완료!")

        st.subheader("📊 단어 수 빈도 그래프")
        plot_freq_bar(df)

        st.subheader("☁️ 워드클라우드")
        plot_wordcloud(df)

elif option == 'CSV 파일 업로드':
    uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
    if uploaded_file:
        column_name = st.text_input("분석할 컬럼명 입력")
        if column_name:
            df_data = pd.read_csv(uploaded_file)
            if column_name in df_data.columns:
                docs = df_data[column_name].dropna().tolist()
                vectorizer, tfidf_matrix = get_tfidf_vectorizer(docs)
                df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
                st.success("CSV 데이터 분석 완료!")

                st.subheader("📊 단어 수 빈도 그래프")
                plot_freq_bar(df)

                st.subheader("☁️ 워드클라우드")
                plot_wordcloud(df)
            else:
                st.warning("⚠️ 컬럼명이 CSV에 존재하지 않습니다.")
