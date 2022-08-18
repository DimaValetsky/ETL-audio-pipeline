import os
from os import listdir
from os.path import isfile, join
from argparse import ArgumentParser
from src.modules.raw_srt_handler.module import workwithraw
from src.modules.prepared_srt_handler.module import workwithprepared


parser = ArgumentParser()
parser.add_argument("-s", "--srt_path", type=str)
parser.add_argument("-a", "--audio_path", type=str)
parser.add_argument("-o", "--output_path", type=str)
args = parser.parse_args()

srt_path = args.srt_path
audio_path = args.audio_path
output_path = args.output_path

if not os.path.exists(output_path):
    os.mkdir(output_path)

raw_srts = [f for f in listdir(srt_path) if isfile(join(srt_path, f))]

workwithraw(srt_path, audio_path, output_path, raw_srts)

prepared_dirs = [f for f in listdir(output_path) if os.path.isdir(join(output_path, f))]

workwithprepared(output_path, prepared_dirs)
