#Basic Weight, Height & BMI Calculator
import math

weight = float(input("Enter Your Weight: "))
weight_type = input("Kilograms or Pound? (K/P): ").upper()
height = float(input("Enter Your Height: "))
height_type = input("Inches or Centimetres? (I/C): ").upper()

if weight_type == "P":
    weight = weight * 0.453592

if height_type == "I":
    height = height * 0.0254
elif height_type == "C":
    height = height / 100

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
