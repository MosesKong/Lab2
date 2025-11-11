def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " , weight)
    BMI = weight/(height**2)
    print("BMI = ", f"{BMI: .2f}")
    if BMI < 18.5:
        print("Under Weight")
    elif BMI > 25.0:
        print("Over Weight")
    else:
        print("Normal Weight")

calculate_bmi(weight=57, height=1.73) 
