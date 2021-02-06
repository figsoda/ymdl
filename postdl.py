#!/usr/bin/env python3

import os, re, sys, taglib

def na(s): return None if s == "NA" else s

name = sys.argv[1]

song = taglib.File(name)
m = re.fullmatch(r"(.+)@(.+)@(.+)@(.+)@(.+)@(.+)\.flac", name)

if not song.tags.get("ALBUM"): song.tags["ALBUM"] = [na(m[1]) or m[2]]

if not song.tags.get("ARTIST"):
    try:
        artist = next(
            re.finditer(r"Associated  Performer: (.*)", song.tags["DESCRIPTION"][0])
        )[1]
    except (IndexError, KeyError, StopIteration):
        artist = na(m[3]) or na(m[4]) or na(m[5]) or m[6]
    song.tags["ARTIST"] = artist

song.save()
os.rename(name, f"{song.tags['ALBUM'][0]} - {song.tags['ARTIST'][0]}.flac")
