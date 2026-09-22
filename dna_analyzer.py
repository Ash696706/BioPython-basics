#DNA sequence
dna = "ATGCCATCCGATCGATTACGGGA"
#count ATGC
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")
print(a)
print(t)
print(g)
print(c)
#GC content
gc_content = (g + c) / len(dna) * 100
print("GC content:",round(gc_content),2, "%")
# maximum value
highest = max(a,t,g,c)
print(highest)
if highest == a:
  print("A is most frequent nucleotide")
elif highest == t:
  print("T is most frequent nucleotide")
elif highest == g:
  print("G is most frequent nucleotide")
else:
  print("C is most frequent nucleotide")
# minimum value   
minimum = min(a,t,g,c)
print(minimum)
if minimum == a:
  print("A")
elif minimum == g:
  print("G")
elif minimum == c:
  print("C")
else:
  print("T")
#count nucleotide percentage
percentage_a = a/len(dna)*100
print("percentage of A:",round(percentage_a, 2), "%")
percentage_t = t/len(dna)*100
print("percentage of T:",round(percentage_t, 2), "%")
percentage_g = g/len(dna)*100
print("percentage of G:",round(percentage_g, 2), "%")
percentage_c = c/len(dna)*100
print("percentage of C:",round(percentage_c, 2), "%")
