#!/usr/bin/env python

import fnmatch
import os

for root, dirnames, filenames in os.walk('../subtitles'):
    for filename in fnmatch.filter(filenames, 'meta.yml'):
        #print os.path.join(root, filename)
        print root
