import os
import urllib
import hashlib
import time
import random

def file_exists(url, target_path):
    absolute_path = os.path.abspath(target_path)
    if not os.path.isdir(absolute_path):
        return False
    target_path = os.path.join(absolute_path, url)
    if not os.path.exists(target_path):
        return False
    return True

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
    target_path = os.path.join(os.path.abspath(target_path), url)
    target = open(target_path, 'r')
    if not target:
        return False
    data = ''.join(target.readlines())
    target.close()
    return data



ad_sleep = 2
def check_ad(checker, path):
    if checker != 'now':
        time.sleep(ad_sleep)

    if checker == 'true':
        return True

    if checker == 'false':
        return False

    result = random.randint(0, 99)
    if result % 3 == 0:
        return False
    return True