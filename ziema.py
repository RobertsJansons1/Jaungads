dati = input("Ievadiet savu vārdu un uzvārdu: ")

with open("ziema.txt", "w", encoding="utf8") as fails:
    fails.write(f"Vārds un uzvārds: {dati}")