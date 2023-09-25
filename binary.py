n=int(input("Enter any number:"))
lis=[]
while n!=0:
  lis.append(n%2)
  n=n//2
lis.reverse()
print("Binary of",n,"is:",end='')
for i in lis:
  print(i,end='')
