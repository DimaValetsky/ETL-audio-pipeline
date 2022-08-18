import re


def reformat_time(label):
    if '\t' in label:
        label = re.split("[:,	]", label)[:-1]
    else:
        label = re.split("[:,	]", label)
    for i in range(len(label)):
        label[i] = int(label[i])
    seconds = label[0] * 3600 + label[1] * 60 + label[2]
    particles = label[3] * 1000
    particles = str(particles)
    while len(particles) < 6:
        particles = particles + '0'
    label = str(seconds) + '.' + str(particles) + '\t'
    return label


def check_vocatives_extended(material) -> str:
    res = []
    for i in range(len(material)):
        res.append(material[i])

    result = ' '.join(res)
    return result


def get_labels(voc_file):
    with open(voc_file, 'r', encoding='UTF-8') as f:
        single_row = f.read()
    split_pattern = r'\n\n'
    spec_sub_pattern = re.compile(r"[^\w ,.!']")
    apstr_sub_pattern = re.compile(r"(?<!\w)'|'(?!\w)")
    tags_sub_pattern = re.compile(r"(<.*?>)|(\[.*?\])|({.*?})")
    sps_beg_sub_pattern = re.compile(r"^\s+|")
    sps_mul_sub_pattern = re.compile(r"\s{2,}")

    replacements = [
        tags_sub_pattern,
        spec_sub_pattern,
        apstr_sub_pattern,
        sps_beg_sub_pattern
    ]
    result = re.split(split_pattern, single_row)[:-1]
    final = []
    for r in result:
        splitted = re.split("\n| --> ", r.replace('\t', ''))[1:]
        splitted[0] = reformat_time(splitted[0])
        splitted[1] = reformat_time(splitted[1])

        incntxt_voc = check_vocatives_extended(splitted[2:])

        for rep in replacements:
            incntxt_voc = re.sub(rep, '', incntxt_voc)

        incntxt_voc = re.sub(sps_mul_sub_pattern, ' ', incntxt_voc)

        #incntxt_voc = incntxt_voc.title()

        final.append(str(splitted[0] + str(splitted[1]) + str(incntxt_voc)))
    return final
