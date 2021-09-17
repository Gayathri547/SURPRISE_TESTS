c1,c2,c3 = 0,0,0
pwd = input("enter your password:\n ")
if (len(pwd) >= 6 and len(pwd)<=16):
    for i in pwd:
        if ( i >='a' and i <= 'z') or (i >='A' and i <='Z'):
            c1 += 1      
        # if int(i) >= 0 and int(i) <=9:
        #     c3 += 1   
        if i == '$' or i == '#' or i == '@':
            c2 += 1

if (c1>=1 and c2>=1 and c1+c2+c3==len(pwd)):
    print("Valid Password")
else:
    print("Invalid Password")