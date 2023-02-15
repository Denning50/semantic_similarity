import spacy

nlp = spacy.load('en_core_web_md')# Changed this to the simpler model 'en_core_web_sm' to get the first results int he commetns below. 
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# The output of the program using 'en_core_web_sm' shows that 'cat' and 'monkey' have a similarity score of 0.45, while 'banana' 
# and 'monkey' have a higher similarity score of 0.56. Interestingly, the similarity score between 'cat' 
# and 'banana' is quite low at 0.28, which makes sense given that they are not semantically related.

# Running the 'en_core_web_md' model, we can observe that the similarity scores between 'cat' and 'monkey' and 
# between 'banana' and 'monkey' have increased compared to the scores obtained using the 'en_core_web_sm' model. 
# This suggests that the larger model is able to capture more subtle nuances in meaning and context, 
# leading to more accurate similarity scores.