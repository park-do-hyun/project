from gtts import gTTS
import os, re
os.chdir(r'C:\Users\mit\Desktop\project')
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

#명언 사이트
url = 'http://quotes.toscrape.com'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

#빈 리스트 생성
i_list = []
j_list = []

#명언 가져오기
for i in soup.select('div.col-md-8 > div.quote > span.text') :
  i_list.append(i.text.strip())

#위인 가져오기
for j in soup.select('div.col-md-8 > div.quote > span > small.author') :
  j_list.append(j.text)

#명언 리스트와 위인 리스트의 길이를 비교하여 길이가 같으면 파일 생성
if len(i_list) == len(j_list) :
  f = open('link.txt', 'w', encoding='UTF-8')
  for a in range(len(i_list)):
    data = i_list[a] + 'by' + j_list[a] + '\n'
    f.write(data)
  f.close()
else:
  print('Error')

# txt 파일을 qwe 안에 저장
txtFile = 'link.txt'
with open(txtFile, 'rt', encoding='UTF-8') as f:
  qwe = f.read()

tts = gTTS(text= qwe, lang='en')
tts.save(r'C:\Users\mit\Desktop\project\a.mp3')
