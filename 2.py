
while True: #une boucle qui recommence tant que les conditions ne sont pas respectées

     courriel= input("Entrer votre adresse courriel : ") #L'utilisateur entre son courriel
     arobase= courriel.count("@") #compte le nombre de "@"
     caracteres_valides = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ123456789.-" #tous les caractères possiblement valides

     nom_utilisateur= courriel.split("@")[0] #extrait le nom d'utilisateur du courriel
     domaine= courriel.split("@")[1] #etrait le domaine du courriel


     if all(i in caracteres_valides for i in nom_utilisateur): #si tous les caractères du nom d'utilisateurs sont valides
         if arobase==1: #si contient juste 1 arobase
             if courriel.endswith(".com") or courriel.endswith(".ca") or courriel.endswith(".org") or courriel.endswith(".net"): #si fini par un des domaines
                print("Votre courriel est valide") #affiche le message
                print("Votre nom d'utilisateur est :", "".join(nom_utilisateur)) #affiche le nom d'utilisateur
                print("le domaine est :", "".join(domaine)) #affiche le domaine
                break


