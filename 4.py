phrase = input("Entrer une phrase : ") #Demander une phrase à l'utilisateur
lettre=input("Entre une lettre à échanger : ") #Demander quel lettre l'utilisateur veut changer
mot=input("Entre un mot pour remplacer : ") #Demander quel est le mot qui va remplacer la lettre
new="" #la nouvelle phrase après les substitutions
vrai="" #la nouvelle phrase sans d'espace

#la phrase après la substitution
for i in phrase: #Pour tout les caractères de la phrase
     if i==lettre: # si le caractère =lettre
         new+=mot #change le par le nouveau mot
     else:
         new+=i #sinon, garde le caractère

#La phrase sans espace, pour vérifier le palindrome
for p in new:  #Pour tous les caractères de la nouvelle phrase
    if p!=" ": #si le caractère n'est pas un espace
        vrai+=p #ajoute le à vrai

#affiche la phrase après la substitution et sans les espaces
print("La nouvelle phrase est :",vrai)

if vrai==vrai[::-1]: #si la phrase est pareil normalement et inversé
    print("Cette phrase est un palindrome") #affiche que la phrase est un palindrome
else:
    print("Cette phrase n'est pas un palindrome") #sinon, affiche quel n'est pas un palindrome