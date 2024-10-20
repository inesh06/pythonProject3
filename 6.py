phrase = input("Entrez une phrase : ") #Demandez à l'utilisateur d'entrer une phrase

phrase_inversé= phrase.split()[::-1] # crée une liste de chaque mot avec .split() puis inverse l'ordre avec [::-1]
print('Phrase inversée :'," ".join(phrase_inversé)) #join la liste avec des espaces entre les mots avec .join()