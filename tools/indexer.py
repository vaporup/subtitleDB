#!/usr/bin/env python

import os
import yaml

uuid_prefix_foldernames = os.listdir("subtitles")

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
          
          # TODO if more than 1 subtitle  https://stackoverflow.com/questions/6987285/python-find-the-item-with-maximum-occurrences-in-a-list

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
                directory = "/tmp/index/by-hash-filesize/" + match["hash"][0:2] + "/" + match["hash"][2:-1] + "-" + match["filesize"]
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
  



