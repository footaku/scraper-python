import logging
import requests
import urllib3
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning


urllib3.disable_warnings(InsecureRequestWarning)

stream_handler = logging.StreamHandler()
info_logger = logging.getLogger()
info_logger.setLevel(logging.INFO)
info_logger.addHandler(stream_handler)


def handler(event, context):
    res = requests.get('https://google.co.jp/', timeout=10)

    content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)

    info_logger.info('page title is "{}".'.format(get_page_title(soup)))
    info_logger.info('antenna for everyone is "{}".'.format(get_footer_bar(soup)))
    return res.status_code


def get_page_title(soup):
    return soup.title.string


def get_footer_bar(soup):
    return soup.find('a', id='gb_70').string


if __name__ == '__main__':
    handler(None, None)
