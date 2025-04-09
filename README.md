# 🔍 KeywordVisualizerApp

**Streamlit 기반 뉴스 키워드 분석 대시보드**  
자연어처리 기술을 활용해 실시간 뉴스 또는 CSV 데이터를 분석하고  
빈도 그래프와 워드클라우드로 시각화하는 프로젝트입니다.

---

## 📌 주요 기능

- 🔎 **뉴스 검색 기능**: 네이버 뉴스에서 키워드 기반 기사 수집
- 📊 **TF-IDF 분석**: 단어 중요도 추출
- ☁️ **워드클라우드**: 시각화된 키워드 강조
- 📁 **CSV 업로드 지원**: 외부 텍스트 데이터 분석 가능

---

## ⚙️ 사용 기술

| 구분         | 사용 도구                         |
|--------------|------------------------------------|
| 웹 프레임워크 | Streamlit                          |
| 데이터 분석   | Pandas, scikit-learn, konlpy       |
| 시각화       | Matplotlib, Wordcloud              |
| 크롤링       | requests, BeautifulSoup (내장 모듈) |
| 배포         | Streamlit Cloud, GitHub            |

---

## 🚀 실행 방법

```bash
# 필수 라이브러리 설치
pip install -r requirements.txt

# 웹 앱 실행
streamlit run KeywordVisualizerSTApp1.py
```

---

## 📁 프로젝트 구조

```
KeywordVisualizerApp/
│
├── lib/
│   ├── myTextMining1.py
│   ├── NaverNewsCrawler1.py
│   └── STVisualizer1.py
│
├── KeywordVisualizerSTApp1.py         # 메인 앱
├── KeywordVisualizerConsoleApp1.py    # 콘솔 실행용
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 개발자 정보

- 이름: 우도연
- 학번: 2403110278
- GitHub: [woodoyeon](https://github.com/woodoyeon)
