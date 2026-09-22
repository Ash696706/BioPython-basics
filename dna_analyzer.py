dna = "ATGCCATCCGATCGATTACGGGA"
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")
print(a)
print(t)
print(g)
print(c)
gc_content = (g + c) / len(dna) * 100
print("GC content:",round(gc_content),2, "%")
highest = max(a,t,g,c)
print(highest)
if highest == a:
  print("A is most frequent nucleotide")
elif highest == b:
  print("B is most frequent nucleotide")
elif highest == c:
  print("C is most frequent nucleotide")
else:
  print("G is most frequent nucleotide")
