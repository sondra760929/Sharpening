# load the required packages
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# bright_ratio = 1.4
# color_ratio = 0.3

# image0 = Image.open('d:/green.jpg')

# bright_color = ImageEnhance.Brightness(image0)
# color_output = bright_color.enhance(bright_ratio)

# change_color = ImageEnhance.Color(color_output)
# color_output = change_color.enhance(color_ratio)
# color_output.save("d:/color_result.jpg")

# for color_i in range(10):
#     color_output = change_color.enhance(0.1*color_i)
#     color_output.save("d:/color_c{}.jpg".format(str(color_i)))
    
# for color_i in range(10):
#     color_output = bright_color.enhance(1 + 0.1*color_i)
#     color_output.save("d:/color_b{}.jpg".format(str(color_i)))

# image0 = image0.convert("RGB")
# width, height = image0.size

# for x in range(width):
#     for y in range(height):
#         r, g, b = image0.getpixel((x, y))
#         if g > (r+10) and g > (b+10):
#             g = min(255, int(g*3))
#             r = g
#             b = g
#             # g = int(g*0.5)
#             image0.putpixel((x, y), (r, g, b))

# image0.save('d:/green_50.jpg')

# load the image into system memory
image = cv2.imread('d:/origin.jpg', flags=cv2.IMREAD_COLOR)

# display the image to the screen
# cv2.imshow('AV CV- Winter Wonder', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

kernel = np.array([[0, -0.1, 0],
                   [-0.1, 1.4,-0.1],
                   [0, -0.1, 0]])
# kernel = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])
# kernel = np.array([[-1, -1, -1],
#                    [-1, 9,-1],
#                    [-1, -1, -1]])
for i in range(10):
    param = -0.1*(i+1)
    param1 = 1 - (param*4)
    kernel = np.array([[0, param, 0],
                    [param, param1,param],
                    [0, param, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    cv2.imwrite("d:/origin_{}.jpg".format(str(i)), image_sharp)
