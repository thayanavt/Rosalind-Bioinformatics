sequence = "GATATATGCATATACTT"
string = "ATAT"
cont = ''
for i in range(len(sequence)):
  if sequence[i:i+len(string)]==string:
    cont = cont + f' {i+1}'
   
print(cont)

