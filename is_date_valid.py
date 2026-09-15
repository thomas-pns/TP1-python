import fonctions

day=input ("Entrez le jour (1-31) : ")
month=input ("Entrez le mois (1-12) : ")
year=input ("Entrez l'année : ")


if fonctions.is_date_valid(int(day), int(month), int(year)):
    print("La date est valide.")
else:   
    print("La date n'est pas valide.")
