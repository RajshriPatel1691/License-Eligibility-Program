User = input("Enter the married and unmarried:")
if(User.lower() == "married"):
    print("Yes,Married")
    print("Driving license is issued")
else:
    gender = input("Enter the Boy and Girl:").lower()
    age = int(input("Enter the age:"))

    if(gender == "boy" and age>=18 ):
        print("Driving license is issued")

    elif(gender == "girl" and age>=25):
        print("Driving license is issued")

    else:
        print("The person is not eligible for a driving license")