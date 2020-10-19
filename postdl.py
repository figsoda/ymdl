#!/bin/python3

import os, re, subprocess, sys

def na(s): return None if s == "NA" else s

name = sys.argv[1]

m = re.fullmatch(r"(.+)@(.+)@(.+)@(.+)@(.+)@(.+)\.m4a", name)
tags = subprocess.run(["AtomicParsley", name, "-t"], check = True, stdout = subprocess.PIPE, text = True).stdout

track = na(m[1]) or m[2]

try:
    artist = next(re.finditer(r"Associated  Performer: (.*)", tags))[1]
except StopIteration:
    artist = na(m[3]) or na(m[4]) or na(m[5]) or m[6]

cmd = ["AtomicParsley", name, "-W", "--artist", artist]
if 'Atom "©alb" contains: ' not in tags: cmd += ["--album", track]
subprocess.run(cmd, check = True)
os.rename(name, f"{track} - {artist}.m4a")
