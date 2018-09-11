#!/usr/bin/env python

import sys
import os
import struct
import yaml

def hashFile(name): 
      try: 
                 
                longlongformat = '<q'  # little-endian long long
                bytesize = struct.calcsize(longlongformat) 
                    
                f = open(name, "rb") 
                    
                filesize = os.path.getsize(name) 
                hash = filesize 
                    
                if filesize < 65536 * 2: 
                       return "SizeError" 
                 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlongformat, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number  
                         
    
                f.seek(max(0,filesize-65536),0) 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlongformat, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF 
                 
                f.close() 
                returnedhash =  "%016x" % hash 
                return returnedhash 
    
      except(IOError): 
                return "IOError"


filename = sys.argv[1]

filehash = hashFile(filename)
filesize = str(os.path.getsize(filename))

filepath = "/home/swick/repos/vaporup/subtitleDB/index/by-hash-filesize/" + filehash[0:2] + '/' + filehash[2:] + "-" + filesize + "/en"

if os.path.isfile(filepath):
  found_subs = open(filepath).readlines()
  print "\nFound %i subs\n" % len(found_subs)
  for found in found_subs:
    print "Subtitle ID: %s" % found

    meta = "/home/swick/repos/vaporup/subtitleDB/subtitles/" + found.strip("\n") + "/meta.yml"
    sub = "/home/swick/repos/vaporup/subtitleDB/subtitles/" + found.strip("\n") + "/1/subtitle.yml"

    meta_data = yaml.load(open(meta))
    sub_data = yaml.load(open(sub))
    print meta_data, sub_data
    print

