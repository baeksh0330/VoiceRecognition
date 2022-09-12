import requests, json
url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
key = '[REST API KEY]'
headers = {
    "Content-Type": "application/octet-stream",
    "Transfer-Encoding": "chunked",
    "Authorization" : "KakaoAK" + key,
}
with open('heyKakao.wav','rb') as fp: # FileNotFoundError -> 파일 다운받아줘야함
    audio = fp.read()

res = requests.post(url, headers=headers, data=audio)
print(res.text)