# Kiểm tra công cụ chẩn đoán máy

Ngày 2026-11-11. 19 unit tests (14 gate + 5 diagnostic) PASS trong môi trường assistant. Bộ test version có fixture giả lập; không gọi các hãng AI.
Smoke test machine_check.py chạy trên môi trường assistant, không phải máy khách. Không lưu thông số môi trường này thành hồ sơ phần cứng khách.
Windows/macOS và GPU: chưa kiểm thử thực tế. Đăng nhập, model call, ảnh -> bài, Drive và Facebook: NOT RUN.
Không cài hay điều khiển máy cá nhân; không có kết nối máy đích. Đây là trở ngại truy cập, không phải yêu cầu xin lại quyền đã được người dùng cấp.
