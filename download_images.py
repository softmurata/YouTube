import os
import time
import traceback

import flickrapi
from urllib.request import urlretrieve

import sys

# keyword type
# building, people, animal, nature

# flicker api
flicker_api_key = "1ede798f6d6eddb61dc93c53c927ef93"
secret_key = "4d0dd6451e0c9edb"

keyword = sys.argv[1]

if __name__ == '__main__':
 
    flicker = flickrapi.FlickrAPI(flicker_api_key, secret_key, format='parsed-json')
    response = flicker.photos.search(
        text=keyword,
        per_page=2000,
        media='photos',
        sort='relevance',
        safe_search=1,
        extras='url_q,license'
    )
    photos = response['photos']
 
    if not os.path.exists('./image-data/' + keyword):
            os.makedirs('./image-data/' + keyword)
 
    for idx, photo in enumerate(photos['photo']):
        print()
        print('---photo number {}---'.format(idx))
        url_q = photo['url_q']
        filepath = './image-data/' + keyword + '/' + photo['id'] + '.jpg'
        urlretrieve(url_q, filepath)
        time.sleep(1)
