import os
import re
from pathlib import Path
import requests

import urllib3
urllib3.disable_warnings()

from linkoscopy.link_validator import test_url


result={}
regex = re.compile( r"\[(.+?)\]\((https?:\/\/.+?)\)" )

for root, dirs, files in os.walk(path):
    for f in files:
        if f.endswith('.md'):
            mdFile = open(os.path.join(root,f), "r", encoding="utf-8")
            entireFile = mdFile.read()
            for title,url in regex.findall(entireFile):
                if "youtu.be" in url:
                    continue
                if "youtube.com" in url:
                    continue
                status_code = test_url(url) #requests.head(url, verify=False)
                if status_code not in result:
                    result[status_code]=[]
                result[status_code].append(url)
                if status_code !=200:
                    print(status_code, url)
