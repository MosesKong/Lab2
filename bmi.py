def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " , weight)
    BMI = weight/(height**2)
    print("BMI = ", f"{BMI: .2f}")
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI > 25.0:
        print("Over Weight")
        return 0
    else:
        print("Normal Weight")
        return 1

print(calculate_bmi(weight=37, height=1.73))
print(calculate_bmi(weight=57, height=1.73))
print(calculate_bmi(weight=97, height=1.73))
