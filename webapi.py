# import chromedriver_binary
import time
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# This code is made for downloading plenty of anime images from tsudora.com

# Chrome driver settings
# If you use another chrome version, you have to download matching chrome driver
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver.exe')

image_dir = './anime_images/'
os.makedirs(image_dir, exist_ok=True)

# tsudora pages
start = 6000
finish = 10543

numbers = list(range(start, finish))
urls = ['https://tsundora.com/page/{}'.format(num) for num in numbers]

count = 95998  # Now image number
for search_url in urls:
    driver.get(search_url)
    time.sleep(3)

    links = driver.find_elements_by_tag_name('img')
    srcs = []
    for link in links:
        src = link.get_attribute('src')
        srcs.append(src)
        
    print()
    print(srcs[0])

    for url in srcs:
        if url[-3:] in ['jpg', 'png']:
            urllib.request.urlretrieve(url, image_dir + '{}.png'.format(count))
            count += 1

    time.sleep(3)

print()
print('---next count---')
print(count)
print()
driver.quit()