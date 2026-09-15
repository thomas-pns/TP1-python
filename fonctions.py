def isbissextile(year):
    assert isinstance(year,int), "L'année doit être un nombre entier"

    if (year % 4 == 0 and str(year)[-1] != "0" and str(year)[-2] != "0") or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(month, year):
    assert isinstance(month,int) and month>=1 and month<=12, "le mois doit être un nombre entier compris entre 1 et 12"  
    bissextile=isbissextile(year)

    days_31=[1,3,5,7,8,10,12]

    if month == 2:
        if bissextile:
            return 29
        else:
            return 28
    elif month in days_31:
        return 31
    else:
        return 30

def is_date_valid(day, month, year):
    assert isinstance(day,int) and isinstance(month,int) and isinstance(year,int), "Le jour, le mois et l'année doivent être des nombres entiers"
    assert month>=1 and month<=12, "le mois doit être un nombre entier compris entre 1 et 12"
    assert day>=1 and day<=31, "le jour doit être un nombre entier compris entre 1 et 31"

    max_day=days_in_month(month,year)
    if day <= max_day:
        return True
    else:
        return False

def mesImpots(salaire):
    assert isinstance(salaire,int) and salaire>=0, "Le salaire doit être un nombre entier positif"
    impot=0
    if salaire >= 11601 and salaire <= 29579:
        impot = (salaire - 11601) * 0.11
    elif salaire >= 29580 and salaire <= 84577:
        impot = (salaire - 29580) * 0.30 + (29579 - 11601) * 0.11
    elif salaire >= 84578 and salaire <= 181917:
        impot = (salaire - 84578) * 0.41 + (84577 - 29580) * 0.30 + (29579 - 11601) * 0.11
    elif salaire >= 181918:
        impot = (salaire - 181918) * 0.45 + (181917 - 84578) * 0.41 + (84577 - 29580) * 0.30 + (29579 - 11601) * 0.11
    return int(impot)

def multiplication(m1, m2):
    m3=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i,j,k,m1[i][k]*m2[k][j], m1[i][k],m2[k][j])
                m3[i][j]+=(m1[i][k]*m2[k][j])
    return m3

def multiplicationV2(m1, m2):
    assert len(m1)==len(m2[0]), "Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice"
    m3 = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                print(i,j,k,m1[i][k]*m2[k][j], m1[i][k],m2[k][j])
                m3[i][j]+=(m1[i][k]*m2[k][j])
    return m3


