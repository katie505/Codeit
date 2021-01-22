#!/usr/bin/env python
# coding: utf-8

# In[1]:


#여러 줄의 텍스트를 """와 """ 사이에 두면, 하나의 문자열로 인식
html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""


# In[3]:


#1. Beautiful Soup 타입 만들기
from bs4 import BeautifulSoup

#BeautifulSoup 타입으로 변환
#HTML을 파싱한다는 의미로 'html.parser'
soup = BeautifulSoup(html_code, 'html.parser')

#type 출력
print(type(soup))


# In[5]:


#2. 특정 태그 선택하기
# 모든 <li> 태그 선택
li_tags = soup.select('li')

# 결과 출력
print(li_tags)
#첫 번째 요소 출력하기
print(li_tags[0])


# In[7]:


#3. 태그에서 문자열 추출하기
print(li_tags[0].text)

beverage_names = []
for li in li_tags:
    beverage_names.append(li.text)
    
print(beverage_names)


# In[11]:


#4. 태그에서 속성 값 추출하기
#<img> 태그의 src 속성에는 일반적으로 이미지 주소가 저장되어 있음

# 모든 <img> 태그 선택하기
img_tags = soup.select('img')
print(img_tags)
print(img_tags[0])

#태그에 ['속성 이름']을 붙여주면 해당 속성의 값 가져올 수 있음
print(img_tags[0]['src']) #이미지 주소만 추출

img_srcs = []
for img in img_tags:
    img_srcs.append(img['src'])

print(img_srcs)


# In[12]:


#실제 웹사이트의 response를 받아서 파싱해보기


# In[14]:


import requests
response = requests.get('https://workey.codeit.kr/music/index')

print(response.text)


# In[15]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


# In[20]:


#태그 r골라내기
#인기 아티스트 10명의 이름 선택
li_tags = soup.select('.popular__order li')

popular_artists = []
for li in li_tags:
    popular_artists.append(li.text.strip())
    
print(popular_artists)


# In[21]:


#필요한 페이지만 가져오기


# In[23]:


import time
import requests
from bs4 import BeautifulSoup

#연속으로 페이지를 가져오려고 하면 사이트에서 차단을 하는 경우가 있는데, 한 페이지를 가져온 뒤 3초간 쉬었다가 다음 페이지를 가져오도록
#time.sleep(3) 이용
pages = []
page_num = 1

while True:
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))
    
    soup = BeautifulSoup(response.text, 'html.parser')
    if len(soup.select('.csrch_tip')) == 0:
        pages.append(soup)
        print(str(page_num) + '번째 페이지 가져오기 완료')
        page_num += 1
        time.sleep(3)
    else:
        break


# In[25]:


response = requests.get('https://workey.codeit.kr/ratings/index').text
print(response)


# In[26]:


#웹 페이지를 Dataframe으로


# In[ ]:


import time
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)

        # 여기에 각 상품의 정보를 하나의 레코드로 저장하는 코드 추가
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get('src'))
            records.append(record)
    else:
        break


# In[ ]:


print(len(records))
print(records)


# In[ ]:


import pandas as pd

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()

