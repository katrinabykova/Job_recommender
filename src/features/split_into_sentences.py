
def sent_simple(text):
#   text = re.sub(r'\B([A-Z])', r'. \1', text)
    text = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', text) # separate fused word with a capital letter
    text = re.sub('[/\n:\)\(!]', ' ', text)   # remove end of line char and others
    
    sents = text.split('.')
    
    return sents



# Split into sentences using SpaCy

tokenizer = spacy.load('en_core_web_sm')

def sentences(text):
    text_obj = tokenizer(text)
    sents = []
    for sent in text_obj.sents:
        sents.append(sent.text)
    
    if len(sents) < 3:
        sents = text.split('.')
        
    return sents
