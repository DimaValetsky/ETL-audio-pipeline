from pydub import AudioSegment


def convert_mp4_to_wav(mp4_path, wav_path):
    mp4_version = AudioSegment.from_file(mp4_path, 'mp4')
    mp4_version.export(wav_path, format='wav', parameters=['-ab', '256k', '-ac', '1', '-ar', '16000', '-vn'])
    print('converted from ' + mp4_path + ' to ' + wav_path)
