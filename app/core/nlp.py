from collections import Counter
import spacy

EXTRA_STOP_WORDS = ['sent', 'replied', 'search', 'active', 'pana', 'stii', 'stiu', 'chestii', 'macar', 'super', 'seama', 'misto', 'genu', 'vrei',
'usor', 'minute', 'poti', 'cativa', 'lume', 'partile', 'parti', 'exemplu', 'varza', 'cate', 'cica', 'media', 'omitted']

nlp = spacy.load('ro_core_news_sm', disable = ['ner'])
nlp.max_length = 2000000

def preprocess_whatsapp_export(text):
    res = []
    for line in text.split('\n'):
        res.append(line[line.find(': '):])
    return '\n'.join(res)

def analyze_whatsapp_export(text):
    text = text.decode('utf-8')
    if len(text) > nlp.max_length:
        print("WARNING: Text file length over limit.")
        text = text[:nlp.max_length-1]
    whatsapp_text = preprocess_whatsapp_export(text)
    
    doc = nlp(whatsapp_text)

    # noun tokens that arent stop words or punctuations
    nouns = [token.text
            for token in doc
            if (not token.is_stop and
                not token.is_punct and
                token.pos_ == "NOUN") and
                len(token.text) > 3 and
                token.text.lower() not in EXTRA_STOP_WORDS]

    noun_freq = Counter(nouns)

    return noun_freq

def analyze_text(text):    
    doc = nlp(text)

    # noun tokens that arent stop words or punctuations
    nouns = [token.text
            for token in doc
            if (not token.is_stop and
                not token.is_punct and
                token.pos_ == "NOUN") and
                len(token.text) > 3 and
                token.text.lower() not in EXTRA_STOP_WORDS]

    noun_freq = Counter(nouns)

    return noun_freq


if __name__ == "__main__":
    r = analyze_text('asd asd asd asd ')
    print(r.most_common(150))
