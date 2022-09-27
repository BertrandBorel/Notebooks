'''Programme d'Indice de Masse Corporel (IMC)'''

weight = float(85)
height = 1.9
bmi = weight / height ** 2

if bmi < 18.5 :
    print("Underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("Normal")
elif bmi >= 25 and bmi < 30 :
    print("Overweight")
else :
    print("Obesity")