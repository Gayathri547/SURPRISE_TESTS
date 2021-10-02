text = input("give your input\n")
words = []
words = text.split(" ")
wfreq=[words.count(w) for w in words]
# to combine the words and its freqency - used zip
x = dict(zip(words,wfreq))
print("Given words with it's frequency are")
print(x)
a = [x[i] for i in x]
a.sort(reverse = True)
print("descending order of frequency is",a)
# b = [i for i in x]
# b.sort(reverse = True)
# print("descending order of words is",b)
