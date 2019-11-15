
# Pre-process text with RegEx
import re

def pre_process(text):
    '''
    Takes a string, returns a cleaned string.
    '''
    text_sub = re.sub('[/.\n:-]', ' ', text)  # Remove seaparators of dif kind
    text_sub = re.sub('[,\(\)]', '', text_sub).lower()  # Remove "," and capital letters
    text_sub = re.sub('[^a-z\s]', '', text_sub) # Keep alphanumeric characters only
#     re.sub('[%s]' % re.escape(string.punctuation), ' ', my_text)

    return text_sub


# Pre-process text using gensim
from gensim.parsing.preprocessing import preprocess_string, strip_numeric, strip_short, stem_text, strip_tags, strip_punctuation, strip_multiple_whitespaces, remove_stopwords

def gensim_preprocess(text):
    '''
    Takes a string, returns a list of cleaned strings.
    '''
    filters = [
        strip_tags,
        strip_punctuation, 
        strip_multiple_whitespaces, 
        strip_numeric, 
        remove_stopwords, 
        strip_short,
        lambda x: x.lower()]
    
    text_proc = preprocess_string(text, filters)
    return text_proc
