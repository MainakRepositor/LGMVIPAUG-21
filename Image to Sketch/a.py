###################################################
#   LGM-VIP AUGUST 21 (DATA SCIENCE INTERNSHIP)   #
#          CODE BY : MAINAK CHAUHDHURI            #
#          DATE    : 25.07.2021                   #
###################################################

#importing the opencv package
import cv2      

#reading the image file 
img_rgb = cv2.imread("image.jpg")

#colour image to grey
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)   

#inverting grey image
img_gray_inv = 255 - img_gray  

#applying Gaussian Blue 
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),sigmaX=0, sigmaY=0)

#applying dodge
def dodgeV2(image, mask):
  return (cv2.divide(image, 255-mask, scale=256))

#applying burn
def burnV2(image, mask):
  return (255 - cv2.divide(255-image, 255-mask, scale=256))

#blending to generate the sketch
img_blend = dodgeV2(img_gray, img_blur)

#displaying the sketch
cv2.imwrite('result.jpg',img_blend)



#### Completed Task 4!


