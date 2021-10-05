i = 1
while i<=100:
    if i%15 == 0:
        print("fizz buzz",end = '\t')
    elif i%3 ==0:
        print("fizz", end = '\t')
    elif i%5 ==0:
        print("buzz", end = '\t')
    else:
        print(i, end = '\t')
    i +=1 