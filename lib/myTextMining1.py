from konlpy.tag import Okt
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# 사용자 정의 토크나이저 함수
def my_tokenizer(text):
    text = re.sub(r'[^\uAC00-\uD7A3\s]', '', text)  # 한글과 공백만 남김
    okt = Okt()
    tokens = okt.morphs(text)
    stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '도', '으로', '하고']
    return [word for word in tokens if word not in stopwords]

# TF-IDF 벡터라이저 생성 및 변환 함수
def get_tfidf_vectorizer(docs):
    vectorizer = TfidfVectorizer(tokenizer=my_tokenizer, max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(docs)
    return vectorizer, tfidf_matrix