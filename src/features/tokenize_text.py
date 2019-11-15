
# Tokenize text
import spacy

tokenizer = spacy.load('en_core_web_sm') # load model

# Tokenize text: words
def tokenize_word(text):
        
    text_obj = tokenizer(text, disable=['parser', 'ner'])
    
    text_text = ' '.join([token.text for token in text_obj if not token.is_stop])
  
    return text_text


# Tokenize text: nouns
def tokenize_noun(text):
        
    text_obj = tokenizer(text, disable=['parser', 'ner'])
    
    text_noun = ' '.join([token.text for token in text_obj if token.pos_=='NOUN'])
  
    return text_noun


# Tokenize text: lemma
def tokenize_lemma(text):
        
    text_obj = tokenizer(text, disable=['parser', 'ner'])
    
    text_lemma = ' '.join([token.lemma_ for token in text_obj if not token.is_stop])
  
    return text_lemma


# Tokenize text: lemma and nouns    
def tokenize_noun_lemma(text):
        
    text_obj = tokenizer(text, disable=['parser', 'ner'])
    
    text_noun_lemma = ' '.join([token.lemma_ for token in text_obj if token.pos_=='NOUN'])
   
  
    return text_noun_lemma
