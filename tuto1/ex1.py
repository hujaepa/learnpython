"""
Question 1: 
Given a two integer numbers return their product and  
if the product is greater than 1000, then return their sum.

Python comparison operator:
    == (equal to)
    != (not equal to)
    <> (not equal to)
    > (more than)
    < (less than)
    >= (more than equal)
    <= (less than equal)
"""
number1=80
number2=90

product=number1*number2

if(product > 1000):
    sum=number1+number2
    print("The result is "+str(sum))
else:
    print("The result is "+str(product))