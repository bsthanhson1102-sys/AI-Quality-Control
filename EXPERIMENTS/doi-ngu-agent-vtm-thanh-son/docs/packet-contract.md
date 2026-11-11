# Hợp đồng packet v0.1

Tất cả đường dẫn tương đối so với thư mục chứa packet.json; không symlink ra ngoài. Không thực thi file evidence.

- task_id: chuỗi không rỗng; round: số nguyên 1..4.
- ai_qc_commit: SHA commit 40 ký tự hex. Validator chỉ kiểm tra hình thức; adapter tương lai phải xác minh commit, Registry và nội dung skill thật.
- artifacts: danh sách {path, sha256} không rỗng, không trùng.
- stages: brief, production, technical, critic, editor, recheck, ai_qc, final. Mỗi bước có status=completed, reviewer và evidence=[{path, sha256}]. Editor không sửa vẫn cần evidence nêu lý do.
- technical/recheck/ai_qc/final: verdict=approved, artifact_hashes phải đúng toàn bộ gói hiện tại.
- reviewer production khác ai_qc và final; final khác ai_qc. Đây là nhãn vai trò, chưa chứng minh tiến trình hay mô hình độc lập.
- gates: technical/domain/regression đều verified, có evidence tương ứng trong hồ sơ.
- scores: 7 điểm theo 25/20/15/15/10/10/5, tổng >=90. Người chấm phải ghi lý do trong evidence; validator không tự chấm.
- findings: danh sách severity Critical/Major/Minor/Enhancement. Critical/Major chỉ chấp nhận resolution=verified_fixed; evidence phải được reviewer tin cậy xác minh.

Kết quả STRUCTURALLY_VALID vẫn publish_allowed=false. Chưa có publisher, chữ ký hay nguồn attest tin cậy.
