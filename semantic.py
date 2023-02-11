#Import spacy
import spacy

nlp = spacy.load('en_core_web_md')

###EXAMPLE 1###
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


###EXAMPLE 2###
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Interesting that cat and monkey(animals) have less similarity than apple banana (fruit).

#My example:
tokens = nlp('dog bowl kitchen spoon')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


###EXAMPLE 3###
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)



#Running example file with 'en_core_web_sm' rather than 'en_core_web_md' results in less useful information of 
#similarity as it does not give context, only similarity based of characteristics such as tagger or parser.