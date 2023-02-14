import spacy

# load english language model

nlp = spacy.load('en_core_web_sm',disable=['ner','textcat'])

text = "could you move the horse from A1 to B2."

# create spacy 

doc = nlp(text)

for token in doc:
    print(token.text,'->',token.pos_)
    print(token.pos_)


for token in doc:
    # check token pos
    if token.pos_=='NOUN' or token.pos_ == 'PROPN':
        print(token.text)