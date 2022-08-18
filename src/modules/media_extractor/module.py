import os
from pydub import AudioSegment


def reformat_boundaries(raw_boundaries):
    result = []
    for rbs in raw_boundaries:
        start = int(float(rbs[0])*1000)
        finish = int(float(rbs[1])*1000)
        result.append({'start': start, 'finish': finish})
    return result


def get_boundaries(labelfile):
    with open(labelfile, 'r', encoding='UTF-8') as f:
        raw_data = f.read().split('\n')
    raw_boundaries = [rd.split('\t')[:2] for rd in raw_data]
    boundaries = reformat_boundaries(raw_boundaries)
    return boundaries


def slice_audio(directory, track, boundaries, labelfile):
    count = 1
    rejected_slice_idx = []
    sliced_audio = []
    for bs in boundaries:
        if (bs['finish'] > len(track)) or (bs['start'] > len(track)):
            rejected_slice_idx.append(count-1)
            count += 1
            continue
        root_ext = os.path.splitext(directory)
        path = root_ext[0] + '-' + str(count) + root_ext[1]
        sliced = track[bs['start']:bs['finish']]
        sliced.export(path, format='wav')
        sliced_audio.append(path)
        count += 1
    if rejected_slice_idx:
        lr = open(labelfile, "r")
        lines = lr.readlines()
        lr.close()
        for r in sorted(rejected_slice_idx, reverse=True):
            del lines[r]
        lw = open(labelfile, "w+")
        lw.writelines(lines)
        lw.close()
    return sliced_audio


def slice_via_pydub(dirs, wavfile, labelfile):
    track = AudioSegment.from_wav(wavfile)
    boundaries = get_boundaries(labelfile)
    sliced_audio = slice_audio(dirs, track, boundaries, labelfile)
    return sliced_audio
