a=str(int(input("Enter any string:")))
b=0
for i in a:
  b=b+int(i)**len(a)
  
if int(a)==b:
  print(" It is Armstrong number ")

else:
  print(" It is not Armstrong number")
