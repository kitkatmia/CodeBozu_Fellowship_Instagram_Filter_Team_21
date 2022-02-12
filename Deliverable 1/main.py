from red_green_blue_bozu import *
from negative_bozu import *
from grayscale_bozu import *

to_convert_image = 'Bozu.png'

print("Team 21 Deliverable 1")
choice = input("Enter 1 to Reddify Bozu\n2 to Greenify Bozu\n3 to Blueify Bozu\n4 to convert Bozu to Grayscale\n5 to get negative image of Bozu\n6 to exit\nYour choice: ")

while choice != '6':
    if choice == "1":
        reddify(to_convert_image)
    elif choice == "2":
        greenify(to_convert_image)
    elif choice == "3":
        blueify(to_convert_image)
    elif choice == "4":
        grayify(to_convert_image)
    elif choice == "5":
        negative(to_convert_image)
    choice = input("Enter 1 to Reddify Bozu\n2 to Greenify Bozu\n3 to Blueify Bozu\n4 to convert Bozu to Grayscale\n5 to get negative image of Bozu\n6 to exit\nYour choice: ")

print("Thank you for using our program!")
