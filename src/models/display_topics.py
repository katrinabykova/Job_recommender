
import pandas as pd

def topics_to_df(model, feature_names, no_top_words, model_name):
    '''
    Add topic words for dimensionality reduction to dataframe.
    '''
    df = pd.DataFrame()
    words_list = []
    
    for ix, topic in enumerate(model.components_):
        words = ", ".join([feature_names[i]for i in topic.argsort()[:-no_top_words - 1:-1]])
        words_list.append(words)
    
    df[model_name] = pd.Series(words_list)
     
    return df
