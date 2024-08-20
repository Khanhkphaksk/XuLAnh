import cv2
import numpy as np

# Đọc ảnh trắng đen từ file
image1 = cv2.imread('h81.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('h82.png', cv2.IMREAD_GRAYSCALE)

# Kiểm tra xem ảnh có được đọc thành công không

# Chuyển đổi ảnh trắng đen thành ma trận số (NumPy array)
matrix1 = np.array(image1)
matrix2 = np.array(image2)

# In ra ma trận để kiểm tra (tuỳ chọn)
print("Ma trận số:")
print(matrix1)
print(matrix2)


matrix = matrix2 - matrix1

# Lấy giá trị tuyệt đối của kết quả phép trừ
matrix3 = np.abs(matrix)

cv2.imshow('Ảnh Trắng Đen', matrix)

# Lưu ảnh trắng đen ra file
cv2.imwrite('bimat.png', matrix)

# Đợi người dùng nhấn phím để đóng cửa sổ ảnh
cv2.waitKey(0)
cv2.destroyAllWindows()