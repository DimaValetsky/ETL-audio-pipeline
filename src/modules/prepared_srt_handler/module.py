from src.modules.labels_generator.module import generate_labels
from src.modules.media_extractor.module import slice_via_pydub
from src.modules.pathes_generator.module import *


def workwithprepared(output_path, prepared_dirs):
    for srt_dir in prepared_dirs:
        generate_labels(output_path, srt_dir)

        wavfile = get_wavfile(output_path, srt_dir)
        labelfile = get_labelfile(output_path, srt_dir)
        sliced_dir = get_sliced_dir(output_path, srt_dir)

        if not os.path.isdir(sliced_dir):
            os.mkdir(sliced_dir)
        dirs = sliced_dir + srt_dir + '.wav'

        try:
            sliced_audio = slice_via_pydub(dirs, wavfile, labelfile)
        except:
            print(f'something wrong with wav {wavfile} or label {labelfile} in {dirs}')
            continue
        print(sliced_audio)
