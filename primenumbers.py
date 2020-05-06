a=int(input('enter last number'))
print(2)
for i in range(3,a):
    j=0
    for k in range(2,i):
        if i%k==0:
            j=j+1
    if j==0:
        print(i)
