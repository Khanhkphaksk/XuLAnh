import numpy as np
import cv2
# Kích thước của ma trận
rows, cols = 350, 280

# Tạo ma trận với tất cả các giá trị là 255
matrix = np.full((rows, cols), 0, dtype=np.uint8)

# Cập nhật phần ma trận từ hàng thứ 0 đến hàng thứ 279 và từ cột thứ 0 đến cột thứ 189 với giá trị 0
matrix[:36, 190:280] = 255
matrix[70:140, 85:191] = 255
matrix[158:193, 190:280] = 255
matrix[210:280, 85:191] = 255
matrix[313:350, 190:280] = 255


# In ra ma trận để kiểm tra (tuỳ chọn)
print(matrix)

# Hoặc, nếu bạn muốn kiểm tra kích thước của ma trận
print(f"Ma trận có kích thước: {matrix.shape}")
cv2.imshow('Ảnh Trắng Đen', matrix)

# Lưu ảnh trắng đen ra file
cv2.imwrite('image_chub.png', matrix)

# Đợi người dùng nhấn phím để đóng cửa sổ ảnh
cv2.waitKey(0)
cv2.destroyAllWindows()