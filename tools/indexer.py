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

        print subtitle_info["title"]

