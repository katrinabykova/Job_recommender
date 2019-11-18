###Project summary

##Job recommender

Katrina Bykova

---------------------------------------------------------------------------------------------------------------

**Introduction**

​	A job search is a time consuming process. Automating any part of the search would give a job seeker more time for networking and following up with potential employers.

**Data**

​	Job descriptions were scraped from *Indeed* with *Beautiful Soup*. Resumes for  the following positions were collected - data scientist/analyst, clinical trial specialist and civil engineer. The resumes were found as images from various websites and then were read in as a text with *Pytesseract*.  The choice of the resumes was driven by similarities in the descriptions and yet very different fields that they belong to. The goal of the recommender algorithm was to return job postings from the correct field.

**Results**

​	Overview of the algorithm steps: 1. Extraction of a required skills section from a job description text; 2. Required skills section tokenization and vectorization; 3. Job description topic modeling; 4. Job recommendation based on cosine similarity with a resume.

​	For the initial topic modeling a complete section of a job description text was used. Subsequently, the required skills section was extracted from the job description text with a use of common word combinations and key words that start and end the skill section. The use of the required skills part instead of the complete job description text resulted in the topics being more focused on  the skills and job requirements and less so not the hiring company specifics.

​	*Spacy* package was used for tokenization. Lemmatization and retaining only nouns were tested in addition to removing common stop words from the job description text. Overall, retaining only nouns worked better for the topic modeling part of the algorithm. The tokenized text was vectorized with TF-IDF.

​		For topic modeling several methods were tested - matrix factorization, LSA and NMF, and Latent Dirichlet Allocation (LDA). Overall, all methods gave similar results in terms of the topic separation and topic meaning.

​	Clusters formed by the job descriptions with topics as features were examined with the use of *UMAP*. 5, 10 and 15 topics gave less separated clusters than 20 topics. 20 topics were then used as a starting point for the subsequent steps.

​	Resumes texts were then transformed with developed models. LDA was used as an example. A job recommendation was given based on the cosine similarity to job descriptions. 

**Conclusions**

​	A job recommender could perform a job search with fewer clicks and prioritize job postings based on the resume matching score.

**Future work**

​	1. Extend the library of job postings and resumes for improving the recommender performance. 2. Optimize job recommender algorithm using a confusion matrix by decreasing the number of false positives that come from unrelated job postings.  3. Add filters for the job title and years of experience. The job title can be matched to the resume's title or summary, the years of experience match would require an extraction of specific skills and matching them to the input resume. 









