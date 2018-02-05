import requests
from bs4 import BeautifulSoup
import settings
import json
import six
import atexit
import time
import logging
import os
from math import ceil

logging.basicConfig(filename='/home/pi/kick.log', format='%(levelname)s:%(message)s', level=settings.LOG_LEVEL)

try:
    from display_inky import display_data, display_happy
except:
    from display_demo import display_data, display_happy

def load_data():
    try:
        with open(settings.JSON_FILE, 'r') as f:
            stats = json.load(f)
    except:
        stats = {'pledged':0, 'percent':0, 'backers':0}
    return stats

def output_data(data):
    with open(settings.JSON_FILE, 'w') as f:
        f.write(json.dumps(data, indent=2))
    return

def scrape():
    url = "https://www.kickstarter.com/projects/{}/{}/stats.json?v=1".format(settings.PROJECT_ID, settings.PROJECT_NAME)
    try:
        logging.debug('GET to Kickstarter')
        resp = requests.get(url, timeout=10)
    except:
        return False
    if resp.status_code in [200,201]:
        logging.debug('Response recieved')
        content = resp.json()
    else:
        logging.warning('No Response recieved')
        return False
    pledged = content['project']['pledged']
    percent = ceil(float(pledged)/settings.TOTAL)
    backers = content['project']['backers_count']
    logging.debug('Finished scraping')
    return {'pledged':pledged, 'percent':percent, 'backers':backers}

# def tear_down():
#     logging.warning("Kickscraper stopped")
#     unicornhathd.off()
#     return
#
# atexit.register(tear_down)

if __name__ == '__main__':
    logging.debug('Starting up')
    # display_happy(settings.PROJECT_DIR+'ada_title.png')
    old_data = load_data()
    display_data(old_data)
    data = scrape()
    if data and old_data['pledged'] != data['pledged']:
        logging.debug('New pledges - {}!'.format(data['pledged']))
        output_data(data)
        display_happy(settings.PROJECT_DIR+'ada_title.png')
    logging.debug('Pledge graphic')
    display_data(data)
