import os
import urllib
import hashlib
import time
import random

def list_folder(relative_path):
    absolute_path = os.path.abspath(relative_path)
    if not os.path.isdir(absolute_path):
        return []

    files = []
    for f in os.listdir(absolute_path):
        if os.path.isfile( os.path.join( absolute_path, f)):
            files.append(f)

    return files

def download_ad(url, target_path):
    absolute_path = os.path.abspath(target_path)
    if not os.path.isdir(absolute_path):
        return False

    target_path = os.path.join(absolute_path, hashlib.sha1(url).hexdigest() + '.html')

    try:
        target = open(target_path, 'w')
        target.writelines(urllib.urlopen(url).readlines())
        target.close()
    except:
        return False

    return True


def serve_file(url, target_path):
    absolute_path = os.path.abspath(target_path)
    if not os.path.isdir(absolute_path):
        return False

    target_path = os.path.join(absolute_path, url)

    if not os.path.exists(target_path):
        return False

    target = open(target_path, 'r')
    if not target:
        return False

    data = ''.join(target.readlines())
    target.close()

    return data



ad_sleep = 10
def check_ad(url):
    time.sleep(ad_sleep)
    result = random.randint(0, 100)
    if result % 10 == 0:
        return False
    return True