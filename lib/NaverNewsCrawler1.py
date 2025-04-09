import urllib.request
import urllib.parse
import json

# 네이버 뉴스 API 호출 함수
def search_naver_news(keyword, display=30):
    client_id = "CL7oQtFIVnlIq2hW5_CN"
    client_secret = "um9wyOZHwb"

    enc_query = urllib.parse.quote(keyword)
    url = f"https://openapi.naver.com/v1/search/news?query={enc_query}&display={display}&start=1"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            result = json.loads(response.read().decode('utf-8'))
            return [item['title'] + ' ' + item['description'] for item in result.get('items', [])]
        else:
            print("오류 코드:", response.getcode())
    except Exception as e:
        print("예외 발생:", e)
    return []