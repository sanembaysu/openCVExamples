import cv2

img = cv2.imread('lena.jpg', -1)
#  1 loads a color image
#  0 loads image in grayscale mode
# -1 loads image as such including alpha channel

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
