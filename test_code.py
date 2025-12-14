#Array

a = [2,3,1,4,5]
b = [1,2,3,5,4]
c = ['This', 'is', 'an', 'array']
int1 = 567
str1 = "Bhumik"
str2 = "My test code"
str3 = "143"
#Sorting
print(sorted(a))
#Length
print(len(a))
#Comparing array
if sorted(a)==sorted(b):
    print("Arrays are matching")
else:
    print("Arrays not matching")


#Array functions
a.append(7)
print(a)

b.insert(1,5)
print(b)

print(b.count(5))

b.remove(2)
print(b)

b.pop(1)
print(b)

b.clear()
print(b)

#String to array
print(list(str2))
print(str2.split())

#Array to string
d=''.join(c)
print(d)
print(list(d))
print(str(int1))
print(int(str3))
a.append(7)
print(a)

#String functions

str1 = "This is a string"
str2 = "String number 2"

print(str1.count("i"))
print(str1.upper())
print(str2.replace("i","2"))
print(len(str2))
str3=''.join(reversed(str1))
print(str3)


print(str1[::-1])
#Reverse a string
s = "GeeksforGeeks"

# Initialize an empty string to hold reversed result
rev = ""

# Loop through each character in original string
for ch in s:
  
    # Add current character to front of reversed string
    rev = ch + rev

print(rev)

print(s==rev)

#Duplicates in a string
e = []

for count in s:
    if s.count(count)>1 and count not in e:
        # print(count)
        e.append(count)
print(e)

s = "racecar"
c = len(s)
for i in range(c):
    b = False
    for j in range(c):
        if i!=j and s[i]==s[j]:
            b=True
            break
            
    if not b:
        print(s[i])



