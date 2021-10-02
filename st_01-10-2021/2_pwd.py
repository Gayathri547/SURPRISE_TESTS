c1,c2,c3 = 0,0,0
x = input("enter your input:")
if (len(x) >= 8):
    for i in x:
        if ( i >='a' and i <= 'z') and (i >='A' and i <='Z'):
            c1 += 1       
        if i == '$' or i == '#' or i == '@' or i==' ' or i=='!' or i=='%' or i=='^' or i=='&' or i=='*' or i==',' or i=='.' or i=='/' or i=='<' or i=='>' or i=='|' or i=='{' or i=='}' or i=='[' or i==']' or i=='(' or i==')' or i==' ':
            c2 +=1
    if any(i.isdigit() for i in x):
            c3 +=1

if (c1>=1 and c2>=1 and c3>=1):
    print("Valid Password")
else:
    print("Invalid Password")
