import json

word_list = []
with open('toeic-words.json', 'rt', encoding='utf-8') as fp:
    toeic_words = json.loads(fp.read())
    for word_id, word in toeic_words.items():
        print(word_id, word['word'])
        if word['other_types']:
            for item in word['other_types']:
                print(item)
        if word['part_of_speech']:
            for item in word['part_of_speech']:
                print(item)
        if word['sentences']:
            for item in word['sentences']:
                print(item)
        word_list.append('{} -> {}'.format(word['word'], '||'.join(word['part_of_speech'])))
        print('-'*80)

with open('toeic-words.txt', 'wt', encoding='utf-8') as fp:
    fp.write('\n'.join(word_list))
