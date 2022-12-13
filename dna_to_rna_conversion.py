def dnd_to_rna(dna):
    return dna.translate(str.maketrans("T","U"))


print(dnd_to_rna('TTTT'))