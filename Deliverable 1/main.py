from red_green_blue_bozu import *
from negative_bozu import *
from grayscale_bozu import *

print("Team 21 Deliverable 1")
choice = input("Enter 1 to reddify, 2 to greenify, 3 to blueify, 4 to grayscale, 5 to negative, 6 to exit: ")
if choice == "1":
    reddify()
elif choice == "2":
    greenify()
elif choice == "3":
    blueify()
elif choice == "4":
    grayscale()
elif choice == "5":
    negative()
elif choice == "6":
    print("Goodbye!")
