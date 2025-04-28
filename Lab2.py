

def calculate_BMI(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    #print("BMI = " + str(bmi))
    return bmi


def classify_BMI(bmi_value):
    if bmi_value < 18.5:
        print("You are UNDERWEIGHT")
    elif bmi_value >= 18.5 and bmi_value <= 25.0:
        print("Your weight is NORMAL")
    else:
        print("You are OVERWEIGHT")
    return


def main():
    bmi_output = calculate_BMI(1.73, 60)
    print("BMI Value = " + str(bmi_output))
    classify_BMI(bmi_output)



if __name__ == "__main__":
    main()





