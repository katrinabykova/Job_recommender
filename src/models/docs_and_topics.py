
from src.models.stop_words_list_1 import stop_words_1
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation 
from sklearn.decomposition import NMF

def docs_to_topics_lda(
                  components, 
                  word_num,
                  positions,
                  resumes,
                  max_df=0.45,
                  min_df = 0.001,
                  stop_words = stop_words_1):
    
    tf_idf = TfidfVectorizer(ngram_range=(1, 2),
                            max_df = max_df,
                            min_df = min_df,
                            stop_words = stop_words)   

    components = components  # number of LSA components
    lda = LatentDirichletAllocation(components, random_state = 5)

    # reduce dimensionality
    lda_vec_pos = lda.fit_transform(tf_idf.fit_transform(positions).toarray())  
    lda_vec_res = lda.transform(tf_idf.transform(resumes).toarray())  
    
    return lda_vec_pos, lda_vec_res


def docs_to_topics_lsa(max_df,
                  min_df,
                  stop_words,
                  components, 
                  positions,
                  word_num,
                  resumes):
    
    tf_idf = TfidfVectorizer(ngram_range=(1, 2),
                            max_df = max_df,
                            min_df = min_df,
                            stop_words = stop_words)   

    components = components  # number of LSA components
    lsa = TruncatedSVD(components, random_state = 5)

    # reduce dimensionality
    lsa_vec_pos = lsa.fit_transform(tf_idf.fit_transform(positions).toarray())  
    lsa_vec_res = lsa.transform(tf_idf.transform(resumes).toarray())  
    
    return lsa_vec_pos, lsa_vec_res

def docs_to_topics_lsa(max_df,
                  min_df,
                  stop_words,
                  components, 
                  positions,
                  word_num,
                  resumes):
    
    tf_idf = TfidfVectorizer(ngram_range=(1, 2),
                            max_df = max_df,
                            min_df = min_df,
                            stop_words = stop_words)   

    components = components  # number of LSA components
    lsa = TruncatedSVD(components, random_state = 5)

    # reduce dimensionality
    lsa_vec_pos = lsa.fit_transform(tf_idf.fit_transform(positions).toarray())  
    lsa_vec_res = lsa.transform(tf_idf.transform(resumes).toarray())  
    
    return lsa_vec_pos, lsa_vec_res


def docs_to_topics_nmf(max_df,
                  min_df,
                  stop_words,
                  components, 
                  positions,
                  word_num,
                  resumes):
    
    tf_idf = TfidfVectorizer(ngram_range=(1, 2),
                            max_df = max_df,
                            min_df = min_df,
                            stop_words = stop_words)   

    components = components  # number of LSA components
    nmf = NMF(components, random_state = 5)

    # reduce dimensionality
    nmf_vec_pos = nmf.fit_transform(tf_idf.fit_transform(positions).toarray())  
    nmf_vec_res = nmf.transform(tf_idf.transform(resumes).toarray())  
    
    return nmf_vec_pos, nmf_vec_res
