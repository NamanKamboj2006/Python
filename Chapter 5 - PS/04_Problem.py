#  What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0) 
s.add('20') # length of s after these operations?

# 20 == 20.0     # True
print(len(s)) #2