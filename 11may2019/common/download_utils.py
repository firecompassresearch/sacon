#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from smart_open import open
import shutil

REPOSITORY_PATH = "https://github.com/hse-aml/natural-language-processing"

def download_file(url, file_path):
    try:
        print("Downloading %s to %s.." % (url, file_path))
        with open(url, encoding='utf8') as fin:
            with open(file_path, 'w', encoding='utf8') as fout:
                shutil.copyfileobj(fin, fout)
    except Exception as ex:
        print(ex)
        print("Download failed")


def download_from_github(version, fn, target_dir, force=False):
    url = REPOSITORY_PATH + "/releases/download/{0}/{1}".format(version, fn)
    file_path = os.path.join(target_dir, fn)
    if os.path.exists(file_path) and not force:
        print("File {} is already downloaded.".format(file_path))
        return
    download_file(url, file_path)


def sequential_downloader(version, fns, target_dir, force=False):
    os.makedirs(target_dir, exist_ok=True)
    for fn in fns:
        download_from_github(version, fn, target_dir, force=force)
