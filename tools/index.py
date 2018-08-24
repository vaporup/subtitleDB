#!/usr/bin/env python

import fnmatch
import os
import yaml

for root, dirnames, filenames in os.walk('subtitles'):
    for filename in fnmatch.filter(filenames, 'meta.yml'):
        if "template" in root:
          continue
        else:
          yaml_file = os.path.join(root, filename)
          yaml_path = os.path.join(root, "")

          #print "Opening: %s" % (yaml_file)

          yaml_data = open(yaml_file).read()
          yaml_content = yaml.load(yaml_data)

          #print yaml.safe_dump(yaml_content, allow_unicode=True, encoding="utf-8", default_flow_style=False)
          if "alternative_titles" in yaml_content:
            for alternative_title in yaml_content["alternative_titles"]:
              print alternative_title
