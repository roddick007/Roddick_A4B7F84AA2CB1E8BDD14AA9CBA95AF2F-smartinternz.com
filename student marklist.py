
name = input("Enter your name: ")
tam = int(input("Enter marks for Tamil: "))
eng = int(input("Enter marks for English: "))
mat = int(input("Enter marks for Math: "))
scp = int(input("Enter marks for Science: "))
soc = int(input("Enter marks for Social Science: "))

total = tam + eng + mat + scp + soc
print("Total marks:", total)

percentage = total / 5
print("Percentage is:", percentage)

if percentage >= 80:
    print("Grade: A")
elif percentage >= 70 and percentage < 80:
    print("Grade: B")
elif percentage >= 60 and percentage < 70:
    print("Grade: C")
elif percentage >= 50 and percentage < 60:
    print("Grade: D")
else:
    print("Grade: F")
