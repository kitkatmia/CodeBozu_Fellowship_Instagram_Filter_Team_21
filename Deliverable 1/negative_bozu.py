import cv2

# Write Negative Bozu function here
# Function to convert image Bozu.png to negative Bozu.png
def negative(to_convert_image):
    img = cv2.imread(to_convert_image, 0)
    img = 255 - img
    cv2.imwrite('negative_bozu.png', img)
    cv2.imshow('Negative Bozu', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
       

if __name__ == '__main__':
    negative('Bozu.png')
