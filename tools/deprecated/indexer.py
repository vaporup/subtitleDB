#!/usr/bin/env python

import os
import sys
import yaml

toolbar_width = 10

percent_10  = True
percent_20  = True
percent_30  = True
percent_40  = True
percent_50  = True
percent_60  = True
percent_70  = True
percent_80  = True
percent_90  = True
percent_100 = True

uuid_prefix_foldernames = os.listdir("subtitles")

alle = len(uuid_prefix_foldernames)
count = float(alle)

# setup toolbar
sys.stdout.write("\nIndexing subtitles ")
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for uuid_prefix_foldername in uuid_prefix_foldernames:

    if uuid_prefix_foldername == "template":
      continue

    uuid_prefix_folder = os.path.join("subtitles", uuid_prefix_foldername)

    if os.path.isdir(uuid_prefix_folder):

      uuid_foldernames = os.listdir(uuid_prefix_folder)

      for uuid_foldername in uuid_foldernames:

        uuid_folder = os.path.join(uuid_prefix_folder, uuid_foldername)

        if os.path.isdir(uuid_folder):

          meta_data_file = os.path.join(uuid_folder, "meta.yml")
          meta_data      = open(meta_data_file).read()
          subtitle_info  = yaml.load(meta_data)

          subtitle_info["subtitles"] = []

          subtitle_dirs = [name for name in os.listdir(uuid_folder) if os.path.isdir( uuid_folder + "/" + name)]

          for subtitle_dir in subtitle_dirs:

            subtitle_meta_data_file = os.path.join(uuid_folder, subtitle_dir, "subtitle.yml")
            subtitle_meta_data      = open(subtitle_meta_data_file).read()
            subtitle_data           = yaml.load(subtitle_meta_data)

            subtitle_info["subtitles"].append(subtitle_data)

          num_subs = len(subtitle_info["subtitles"])

          if num_subs == 1:
            language = subtitle_info["subtitles"][0]["language"]

          if num_subs > 1:
            # https://stackoverflow.com/questions/6987285/python-find-the-item-with-maximum-occurrences-in-a-list
            languages = []
            for sub in subtitle_info["subtitles"]:
              languages.append(sub["language"])
            language = max(languages,key=languages.count)

          for id_prov in ["imdb_id", "tmdb_id"]:

            if id_prov in subtitle_info:
              #print subtitle_info["imdb_id"] + "-" + language + "-" + str(num_subs) + "-" + os.path.join(uuid_prefix_foldername , uuid_foldername)
              sub = os.path.join(uuid_prefix_foldername , uuid_foldername)
              directory = "/tmp/index/by-" + id_prov.replace("_id","") + "/" + subtitle_info[id_prov]
              if not os.path.exists(directory):
                  os.makedirs(directory)

              filename = directory + "/" + language + "-" + str(num_subs)

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

          for subtitle in subtitle_info["subtitles"]:

            if "matches" in subtitle:
              for match in subtitle["matches"]:
                directory = "/tmp/index/by-hash-filesize/" + match["hash"][0:2] + "/" + match["hash"][2:] + "-" + match["filesize"]
                sub = os.path.join(uuid_prefix_foldername , uuid_foldername)
                if not os.path.exists(directory):
                  os.makedirs(directory)

                filename = directory + "/" + language

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
  


    count = count -1
    percent = 100 - count / alle * 100

    if percent > 10:
      if percent_10:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_10 = False
    if percent > 20:
      if percent_20:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_20 = False
    if percent > 30:
      if percent_30:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_30 = False
    if percent > 40:
      if percent_40:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_40 = False
    if percent > 50:
      if percent_50:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_50 = False
    if percent > 60:
      if percent_60:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_60 = False
    if percent > 70:
      if percent_70:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_70 = False
    if percent > 80:
      if percent_80:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_80 = False
    if percent > 90:
      if percent_90:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_90 = False
    if percent > 95:
      if percent_100:
        sys.stdout.write(".")
        sys.stdout.flush()
        percent_100 = False

sys.stdout.write("\n")
sys.stdout.write("\n")

