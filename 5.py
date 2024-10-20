nombre1=int(input("Entrer un premier nombre: "))  #L'utilisateur entre un premier nombre.  int() convertie en valeur numérique le nombre donné
nombre2=int(input("Entrer un deuxième nombre :")) #L'utilisateur entre un deuxième nombre. int() convertie en valeur numérique le nombre donné4
operation=input("Entrer une opération entre +,-,*,/ : ") #l'utilisateur entre une opération ente celles affichées

if operation=="*": #si l'opération est *
    print(nombre1*nombre2) #le programme affiche le produit des deux nombres
elif operation=="+": #si l'opération est +
    print(nombre1+nombre2) #le programme affiche l'addition des deux nombres
elif operation=="-": #si l'opération est -
    print(nombre1-nombre2) #le programme affiche la différence des deux nombres
elif operation=="/": #si l'opération est /
    if nombre2==0: #le programme vérifie que ce n'est pas une division par 0
        print("error") #si c'est une division par 0, le programme affiche error
    else:
        print(nombre1/nombre2) #si ce n'est pas une division par 0, le programme affiche la division des deux nombres
else:
    print("l'opérateur est invalide") #si l'opérateur choisi n'est pas parmi les opérateurs valident, le programme affiche que l'opérateur est invalide
