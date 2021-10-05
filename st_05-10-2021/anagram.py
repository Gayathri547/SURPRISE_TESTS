#anagram means a word, phrase, or name formed by rearranging the letters of another
#by using sorted function we can get the char by char in list form so that we can compare both the strings
s1 = input("give your first string:\n" )
s2 = input("give your second string:\n")
if(sorted(s1) == sorted(s2)):
    print("both strings are anagrams")
else:
    print("given strings are not anagrams")
