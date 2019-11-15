
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def similarity(X_red, Z_red):
    score = cosine_similarity(X_red, Z_red).round(2)
    
    column_labels = ['Resume'+str(i) for i in range(1, Z_red.shape[0]+1)]
    row_labels = ['Job'+str(i) for i in range(1, X_red.shape[0]+1)]
    
    
    
    similarity_df = pd.DataFrame(score, columns=column_labels, index=row_labels)
    
    #Remove later
#     similarity_df['clean_text '] = jobs_skills.clean_text
#     similarity_df['type'] = jobs_skills.type
#     similarity_df['job_title'] = jobs_skills.job_title
#     similarity_df['description'] = jobs_skills.job_title
    
    return similarity_df
