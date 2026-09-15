import fonctions
salaire=input("Entrez votre salaire annuel : ")
impot=fonctions.mesImpots(int(salaire))
print(f"Votre impôt est de {impot} euros.")
print(f"Votre salaire après impôt est de {int(salaire)-impot} euros.")