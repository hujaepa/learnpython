#BMI = weight(kg)/[height(m)]2

import math

height = float(input())
weight = float(input())

bmi = weight/math.pow(height,2)

if(bmi < 18.5):
    print("Your BMI is "+str(format(bmi,".2f"))+". So you are underweight")
elif(bmi >= 18.5 and bmi < 25.0):
    print("Your BMI is "+str(format(bmi,".2f"))+". So you are normal")
elif(bmi >= 25.0 and bmi < 30):
    print("Your BMI is "+str(format(bmi,".2f"))+". So you are overweight")
elif(bmi >= 30):
    print("Your BMI is "+str(format(bmi,".2f"))+". So you are obese")