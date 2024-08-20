import cv2
import numpy as np

# Đọc ảnh xám
image_path = 'b4.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Tạo mặt nạ cho các vùng trắng và đen
# Vùng trắng: giá trị pixel lớn hơn 127
# Vùng đen: giá trị pixel nhỏ hơn hoặc bằng 127
_, white_mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)


# Tạo ảnh trắng và đen từ mặt nạ
white_image = cv2.bitwise_and(image, image, mask=white_mask)

# Hiển thị ảnh
cv2.imshow('Original Image', image)
cv2.imshow('White Image', white_image)
cv2.waitKey(0)  # Chờ nhấn phím
cv2.destroyAllWindows()

# Lưu ảnh
cv2.imwrite('white_image.jpg', white_image)


print("Ảnh đã được lưu tại white_image.jpg và black_image.jpg")
