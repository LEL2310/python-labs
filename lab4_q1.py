# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:47:27 2024

@author: motil
"""

def main():
    Weight=(int(input("Enter Weight (in kg):")))
    Height=(int(input("Enter Height (in cm):")))
    Height_m=Height/100
    BMI=(Weight/(Height_m**2))
    if BMI<18.5:
        print("Underweight")
    elif BMI<25.0:
        print("Normal weight")
    elif BMI<30.0:
        print("Increased weight")
    elif BMI<40.0 :
        print("Obese")
    elif BMI>=40.0:
        print("Very high obese")
main()
