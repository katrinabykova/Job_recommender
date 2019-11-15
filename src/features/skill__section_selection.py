
# Label start and end sentence for sentence collection
# Re-write if have time

# Key words for collecting skills and requirements portion of a job description
start_list = [
    'ideal data scientist', 'ideal candidate', 'you’ll', 'you will', 'you should', 'if you are', 'skills',
    'job description', 'job', 'requirements', 'ability', 'top candidate', 'experience', 'you must', 
    'be instrumental', 'key functions', 'role summary', 'your role', 'responsibilities', 'key duties',
    'job-specific skills', 'experience', 'ability'
]
stop_list = [
    'we offer', 'apply', 'with more than', 'focused on', 'location', 'job type', 'sponsor h1b',
    'more information', 'equal employment', 'race', 'color', 'religion', 'interested', 'we strive'
]


# Make ngrams
def ngrams(sent, n):
    ngrams = zip(*[sent.lower().split(' ')[i:] for i in range(n)])
        
    return [' '.join(ngram) for ngram in ngrams]


# Get indices for the start and end sentences of a job skill section
def start_stop(sents):
    start = []
    stop = []
    
    for ix,sent in enumerate(sents):        # single word
        for word in sent.lower().split(' '):  
            if word in start_list:
                start.append(int(ix))
                
   
    for ix,sent in enumerate(sents):          # two words
        for two_words in ngrams(sent, 2):
            if word in start_list:
                start.append(int(ix))                

    for ix,sent in enumerate(sents):          # three words
        for three_words in ngrams(sent, 3):
            if word in start_list:
                start.append(int(ix))  
        
        
    for ix,sent in enumerate(sents):          # single word
        for word in sent.lower().split(' '):
            if word in stop_list:
                stop.append(int(ix))

    for ix,sent in enumerate(sents):          # two words
        for two_words in ngrams(sent, 2):
            if word in stop_list:
                stop.append(int(ix))                

    for ix,sent in enumerate(sents):          # three words
        for three_words in ngrams(sent, 3):
            if word in stop_list:
                stop.append(int(ix))  
    
    if start==[]:
        start = 0
    
    if stop==[]:
        stop = len(sents)-1
        
    if type(start) == list:
        start = min(start)

    if type(stop) == list:
        stop = min(stop)  
    
    if start >= stop:
        stop = len(sents)-1
        
    if stop==0:
        stop = len(sents)-1
        
    if start==len(sents)-1:
        start = 0
    
    return start, stop


# Collect skills and requirements
def extract_skills(sents, start_stop):
    (start, stop) = start_stop
    skills_text = ''
    
    for ix,sent in enumerate(sents):
        if ix >= start and ix < stop:
            skills_text = skills_text + sent + '. '
            
    if start==0 and stop==0:
        for sent in sents:
            skills_text = skills_text + sent + '. '
        
    return skills_text   
