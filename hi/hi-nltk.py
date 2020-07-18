import nltk

sentence = "Hola, soy un robot, me llamo Bender. ¿Quién eres tú?"
tokens = nltk.word_tokenize(sentence, "spanish")
print("Tokens")
print(tokens)
tagged = nltk.pos_tag(tokens)
print("Tags")
print(tagged)