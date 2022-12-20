import re
import spacy
import pymorphy2

with open(r'C:\Users\Note\Desktop\панченко\4\text_for_db.txt', 'r', encoding='utf-8') as f:
    text = f.read()

nlp = spacy.load("uk_core_news_sm")
doc = nlp(text)
normal_forms = {}
for token in doc:
    if re.match(r"[А-ЩЬЮЯҐЄІЇа-щьюяґєії'`’ʼ]", token.text):
        normal_forms[token.lemma_]=token.pos_



morph = pymorphy2.MorphAnalyzer(lang='uk')
for k,v in normal_forms.items():
    normal_forms[k] = (v, [inf[0] for inf in morph.parse (k)[0].lexeme])

print(normal_forms)
