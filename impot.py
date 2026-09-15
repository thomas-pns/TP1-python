import fonctions
salaire=input("Entrez votre salaire annuel : ")
impot=fonctions.mesImpots(int(salaire))
print(f"Votre impôt est de {impot} euros.")
print(f"Votre salaire après impôt est de {int(salaire)-impot} euros.")
print(f"Cela représente {round(impot/int(salaire)*100,2)}% de votre salaire.")

