from bs4 import BeautifulSoup
import requests

print("데이터 수집 시작")
target = "https://music.bugs.co.kr/chart"
raw = requests.get(target)

# print(raw.text)
html = BeautifulSoup(raw.text, "html.parser")
print(type(html))
title_list_tag = html.find_all("p", {"class":"title"} ) # get artist
artist_list_tag = html.find_all("p", {"class":"artist"} ) # get artist
# print(artist_list_tag)
title_list = list()
artist_list = list()
for i in title_list_tag:
    tmp = i.text
    tmp = tmp.replace("\n","",100)
    title_list.append(tmp)


for idx,v in enumerate(artist_list_tag):
    tmp = v.text
    tmp = tmp.replace(chr(13), "", 10)
    tmp = tmp.replace("\n", "", 100)
    artist_list.append(tmp)
#
for idx,val in enumerate(title_list):
    print("{0}위 / 제목 : {1} / 가수 : {2}".format(idx+1,val,artist_list[idx]))



# artist = list()
# cnt = 1
# for i in artist_list_tag:
#     # print(i.get_text())
#     tmp = i.get_text()
#     tmp = tmp[1:]
#     rank = str(cnt) +". " + tmp
#     cnt += 1
#     artist.append(rank)
#
# for i in artist:
#     print(i)