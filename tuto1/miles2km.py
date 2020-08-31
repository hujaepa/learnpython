"""
This program is to convert miles into km.
type casting is needed when receiving input as string in order to convert into number.
Vice versa
"""

miles = input("Enter how many miles: ")
km = float(miles) * 1.609
print("miles in km is " + str(km))