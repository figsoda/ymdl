#!/bin/sh

youtube-dl --format bestaudio/m4a/best\
    -x --audio-format m4a --audio-quality 0\
    --add-metadata --embed-thumbnail\
    -o "%(track)s@%(title)s@%(artist)s@%(creator)s@%(channel)s@%(uploader)s.%(ext)s"\
    --exec "python3 postdl.py {}"\
    "$@"
