# Báo cáo bản nền v0.1.0

Ngày: 2026-11-11. Phương thức review: các lượt xử lý trong cùng assistant, không phải các AI độc lập.

## Kiểm tra thực hiện
- python -m unittest discover -s EXPERIMENTS/doi-ngu-agent-vtm-thanh-son -p 'test_*.py' -v: 14 test PASS; các packet là fixture mô phỏng.
- python TOOLS/validate_registry.py: PASS, 8 entry hiện hành.
- env PYTHONPATH=TOOLS python -m unittest discover -s TESTS -p 'test_*.py' -v: 35 test PASS. Đây là bộ discover cấp TESTS, không bao gồm mọi kiểm thử trong thư mục con.
- Lần đầu chạy bộ cũ thiếu PYTHONPATH gây 2 import error. Đã chạy lại đúng môi trường và không sửa mã cũ.

## Review và sửa
- G1 Major: gates=null có thể gây exception thay vì trả lỗi danh sách. Đã sửa kiểm tra kiểu; test null_gates_fail_closed PASS.
- G2 Major: chưa ngăn cùng reviewer AI-QC và final. Đã thêm điều kiện; test same_qc_and_final_reviewer_blocks PASS. Nhãn reviewer không chứng minh danh tính thật, giới hạn ghi rõ trong README.
- G3 Major về diễn giải: dễ nhầm cấu trúc hợp lệ với quyền đăng. Kết quả luôn publish_allowed=false và tên STRUCTURALLY_VALID; README/contract ghi rõ không xác minh nội dung hoặc nguồn attest. Chưa triển khai publisher.

## Phạm vi nghiệm thu
Bản nền offline: code và tài liệu được kiểm tra, không đổi CORE/Registry/SKILLS; không thêm skill auto-load. Evidence của test không dùng để phê duyệt ảnh/bài thật.
Hệ thống đầy đủ: BLOCKED — chưa kiểm tra máy người dùng, chưa xác nhận model/OAuth/API, chưa adapter Hermes/Codex/Gemini, chưa lưu trạng thái chống đăng trùng, chưa công cụ ảnh và kết nối Page, chưa thử sản phẩm thật hoặc lịch nền.
Không chấm điểm hoặc tuyên bố PASS cho hệ thống chưa triển khai.

## Cách ly
Validator hiện tại chỉ đọc đường dẫn Registry. Các nguồn nạp skill của công cụ ngoài có thể khác: phải exclude EXPERIMENTS khi cấu hình runtime. Không suy ra tất cả môi trường đều cách ly chỉ từ validator này.
