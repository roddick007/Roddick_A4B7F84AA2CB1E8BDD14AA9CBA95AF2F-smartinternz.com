def area_of_rectangle(length, width):
    return length * width

def area_of_square(side):
    return side * side

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return 3.14 * radius * radius

print("Choose a shape to calculate its area:")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Circle")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is:", area_of_rectangle(length, width))

elif choice == '2':
    side = int(input("Enter the side of the square: "))
    print("The area of the square is:", area_of_square(side))

elif choice == '3':
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    print("The area of the triangle is:", area_of_triangle(base, height))

elif choice == '4':
    radius = int(input("Enter the radius of the circle: "))
    print("The area of the circle is:", area_of_circle(radius))

else:
    print("Invalid choice. Please enter a number between 1 and 4.")
