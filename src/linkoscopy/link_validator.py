import os
import re
from pathlib import Path
import requests
import logging


import urllib3
urllib3.disable_warnings()

from chrome_headers2 import headers
session = requests.Session()
session.headers.update(headers)


def test_url(url):
    try:
        resp = session.head(url, verify=False)
        if resp.status_code != 200:
            resp = session.get(url, verify=False)
    except Exception as e:
        print(e)
        return 0
    # print(resp.status_code, url)
    return resp.status_code


if __name__ == "__main__":
    for url in E403:  # "http://localhost:1234"]:
        # resp = session.get(url, verify=False)
        resp = test_url(url)
        print(resp, url)
