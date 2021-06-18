# Q1. Create a function getting two integer inputs from user and perform basic mathematical operations

def math(num1, num2):
    print("Addition of two numbers", num1 + num2)
    print("Subtraction of two numbers", num1 - num2)
    print("Multiplication of two numbers", num1 * num2)
    print("Division of two numbers", num1 / num2)


num1 = float(input("Enter Num 1: "))
num2 = float(input("Enter Num 2: "))

math(num1, num2)


# Q2. Create a fumction covid() & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

def covid(patient_name, body_temperature):
    if body_temperature < str(0):
        default = str(98)
        print("Patient Name is ", patient_name, "Body Temperature is ", default)
    else:
        print("Patient Name is ", patient_name, "Body Temperature is ", body_temperature)


covid("Yeshu", " ")
covid("Yeshu", "99")
