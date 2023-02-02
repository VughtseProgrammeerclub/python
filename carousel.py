plaatjes = [1, 2, 3]

middelstePlaatje = 0

# Optie 1: met Ternary operators. Compact maar minder leesbaar
for i in range(0, 10):
    middelstePlaatje = (middelstePlaatje + 1) if middelstePlaatje != len(plaatjes) - 1 else 0
    links = middelstePlaatje - 1 if middelstePlaatje != 0 else len(plaatjes) - 1
    rechts = middelstePlaatje + 1 if middelstePlaatje != len(plaatjes) - 1 else 0
    print(plaatjes[links], plaatjes[middelstePlaatje], plaatjes[rechts])

print()

middelstePlaatje = 0
# Optie 2: met gewone ifs. Iets leesbaarder
for i in range(0, 10):
    middelstePlaatje = middelstePlaatje + 1
    if middelstePlaatje == len(plaatjes):
        middelstePlaatje = 0
    
    links = middelstePlaatje - 1
    if middelstePlaatje == 0:
        links = len(plaatjes) - 1
    
    rechts = middelstePlaatje + 1
    if rechts == len(plaatjes):
        rechts = 0
    
    print(plaatjes[links], plaatjes[middelstePlaatje], plaatjes[rechts])
