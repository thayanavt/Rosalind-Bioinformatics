from Bio import SeqIO

max_total = 0

for record in SeqIO.parse("example.fasta", "fasta"):
  G = str(record.seq).count("G")
  C = str(record.seq).count("C")
  total = ((G+C)/len(record.seq))*100

  if total >= max_total:
    max_total = total
    id = record.id

print(f">{id}")
print(max_total)
