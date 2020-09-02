import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


vrm_txt = 'vrm.txt'

with open(vrm_txt, 'rb') as f:
    u = f.readlines()
    

url_pathes = [ui[:-2].decode() for ui in u]


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver.exe')
driver.get('https://hub.vroid.com/models?is_other_users_available=1&is_downloadable=1')

# url_pathes = ['https://hub.vroid.com/characters/9186847271079065710/models/7067380158973065589',
#            'https://hub.vroid.com/characters/102967867779054694/models/3951530788401416123'] 


# get datetime
vrm_time_txt = 'vrm_time.txt'

dates = []

for url_path in url_pathes:
    """
    urls = url_path.split('/')[3:]
    url = ''
    for u in urls:
        url += '/{}'.format(u)
    print('url path:', url)
    driver.get(url)
    """
    driver.get(url_path)
    time.sleep(3)
                
    times = driver.find_elements_by_tag_name('time')
    # <time datetime="2020-08-05T01:42:01.000Z">2020年8月5日 10:42</time>
    date_time = times[0].get_attribute('datetime')
    dates.append(date_time)

driver.quit()

with open(vrm_time_txt, 'wb') as f:
    for url_path, date_time in zip(url_pathes, dates):
        content = '{} {}\n'.format(date_time, url_path)
        f.write(content)