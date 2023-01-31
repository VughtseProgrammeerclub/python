plaatjes = [1, 2, 3]

middelstePlaatje = 0

for i in range(0, 10):
    middelstePlaatje = (middelstePlaatje + 1) if middelstePlaatje != len(plaatjes) - 1 else 0
    links = middelstePlaatje - 1 if middelstePlaatje != 0 else len(plaatjes) - 1
    rechts = middelstePlaatje + 1 if middelstePlaatje != len(plaatjes) - 1 else 0
    print(plaatjes[links], plaatjes[middelstePlaatje], plaatjes[rechts])
