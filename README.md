# 🚦 Driving License Eligibility Program

This is a simple **Python program** that checks whether a person is eligible for a driving license based on marital status, gender, and age.

---

## 📝 Problem Statement
Write a Python program to check eligibility for a driving license:
1. If the person is **married**, they are directly eligible for a driving license.  
2. If the person is **unmarried**:
   - If the person is a **boy** and his age is **18 or above**, he is eligible.  
   - If the person is a **girl** and her age is **23 or above**, she is eligible.  
   - Otherwise, the person is **not eligible**.

---

## 💻 Code
```python
user = input("Enter married or unmarried: ").lower()

if user == "married":
    print("Yes, Married")
    print("Driving license is issued")
else:
    gender = input("Enter your gender (boy/girl): ").lower()
    age = int(input("Enter your age: "))

    if (gender == "boy" and age >= 18) or (gender == "girl" and age >= 23):
        print("Driving license is issued")
    else:
        print("The person is not eligible for a driving license")
