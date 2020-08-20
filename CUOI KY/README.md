Mô tả bài toán:
  1. Input: Đầu vào là một bức ảnh có kích thước bất kỳ chụp một khu vực có hoặc không xuất hiện voi.
  2. Output: Status dự đoán trong ảnh có xuất hiện voi hay không.
  
Mô tả dữ liệu: Các dữ liệu sử dụng cho bài toàn đều được tự thu thập.

       1.Nhãn 1: Là những bức hình chụp nương rẫy không xuất hiện voi. Với số lượng 1927 tấm.
  
       2.Nhãn 2: Là những bức ảnh chụp voi từ phía bên hông chúng dưới ánh sáng mặt trời, với kích thước 140x110 px, số lượng 1000 tấm.
  
Bài toán sử dụng HOG để rút trích đặc trưng và sử dụng SVM là thuật toán cho model.
