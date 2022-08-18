import re
import spacy


def detect_voc_cases(f, lines):
    nlp = spacy.load('en_core_web_trf')
    
    regular = r'(, (Mrs?\.)? ?[A-Z]\w*(,|[.?!]))|^((Mrs?\.)? ?[A-Z]\w*,)'

    srt_block = []
    string_block = ''
    tags_sub_pattern = re.compile(r"(<.*?>)|(\[.*?\])|({.*?})")
    quotes_sub_pattern = re.compile(r"('.*?')|(\".*?\")")

    for line in lines:

        line = re.sub(tags_sub_pattern, '', line)
        line = re.sub(quotes_sub_pattern, '', line)

        if line != '\n':
            string_block += line
            srt_block.append(line)

        else:
            person = False
            match_string = re.findall(regular, string_block, re.MULTILINE)
            if match_string:
                text_check = nlp(string_block)
                for ent in text_check.ents:
                    if ent.label_ == "PERSON":
                        person = True
                if person:
                    string_block += '\n'
                    f.write(string_block)

            srt_block = []
            string_block = ''
