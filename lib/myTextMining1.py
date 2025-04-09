from konlpy.tag import Okt
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# 한글 단어 추출용 tokenizer
def simple_korean_tokenizer(text):
    return re.findall(r'[가-힣]{2,}', text)  # 2글자 이상 한글만 추출

def get_tfidf_vectorizer(docs):
    vectorizer = TfidfVectorizer(tokenizer=simple_korean_tokenizer, max_features=100)
    tfidf_matrix = vectorizer.fit_transform(docs)
    return vectorizer, tfidf_matrix
