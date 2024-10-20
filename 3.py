phrase=input("Entre une phrase:")  #L'utilisateur entre une phrase
minuscule=phrase.lower() #convertis la phrase en minuscule pour identifier les voyelles même en majuscule

#Compte le nombre de voyelles avec .count et l'affiche
print("le nombre de voyelle :",minuscule.count("a")+minuscule.count("e")+minuscule.count("i")+minuscule.count("o")+minuscule.count("u"))

#Compte le nombre d'espaces et ajoute 1.
print("Le nombre de mot est :",phrase.count(" ")+1)
