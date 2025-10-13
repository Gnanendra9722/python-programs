s1={1,2,3,4}
s2={3,4,5,6}
print(s1,s2)
s3=s1.union(s2)
print(f"{s3} is union")
s4=s1.intersection(s2)
print(f"{s4} is intersection")
s5=s1.difference(s2)
print(f"{s5} is s1-s2")
s6=s2.difference(s1)
print(f"{s6} is s2-s1")

s7=s1.symmetric_difference(s2)
print(f"{s7} is s1-s2 union s2-s1")
