from src.modules.srt_processor.module import get_labels
from src.modules.pathes_generator.module import get_voc_path, get_labelfile


def generate_labels(prepared_srt_path, voc_file):
    voc_path = get_voc_path(prepared_srt_path, voc_file)
    labels = get_labels(voc_path)
    labelfile = get_labelfile(prepared_srt_path, voc_file)
    with open(labelfile, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(labels))
    print(labelfile)
