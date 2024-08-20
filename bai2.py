import cv2

# Đọc ảnh ở chế độ grayscale (nếu ảnh đã là ảnh trắng đen)
image_path = 'b2.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
reverse_image = 255 - image

   # Lưu ảnh
output_path = 'reverse_image.jpg'
cv2.imwrite(output_path, reverse_image)

cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', reverse_image)
cv2.waitKey(0)

