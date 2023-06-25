print("Hello World")

age= int(input("how old are you: "))
print(age)

if age > 18:
    print("you are an adult")
else:
    print("you are a child")

def bmi (weight, height):
    bmi = weight / (height * height)
    return bmi
    