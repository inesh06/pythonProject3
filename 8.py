liste=[10,2,5,18,2]
nom=["A","B","C","D","E"]
for i in range(len(liste)-1):
    for j in range(i+1,len(liste)):
        if liste[j]<liste[i]:
            a=liste[i]
            liste[i]=liste[j]
            liste[j]=a
            b=nom[i]
            nom[i]=nom[j]
            nom[j]=b


print(liste)
print(nom)