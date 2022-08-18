import os


def get_wav_path(prepared_srt_path, srt_file):
    return os.path.join(prepared_srt_path + srt_file[:-4], srt_file[:-4] + '.wav')


def get_wavfile(prepared_srt_path, srt_dir):
    return os.path.join(prepared_srt_path + srt_dir, srt_dir + '.wav')


def get_labelfile(prepared_srt_path, srt_dir):
    return os.path.join(prepared_srt_path + srt_dir, srt_dir + '_label.txt')


def get_sliced_dir(prepared_srt_path, srt_dir):
    return os.path.join(prepared_srt_path + srt_dir, 'sliced/')


def get_voc_path(prepared_srt_path, voc_file):
    return os.path.join(prepared_srt_path + voc_file, voc_file + '.srt')
