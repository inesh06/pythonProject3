phrase=input("Entrez une phrase : ") #L'utilisateur entre une phrase

nombre=1 #Nombre contient les nombres de mots. Commence par 1 parce que nombre de mots= nbr d'espaces +1

#Va compter le nombre d'espaces
for i in phrase: #Pour tous les caractères dans phrase
    if i==" ": #si i est un espaces
        nombre+=1 #ajoute 1 dans nombre

print("La phrase contient", nombre,"mots.")    #affiche le nombre de mots