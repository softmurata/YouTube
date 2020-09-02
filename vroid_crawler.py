import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver.exe')

root_url = 'https://hub.vroid.com'

url = 'https://hub.vroid.com/models?is_other_users_available=1&is_downloadable=1'

driver.get(url)
time.sleep(3)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

start = time.time()
finish = 600

target_year = 2020
target_month = 6
target_day = 6

answer_urls = []
answer_times = []

write_text_file = 'vrm.txt'

while True:
    
    links = driver.find_elements_by_tag_name('a')
    
    target_urls = []
    target_dates = []
    
    for link in links:
        href = link.get_attribute('href')
        print(href)
        contents = href.split('/')
                
        if 'characters' not in contents:
            continue
        
            
        target_urls.append(href)
        
    for target_url in target_urls:
        driver.get(target_url)
        time.sleep(3)
                        
        times = driver.find_elements_by_tag_name('time')
        # <time datetime="2020-08-05T01:42:01.000Z">2020年8月5日 10:42</time>
        date_time = times[0].get_attribute('datetime')
        
        year, month, day = date_time.split('-')
        day, postfix = day.split('T')
        
        if int(month) >= target_month and int(day) >= target_day:
            continue
            
        
        target_dates.append(date_time)
        
        # time.sleep(10)
    
        
        
    answer_urls.extend(target_urls)
    answer_times.extend(target_dates)
    
    print(answer_times)
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    
    current = time.time()
    search_time = current - start
    print('search time:', search_time)
    if search_time >= finish:
        break
        
    last_height = new_height


# save txt file
with open(write_text_file, 'w') as f:
    for path in answer_urls:
        content = '{}\n'.format(path)
        f.write(content)

