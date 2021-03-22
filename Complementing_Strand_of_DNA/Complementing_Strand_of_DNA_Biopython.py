from Bio.Seq import Seq

dna = "ACT"
dna = Seq(dna)
print(dna.reverse_complement())