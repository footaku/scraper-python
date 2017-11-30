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
    res = requests.get('http://www.yahoo.co.jp/', timeout=10, verify=False)
    content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
    info_logger.info('page title is "{}".'.format(get_page_title(res, content_type_encoding)))
    return res.status_code


def get_page_title(res, encoding):
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding=encoding)
    return soup.select("title")[0].string
