s1 = set(map(int, input('give your 1st set: ').split(",")))
print("1st set is:\n", s1)
s2 = set(map(int, input('give your 2nd set: ').split(",")))
print("2nd set is:\n", s2)

if s1.issubset(s2):
    print ("s1 is subset of s2\n")
elif s2.issubset(s1):
    print("s2 is subset of s1\n")
