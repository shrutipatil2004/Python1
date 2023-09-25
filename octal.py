n=int(input("Enter any number:"))
lis=[]
while n!=0:
  lis.append(n%8)
  n=n//8
lis.reverse()
print("Octal of",n,"is:",end='')
for i in lis:
  print(i,end='')              
