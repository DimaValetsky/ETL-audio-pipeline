import os
from src.modules.voc_detector.module import detect_voc_cases
from src.modules.media_converter.module import convert_mp4_to_wav
from src.modules.pathes_generator.module import get_wav_path


def workwithraw(srt_path, audio_path, output_path, raw_srts):
    for srt_file in raw_srts:

        with open(srt_path + srt_file, 'r') as f:
            lines = f.readlines()

        if not os.path.exists(output_path + srt_file[:-4]):
            os.mkdir(output_path + srt_file[:-4])

        with open(os.path.join(output_path + srt_file[:-4], srt_file), 'w') as f:
            detect_voc_cases(f, lines)

        mp4_path = audio_path + srt_file[:-4] + '.mp4'
        wav_path = get_wav_path(output_path, srt_file)

        try:
            convert_mp4_to_wav(mp4_path, wav_path)
        except:
            print(f'something wrong with mp4 {mp4_path} and wav_path {wav_path}')
            continue
