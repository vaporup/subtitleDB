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
          if "matches" in yaml_content:
            for match in yaml_content["matches"]:
                #print match["hash"][0:2] + "/" + match["hash"][2:-1] + "-" + match["filesize"], yaml_content["language"], yaml_content["title"], yaml_path
                #print match["hash"][0:2] + "/" + match["hash"][2:-1], root.replace("subtitles/",""), yaml_content["title"]
                #print match["hash"][0:2] + "/" + match["hash"][2:-1] + "-" + match["filesize"] + "-" + yaml_content["language"] + "-" + root.replace("subtitles/","")
                directory = "/tmp/index/by-hash-filesize/" + match["hash"][0:2] + "/" + match["hash"][2:-1] + "-" + match["filesize"]
                sub = root.replace("subtitles/","")
                if not os.path.exists(directory):
                  os.makedirs(directory)

                filename = directory + "/" + yaml_content["language"]

                if os.path.exists(filename):
                  with open(filename, "r+") as f:
                    for line in f:
                      if sub in line:
                        break
                    else: # not found, we are at the eof
                      f.write(sub) # append missing data
                else:
                  f = open(filename, "w")
                  f.write(sub + '\n')
                  f.close()

          if "imdb_id" in yaml_content:
            directory = "/tmp/index/by-imdb/" + yaml_content["imdb_id"]
            sub = root.replace("subtitles/","")

            if not os.path.exists(directory):
              os.makedirs(directory)

            filename = directory + "/" + yaml_content["language"]

            if os.path.exists(filename):
              with open(filename, "r+") as f:
                for line in f:
                  if sub in line:
                    break
                else: # not found, we are at the eof
                  f.write(sub) # append missing data
            else:
              f = open(filename, "w")
              f.write(sub + '\n')
              f.close()

          if "tmdb_id" in yaml_content:
            directory = "/tmp/index/by-tmdb/" + yaml_content["tmdb_id"]
            sub = root.replace("subtitles/","")

            if not os.path.exists(directory):
              os.makedirs(directory)

            filename = directory + "/" + yaml_content["language"]

            if os.path.exists(filename):
              with open(filename, "r+") as f:
                for line in f:
                  if sub in line:
                    break
                else: # not found, we are at the eof
                  f.write(sub) # append missing data
            else:
              f = open(filename, "w")
              f.write(sub + '\n')
              f.close()
