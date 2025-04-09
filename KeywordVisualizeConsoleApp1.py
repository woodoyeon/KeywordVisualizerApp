from lib.NaverNewsCrawler1 import search_naver_news
from lib.myTextMining1 import get_tfidf_vectorizer
import pandas as pd

# 키워드 입력
keyword = input("검색어를 입력하세요: ")

# 뉴스 검색
print("[1단계] 뉴스 수집 중...")
news_data = search_naver_news(keyword)

if not news_data:
    print("❌ 뉴스 검색 결과가 없습니다.")
    exit()

# TF-IDF 분석
print("[2단계] 단어 중요도 분석 중...")
vectorizer, tfidf_matrix = get_tfidf_vectorizer(news_data)

# 결과 출력
print("[3단계] 분석 결과:")
print("▶ 단어 목록:")
print(vectorizer.get_feature_names_out())

print("\n▶ TF-IDF 행렬:")
print(tfidf_matrix.toarray())

# DataFrame으로 보기 좋게 출력
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print("\n▶ TF-IDF DataFrame (상위 5개 문서):")
print(df.head())
