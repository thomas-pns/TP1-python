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
