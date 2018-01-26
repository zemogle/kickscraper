# Kickscraper
Sorry this project is so rough!

## Requirements
You'll need:
- Pimoroni [Unicorn HAT HD](https://shop.pimoroni.com/products/unicorn-hat-hd)
- [Unicorn HAT HD python library](https://github.com/pimoroni/unicorn-hat-hd)

You'll also need a `settings.py` file which has the following format:

```
import logging

PROJECT_ID = 'XXXX' # Numbers
PROJECT_NAME = 'YYY-YYY' # the name of your project, lower case with spaces replaced with 'u'
JSON_FILE = 'data.json' # Where the data is stored so we know if we have new pledges
PROJECT_DIR = '/home/pi/kickscraper/'
LOG_LEVEL=logging.DEBUG
```
