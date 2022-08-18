# Vocative Case Labeling Service

A service that analyzes subtitle files (srt format), finding replicas containing vocative cases, moving this cases in txt-file with timings and extracts the corresponding audio fragments into separate files.

## Installation
- python -m pip install -r requirements.txt
- sudo apt install ffmpeg (if you use Linux)

## Basic scripts
main.py -s "srt file path" -a "mp4 file path" -o "output path"
