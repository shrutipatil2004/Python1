print("                 * Anagram * ")
print("\n")
str1=input("enter str:" )
str2=input("enter str:" )
count1=0
count2=0
for i in str1:
  if i in str2:
    count1=count1+1

for i in str2:
  if i in str1:
    count2=count2+1

if (count1==len(str2)) and (count2==len(str1)):
  print("\n")
  print("Yes,It is Anagram")

else:
  print("No, It is not Anagram")
