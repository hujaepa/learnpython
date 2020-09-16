"""
Question 3: Given a string, display only those characters which are present at an even index number.
logical operator in python
AND - &
OR - |
"""
word="Hello_World"

for i in range(len(word)):
    if(i%2==0):
        print(word[i]+" : "+str(i))