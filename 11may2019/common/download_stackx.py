#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common import download_utils


def download_stackx_resources(force=False):
    download_utils.sequential_downloader(
        "week1",
        [
            "train.tsv",
            "validation.tsv",
            "test.tsv",
            "text_prepare_tests.tsv",
        ],
        "data/stackx",
        force=force
        )

download_stackx_resources()
