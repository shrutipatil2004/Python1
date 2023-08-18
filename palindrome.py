print("             * Palindrome *")
print("\n")
str1=input("enter str:" )
rev=''
for i in str1:
  rev=i+rev

if str1==rev:
  print("It is palindrome")

else:
  print("It is not palindrome")
