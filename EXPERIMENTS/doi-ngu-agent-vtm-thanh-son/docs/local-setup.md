# Máy đích và kết nối — bước tiếp theo

Trạng thái: BLOCKED_TARGET_ACCESS. Chưa kết nối máy cá nhân người dùng. Không được coi máy Linux của phiên chat là máy người dùng.

## Đã chuẩn bị
machine_check.py chỉ kiểm tra hệ điều hành, kiến trúc, RAM (Linux/Windows), sự hiện diện và phiên bản các lệnh phổ biến. Không đọc auth/config/env, không cài phần mềm, không gọi model, không gửi mạng, không xác minh đăng nhập. Có chạy lệnh --version của ứng dụng đã có; shim cmd/bat/ps1 chỉ ghi nhận sự hiện diện. GPU chưa kiểm tra.

Chạy trên máy đích bằng Python 3.10+:

    python machine_check.py --output machine-report.json

Không ghi đè file hiện có. Không đưa báo cáo máy khách lên kho public; gửi trực tiếp khi cần. Kết quả này không tự xác minh rằng máy thuộc người dùng.

## Khi đã có quyền thao tác máy
1. Xác nhận máy đích, OS/RAM/GPU và các ứng dụng.
2. Kiểm tra Codex CLI/app và Gemini CLI bằng bản chính thức; xác định phiên bản tương thích trước khi cài. Không tự lấy token từ ứng dụng chat hoặc tái sử dụng auth ngoài cách hãng hỗ trợ.
3. Đăng nhập bằng luồng hãng; người dùng thực hiện bước xác thực khi cần. Không gửi mật khẩu/token vào chat. Chưa đăng nhập hoặc hết hạn mức thì BLOCKED, không giả lập câu trả lời của model khác.
4. Test read-only từng kết nối: yêu cầu trả một chuỗi định danh thử, lưu stdout/exit code đã lọc thông tin nhạy cảm và kiểm tra nguồn phiên thực thi.
5. Chạy một ảnh nguồn có quyền sử dụng, nhận caption Gemini, xử lý ảnh bằng công cụ đã chọn và kiểm định thật. Không tự dùng ảnh màn hình TikTok của cuộc chat làm ảnh khách.
6. Chỉ sau bộ thử nội bộ mới nối Page và publisher, mặc định vẫn tắt lịch/đăng.

## Nguồn tài liệu đã kiểm tra
- https://learn.chatgpt.com/docs/codex/cli
- https://geminicli.com/docs/get-started/installation/
- https://geminicli.com/docs/get-started/authentication/

Thuê bao chat không được mặc định cấp API cho mọi adapter. Cần xác minh quyền thực tế trong phiên đăng nhập. Chưa có kết nối tự động nào được thiết lập.
