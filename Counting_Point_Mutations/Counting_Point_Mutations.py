seq1 = input("insira sequencia 1: ")
seq2 = input("insira sequencia 2: ")
seq1.upper()
seq2.upper()

total = 0
for nucleotideo_seq1, nucleotideo_seq2 in zip(seq1, seq2):
    if nucleotideo_seq1 != nucleotideo_seq2:
        total +=1

print(total)