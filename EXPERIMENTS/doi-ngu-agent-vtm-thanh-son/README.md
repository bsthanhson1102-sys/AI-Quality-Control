# Đội ngũ Agent VTM Thanh Sơn — thử nghiệm v0.1.0

**Trạng thái: bản nền offline. Chưa có đội AI tự động đang chạy.**

## Phạm vi đã thực hiện
- Hợp đồng vai trò ChatGPT CEO, Codex vận hành/kỹ thuật, Gemini biên tập, AI-QC riêng, kiểm soát cuối riêng. Claude/Ollama phụ trợ.
- Chọn Hermes Agent làm khung tham chiếu cho bộ nhớ, lịch và ủy nhiệm; pin commit trong config/project.json. Mã nguồn đầy đủ đã tải riêng; trong kho này chỉ giữ tham chiếu và LICENSE, không nạp runtime hoặc skill Hermes.
- Cổng kiểm tra gói bàn giao offline: file và evidence phải tồn tại trong thư mục nhiệm vụ, khớp SHA-256, đủ bước và phê duyệt đúng phiên bản; 7 trọng số, >=90, không Critical/Major chưa sửa, 1–4 vòng.
- Publisher luôn tắt. Không có API hay cơ chế tự đăng, tự like hoặc trả lời bình luận.

## Tách biệt
Không thay CORE, Registry, SKILLS, hướng dẫn gốc hay workflow CI. Không tạo file tên SKILL.md hoặc AGENTS.md ở vùng thử. Không cài personal skills, hooks, profile hoặc scheduler. Bộ validator cũ chỉ đọc path trong Registry. Công cụ bên ngoài quét đệ quy vẫn cần cấu hình exclude EXPERIMENTS trước khi cài vào máy.

## Chạy kiểm thử (Python 3.10+)
Tại thư mục gốc kho:

    python -m unittest discover -s EXPERIMENTS/doi-ngu-agent-vtm-thanh-son -p 'test_*.py' -v

Kiểm tra gói nhiệm vụ đã được các reviewer tạo:

    python EXPERIMENTS/doi-ngu-agent-vtm-thanh-son/handoff_gate.py /path/to/task/packet.json

Exit 0 = STRUCTURALLY_VALID, **không phải AI-QC PASS hoặc quyền đăng bài**. Exit 1 = BLOCKED. Fixture hợp lệ trong test là dữ liệu mô phỏng; không được dùng làm bằng chứng sản phẩm thật.

## Luồng mục tiêu
Brief -> Codex phân việc -> Gemini/công cụ ảnh sản xuất -> kiểm thử -> Critic -> Editor -> Re-check -> AI-QC -> kiểm soát cuối -> publisher -> đọc lại bài.

## Skill hiện có
content-master cho bài; image-master cho ảnh; research-master khi xác minh nguồn cần thiết; coding-master cho code; video-master khi làm video; academic-master khi phù hợp học thuật. Đọc registry active mới nhất lúc nhận việc, chốt commit, lưu trạng thái SELECTED/LOADED/APPLIED/VERIFIED và evidence. Không tự thêm draft, không tự tải/chạy skill ngoài. Chưa có adapter tự lấy và áp dụng các skill này trong bản v0.1.

## Lưu trữ
Mặc định tương lai: mỗi nhiệm vụ một thư mục cục bộ gồm ảnh gốc, ảnh xuất, caption và bằng chứng. Google Drive tùy chọn sau khi có quyền. Không lưu ảnh khách, tokens, mật khẩu hay logs có dữ liệu cá nhân vào kho public.

## Thứ tự phát triển
1. Xác định OS, RAM/GPU, loại Claude, model Ollama và phương thức đăng nhập/kết nối Codex/Gemini hỗ trợ.
2. Tích hợp runtime Hermes với một model và kiểm tra nhiệm vụ read-only; không mặc định có quyền API từ thuê bao chat.
3. Một ảnh đã có quyền -> chỉnh theo mẫu -> caption -> hồ sơ kiểm định thật.
4. Nối publisher trên Page thử; idempotency theo task ID và hash, xác minh URL bài; xử lý phản hồi không rõ trạng thái trước retry để tránh đăng trùng.
5. Bình luận mẫu, rồi mới đọc/trả lời thật trong phạm vi đã cho phép; ca y khoa, khiếu nại chuyển người.
6. Bật lịch khi kiểm thử restart, chống trùng, giới hạn chi phí, dừng khẩn và nhật ký đã đạt.

## Giới hạn cổng offline
Chỉ kiểm tra cấu trúc và tính toàn vẹn byte. Người sửa được packet có thể tự ghi reviewer, điểm và verdict; chưa có xác thực danh tính, chữ ký, chứng minh nguồn hoặc kiểm tra ngữ nghĩa. Các adapter tin cậy và reviewer thật phải xử lý trước khi bất kỳ publisher nào dùng kết quả này. Không được bỏ cờ publish_allowed=False để coi đây là hệ thống production.
