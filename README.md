# Giới thiệu bài toán 
## Tóm tắt bài toán
Bài toán lớn là truy xuất thông tin pháp lý (Retrieval Case-Law) từ bộ dữ liệu gồm
10000 bản án hình sự và 1122 điều luật từ bộ luật Hình sự Việt Nam.

Mục tiêu của đề tài là triển khai các mô hình cơ sở bao gồm TF-IDF, BM25 và BERT
nhằm truy xuất và liệt kê các điều luật được đề cập trong mỗi bản án, dựa trên tập dữ liệu
đã được gán nhãn thủ công làm chuẩn. Kết quả của các mô hình sẽ được đánh giá thông
qua các chỉ số như precision, recall, F1 và MAP. Những kết quả này đóng vai trò baseline
cho việc so sánh và phát triển các phương pháp nâng cao trong tương lai.

## Bài toán được chia thành hai nhóm công việc chính:

- Nhóm công việc thứ nhất là xây dựng bộ dữ liệu gán nhãn, vì bộ dữ liệu rất lớn (10000
bản án) nên được thực hiện theo nhóm để tối ưu thời gian và đảm bảo tạo bộ dữ liệu
gán nhãn chất lượng, chính xác.

- Nhóm công việc thứ hai được thực hiện cá nhân là tiền xử lý dữ liệu, xây dựng mô hình học máy cơ bản
và đánh giá.


# Cài đặt bộ dữ liệu và môi trường thực nghiệm

## Bộ dữ liệu

### 1. Import bộ dữ liệu

- Import file `dataset_10k.sql` vào **MySQL Workbench**.
- Nếu sử dụng **Google Colab**, chuyển các bảng trong cơ sở dữ liệu sang định dạng **JSON** để thuận tiện cho việc import và xử lý dữ liệu.

### 2. Cấu trúc dữ liệu

| Bảng | Mô tả |
|------|------|
| `case` | Chứa **10.000 bản án**, trong đó cột `text` lưu toàn bộ nội dung của bản án. |
| `law` | Chứa **1.122 điều luật** thuộc ba bộ luật chính: Bộ luật Hình sự, Bộ luật Tố tụng Hình sự và Luật Thi hành án Hình sự. |
| `case_law` | Lưu mối quan hệ giữa các bản án và các điều luật được trích xuất tương ứng. |

---

# Môi trường cài đặt

## Ngôn ngữ lập trình

- Python

## Môi trường thực nghiệm

- Google Colab (Jupyter Notebook)
- Khuyến nghị sử dụng **GPU Runtime** để tối ưu thời gian huấn luyện và thực nghiệm.

## Thư viện sử dụng

Dự án sử dụng các thư viện Python phục vụ cho:

- Tiền xử lý dữ liệu
- Xây dựng mô hình
- Huấn luyện mô hình
- Đánh giá mô hình
- Trực quan hóa kết quả

---

# Quy trình thực nghiệm

## Bước 1. Tiền xử lý dữ liệu

- Đọc dữ liệu từ các nguồn:
  - File CSV
  - File JSON
  - Cơ sở dữ liệu MySQL
- Thực hiện tiền xử lý văn bản:
  - Loại bỏ ký tự đặc biệt
  - Chuẩn hóa chữ thường
  - Làm sạch văn bản

---

## Bước 2. Xây dựng và huấn luyện mô hình

- Tạo tập **ground truth** từ dữ liệu đã được gán nhãn.
- Huấn luyện các mô hình:
  - TF-IDF
  - BM25
  - BERT

---

## Bước 3. Tạo tập dự đoán và đánh giá

- Sử dụng các mô hình đã huấn luyện để tạo tập dự đoán (**predictions**) trên tập kiểm thử.
- Đánh giá hiệu suất của từng mô hình dựa trên các chỉ số:
  - Precision
  - Recall
  - F1-score
  - Mean Average Precision (MAP)
- Trực quan hóa và so sánh kết quả bằng thư viện **Matplotlib**.

# Kết quả đánh giá 

## Kết quả TF IDF 
<img width="838" height="652" alt="image" src="https://github.com/user-attachments/assets/e28e1799-6289-456e-903c-bf6802dad1ba" />

## Kết quả BM25
<img width="856" height="648" alt="image" src="https://github.com/user-attachments/assets/fc37db4e-9bcd-44fa-ac33-85194096eb0d" />

## Kết quả Bert
<img width="864" height="726" alt="image" src="https://github.com/user-attachments/assets/d5fc6c28-dd9c-42b7-9e03-32ae6d450346" />
