from collections import Counter
import spacy

EXTRA_STOP_WORDS = ['sent', 'replied', 'search', 'active', 'pana', 'stii', 'stiu', 'chestii', 'macar', 'super', 'seama', 'misto', 'genu', 'vrei',
'usor', 'minute', 'poti', 'cativa', 'lume', 'partile', 'parti', 'exemplu', 'varza', 'cate', 'cica', 'media', 'omitted']

nlp = spacy.load('ro_core_news_sm')

def preprocess_whatsapp_export(text):
    res = []
    for line in text.split('\n'):
        res.append(line[line.find(': '):])
    return '\n'.join(res)

with open(file='sample_texts6_wapp.txt', encoding='utf8') as f:
    text = f.read()[:]
    whatsapp_text = preprocess_whatsapp_export(text)
    
    doc = nlp(whatsapp_text)
    words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct and len(token.text) > 3]

    # noun tokens that arent stop words or punctuations
    nouns = [token.text
            for token in doc
            if (not token.is_stop and
                not token.is_punct and
                token.pos_ == "NOUN") and
                len(token.text) > 3 and
                token.text.lower() not in EXTRA_STOP_WORDS]

    # noun tokens that arent stop words or punctuations
    verbs = [token.text
            for token in doc
            if (not token.is_stop and
                not token.is_punct and
                token.pos_ == "VERB") and
                len(token.text) > 3]

    adjectives = [token.text
            for token in doc
            if (not token.is_stop and
                not token.is_punct and
                token.pos_ == "ADJ") and
                len(token.text) > 3]


word_freq = Counter(words)
noun_freq = Counter(nouns)
verb_freq = Counter(verbs)
adj_freq = Counter(verbs)
print(noun_freq.most_common(150))
