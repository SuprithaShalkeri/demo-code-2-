import cv2


def viewImage(img, name_of_window):
  cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
  cv2.imshow(name_of_window, img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


#Crop an image
crop = img[10:500, 500:2000]
viewImage(crop, "Cropped Image")
#Resize an image
scaling = 20
#Change Width and Height
width = int(img.shape[1] * scaling / 100)
height = int(img.shape[0] * scaling / 100)
dim = (width, height)
resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
viewImage(resize, "Resized Image by 20%")
#Convert the image into grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
viewImage(gray_img, "Grayscale Image")
