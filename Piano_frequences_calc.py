
def calcul_frequences(ref_freq):
    note_frequences = {}

    for n in range(-48, 40):
        frequence = round((2 ** (1/12)) ** n * ref_freq, 2)
        note_frequences[f"Note {n+49}"] = frequence
    
    return note_frequences

ref_freq = float(input("Donnez la fréquence de référence pour la3 (440 Hz par défaut): ") or 440)

frequences = calcul_frequences(ref_freq)

with open('frequences.txt', 'w') as file:
    for key, frequence in frequences.items():
        file.write(f"{key}: {frequence} Hz\n")

print(f"sauvegardé avec succès à 'frequences.txt'.")
