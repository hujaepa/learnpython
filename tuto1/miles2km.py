"""
This program is to convert miles into km.
type casting is needed when receiving input as string in order to convert into number.
Vice versa.
Standard Data type in python:
    -Numbers
    -String
    -List
    -Tuple
    -Dictionary
"""

miles = input("Enter how many miles: ")
km = float(miles) * 1.609
print("miles in km is " + str(km))