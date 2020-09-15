import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# DOMAIN = 'https://www.miniclip.com'
# URL = DOMAIN+'/games/page/en/downloadable-games'


# pageTree = requests.get(URL)
# soup = BeautifulSoup(pageTree.content, 'lxml')
# ul = soup.find('ul', attrs={'class': 'downloads'})
# li = ul.find_all('li')
# download_links = ul.find_all('a', attrs={'class': 'button positive small greedy'})
# count = 0
# for link in download_links:
#     count += 1
#     full_url = DOMAIN+link.get('href')
#     urllib.request.urlretrieve(full_url, '../bin/miniclip/game_'+str(count))
#     print(count, full_url)





# DOMAIN = 'https://www.gametop.com'
# URL = DOMAIN+'/category/mini-games.html'


# pageTree = requests.get(URL)
# soup = BeautifulSoup(pageTree.content, 'lxml')
# # print('soup', soup)
# divs = soup.find_all('div', attrs={'class': 'row pb-3'})
# # print('divs', divs)
# count = 0
# for div in divs:
# # if True:
#     download_links = div.find_all('a')
#     # print('download_links', download_links)
#     for link in download_links:
#         count += 1
#         full_url = DOMAIN+link.get('href')+'download.html'
#         print(count, link.get('title'), full_url)
#         filename = link.get('title').replace(' ','-').replace(':', '-')
#         if not os.path.exists('../bin/gametop/'+filename):
#             urllib.request.urlretrieve(full_url, '../bin/gametop/'+filename)






# DOMAIN = 'https://www.game-remakes.com'
# count = 0
# for page in range(3, 54):
#     URL = DOMAIN+'/?cat=123&p='+str(page)

#     pageTree = requests.get(URL)
#     soup = BeautifulSoup(pageTree.content, 'lxml')
#     tbls = soup.find_all('table', attrs={'class': 'categoryGameCard'})
#     for tbl in tbls:
#         download_links = tbl.find_all('a', attrs={'class': 'categoryGameLinks'})
#         # print('download_links', download_links)
#         link = download_links[0]
        
#         count += 1
#         full_url = DOMAIN+link.get('href')
#         title = tbl.find('h2').text.split('. ')[1].strip()
#         print(count, 'page', page, title, full_url)

#         filename = title.replace(' ','-').replace(':', '-')
#         if not os.path.exists('../bin/game-remakes/'+filename):
#             urllib.request.urlretrieve(full_url, '../bin/game-remakes/'+filename)

