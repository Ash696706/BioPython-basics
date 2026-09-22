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
