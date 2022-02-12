import cv2
def negative(to_convert_image):
    img = cv2.imread(to_convert_image, 0)
    img = 255 - img
    cv2.imwrite('negative_bozu.png', img)
    cv2.imshow('Negative Bozu', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def grayify(to_convert_image):
    pass

def reddify(to_convert_image):
    pass


def greenify(to_convert_image):
    pass


def blueify(to_convert_image):
    pass


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
