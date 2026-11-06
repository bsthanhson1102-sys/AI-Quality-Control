# T04 — Academic Master: Mô cơ và mô thần kinh

- **Test ID:** T04
- **Runtime:** ChatGPT, with GitHub repository access and the user-supplied PDF attached in the conversation
- **Test date:** 2026-11-06
- **Primary skill:** `academic-master` v1.0.0 (active)
- **Secondary skill:** none; no external research was requested
- **Routing rationale:** the deliverable is a structured academic report based on supplied course material.
- **Registry:** `REGISTRY/skills-registry.yml`, branch `main`, version `1.0.0`, blob SHA `e38086d765fae7e0895ae95bf777da23de146315`
- **Skill file:** `SKILLS/academic-master/SKILL.md`, registered version `1.0.0`, status `active`, blob SHA `b76cb272b4fa06bd8917b3982e14afbb7589e87f`
- **CORE:** `CORE/quality-control.md`, blob SHA `6b1de5d165912344d9f096d48c1fc81196cb1274`
- **Test specification:** `TESTS/skill-routing-test-suite.md`, blob SHA `b9ddf3fd7d701efd9046dc9f788bdadcfba5e109`

## 1. Source material and scope

The user supplied **“TRANG _ CƠ-THẦN KINH_ TÓM TẮT.pdf”**, a 4-page study summary titled “BUỔI 2: TÓM TẮT ÔN BÀI – MÔ CƠ & MÔ THẦN KINH”.

- Source type: user-provided course/study summary PDF.
- Pages inspected: all 4 pages, including the overview diagram on page 1 and the tables/mnemonics on pages 2–4.
- PDF SHA-256: `fc60a5f381b9b5a4916b700be61da20e173a6ef58ad4f5abce56591c8b8d38fc`.
- Author, institution, textbook bibliography and publication details: not stated in the supplied PDF.
- No external sources were used. Statements below are attributed to the supplied summary, not represented as independently verified histology facts.

## 2. Intake and acceptance criteria

The test prompt requires a structured academic report based on supplied source material. The following criteria were set before drafting:

1. Preserve the source's terminology, main organization and key relationships.
2. Cover both tissue groups: muscle tissue and nervous tissue.
3. Retain important classifications, structures, mechanisms and comparison points.
4. Distinguish what the source states from gaps or ambiguities in the source.
5. Do not invent citations, textbook details, page references, data or institutional formatting requirements.
6. Keep the report readable and logically structured.
7. Critique, edit, re-check and conduct a final audit against the test prompt.

## 3. Created artifact — Structured academic report

# Mô cơ và mô thần kinh

## 3.1. Mô cơ

### 3.1.1. Đặc điểm chung và nguồn gốc

Theo tài liệu ôn tập, bộ máy co cơ gồm actin (mảnh) và myosin (dày) trượt lên nhau. Phần lớn mô cơ có nguồn gốc trung bì. Tài liệu nêu các ngoại lệ có nguồn gốc ngoại bì gồm cơ–biểu mô, cơ dựng lông và cơ co đồng tử.

### 3.1.2. Cấu tạo cơ vân

Cấu trúc được trình bày theo thứ tự: bắp cơ → bó cơ → sợi cơ (hợp bào) → tơ cơ → xơ cơ. Các lớp bao liên kết gồm ngoại cơ, quanh cơ và nội cơ. Bên trong sợi cơ có lưới cơ tương (kho Ca²⁺), ống T, bộ ba và ty thể.

Ở mức sarcomere, các cấu trúc/băng được tóm tắt như sau:

- Vạch Z: nơi neo actin.
- Băng I: vùng sáng, chỉ có actin.
- Băng A: vùng tối, có myosin và phần actin lồng vào.
- Vùng H: chỉ có myosin.
- Vạch M: nằm ở giữa.
- Sarcomere: đoạn nằm giữa hai vạch Z.

### 3.1.3. Cơ chế co và giãn cơ

Tài liệu mô tả chuỗi co cơ: acetylcholine (ACh) → ống T → Ca²⁺ được giải phóng → Ca²⁺ gắn với TnC → vị trí gắn được bộc lộ → myosin sử dụng ATP để kéo actin. Khi co, hai vạch Z tiến lại gần; băng I và vùng H ngắn lại; băng A không đổi. Khi Ca²⁺ trở về lưới cơ tương, cơ giãn.

### 3.1.4. Ba loại mô cơ

| Đặc điểm | Cơ vân | Cơ tim | Cơ trơn |
|---|---|---|---|
| Hình dạng | Trụ dài, hợp bào | Trụ, phân nhánh | Hình thoi |
| Nhân | Nhiều, sát rìa | 1–2, ở giữa | 1, ở giữa |
| Vân ngang | Có | Có | Không |
| Điều khiển | Theo ý muốn | Không theo ý muốn | Không theo ý muốn |
| Đặc điểm co | Nhanh, mạnh, chóng mỏi | Nhịp nhàng, tự động, lâu mỏi | Chậm, dẻo dai, lâu mỏi |
| Liên hệ tế bào | Độc lập | Đĩa nối | Liên kết khe |
| Ống T | Bộ ba (triad) | Bộ đôi (dyad) | Không nêu |
| Điều hòa Ca²⁺ | Troponin | Troponin | Calmodulin |

**Cơ tim:** tế bào phân nhánh, có 1–2 nhân ở giữa và bộ đôi (dyad). Đĩa nối có phần ngang (màng dính và thể nối) giúp giữ tế bào; phần dọc (liên kết khe) giúp thông điện.

**Cơ trơn:** tế bào hình thoi, một nhân ở giữa, không có sarcomere và không có troponin. Tài liệu nêu cơ chế Ca²⁺–calmodulin → MLCK; thể đặc có vai trò tương tự vạch Z.

### 3.1.5. Sửa chữa và tái sinh

Theo bảng tóm tắt, cơ vân có tế bào vệ tinh tham gia sửa chữa; cơ tim sau hoại tử được thay bằng mô sợi; cơ trơn còn khả năng phân bào và phì đại. Tài liệu ghi chú rằng hai giáo trình được tham khảo có điểm hơi khác nhau về cơ tim, nhưng không nêu tên giáo trình hoặc nội dung khác biệt cụ thể.

## 3.2. Mô thần kinh

### 3.2.1. Thành phần và nguồn gốc

Mô thần kinh gồm neuron và tế bào đệm (neuroglia). Neuron đảm nhiệm hoạt động nghĩ, quyết định và dẫn truyền; tế bào đệm có vai trò nâng đỡ và nuôi dưỡng. Theo tài liệu, ống thần kinh phát triển thành hệ thần kinh trung ương, mào thần kinh góp phần tạo hệ thần kinh ngoại biên; vi bào đệm là ngoại lệ có nguồn gốc trung bì.

### 3.2.2. Phân chia hệ thần kinh

- **Hệ thần kinh trung ương:** não và tủy sống.
- **Hệ thần kinh ngoại biên:** 12 đôi dây thần kinh sọ, 31 đôi dây thần kinh sống và hệ thần kinh thực vật.
- **Hệ thần kinh thực vật:** tài liệu ghi giao cảm làm tăng và phó giao cảm làm giảm hoạt động, góp phần duy trì cân bằng.

### 3.2.3. Neuron: cấu tạo, phân loại và khả năng phân chia

Neuron được mô tả gồm: nhiều nhánh (hướng tâm, dẫn truyền thông tin vào) → thân neuron (xử lý; có thể Nissl; thiếu trung thể) → gò sợi trục → một sợi trục (dẫn truyền ly tâm) → cúc tận cùng.

Phân loại hình thái gồm neuron đa cực (phổ biến), hai cực (võng mạc, khứu giác) và giả đơn cực (hạch gai). Phân loại chức năng gồm neuron cảm giác, vận động và trung gian.

Tài liệu nêu neuron ở pha G0, thiếu trung thể nên không phân chia; số lượng neuron vì vậy chỉ giảm và rất hiếm sinh u (không diễn đạt thành “không bao giờ”). Tài liệu liên hệ học tập với việc tạo liên kết mới. Tế bào đệm vẫn có thể phân chia và có thể sinh u.

### 3.2.4. Bao myelin và dẫn truyền

Bao myelin là lớp lipoprotein có tác dụng cách điện. Xung thần kinh dẫn truyền kiểu nhảy cóc qua eo Ranvier, nhanh hơn sợi trần khoảng hàng chục đến hàng trăm lần theo tài liệu. Tốc độ của sợi không myelin được ghi khoảng 1 m/s. Ở hệ thần kinh trung ương, một tế bào ít nhánh có thể tạo myelin cho nhiều sợi; ở ngoại biên, tế bào Schwann bọc một đoạn của một sợi trục.

### 3.2.5. Synapse

Synapse gồm màng trước synapse, khe synapse (20–30 nm) và màng sau synapse. Túi synapse giải phóng chất dẫn truyền thần kinh vào khe; chất dẫn truyền gắn với thụ thể ở phía sau synapse. Tài liệu phân loại synapse thành hóa học/điện và hưng phấn/ức chế. Synapse thần kinh–cơ sử dụng acetylcholine.

### 3.2.6. Dây thần kinh, chất xám, chất trắng và hàng rào máu–não

Dây thần kinh có các lớp/bó được ghi theo thứ tự ngoại thần kinh – bó thần kinh – nội thần kinh. Chất xám chứa thân neuron; chất trắng chứa các sợi có myelin. Tài liệu ghi tủy sống có chất xám ở trong, vỏ não có chất xám ở ngoài. Với hàng rào máu–não (BBB), tế bào nội mô giữ vai trò quyết định và chân tế bào sao hỗ trợ. Tài liệu cũng nêu sợi thần kinh ngoại biên có khả năng tái sinh từ phía thân neuron.

### 3.2.7. Sáu loại tế bào đệm

| Tế bào đệm | Vị trí | Vai trò/đặc điểm theo tài liệu |
|---|---|---|
| Tế bào sao (astrocyte) | Trung ương | Nâng đỡ, nuôi dưỡng; chân sao hỗ trợ BBB. Sao xơ ở chất trắng; sao nguyên sinh ở chất xám. |
| Tế bào ít nhánh (oligodendrocyte) | Trung ương | Tạo myelin, bọc nhiều sợi trục. |
| Vi bào đệm (microglia) | Trung ương | Thực bào; nguồn gốc trung bì (máu). |
| Biểu mô nội tủy (ependymal) | Trung ương | Lót não thất và ống tủy; tiết dịch não tủy. |
| Schwann | Ngoại biên | Tạo myelin, bọc một đoạn; có thể ôm vài sợi trong trường hợp sợi không myelin. |
| Tế bào vệ tinh (satellite) | Ngoại biên | Bao quanh thân neuron trong hạch. |

## 3.3. Tổng hợp các điểm ghi nhớ trong tài liệu

- **Mô cơ:** actin mảnh – myosin dày; dày thì tối, mỏng thì sáng; sarcomere nằm giữa hai vạch Z.
- **Co cơ:** ACh → Ca²⁺ → troponin → kéo actin; Z gần lại, I và H ngắn, A không đổi; Ca²⁺ trở về lưới cơ tương thì giãn.
- **Ba loại cơ:** vân nhiều nhân, tim 1–2 nhân, trơn một nhân; cơ tim có dyad, cơ vân có triad.
- **Mô thần kinh:** neuron tiếp nhận/xử lý/dẫn truyền; tế bào đệm nâng đỡ và nuôi dưỡng.
- **Nguồn gốc:** ống thần kinh → trung ương; mào thần kinh → ngoại biên; vi bào đệm là ngoại lệ nguồn gốc trung bì.
- **Tế bào đệm:** trung ương gồm sao, ít nhánh, vi bào đệm, nội tủy; ngoại biên gồm Schwann và vệ tinh.
- **Myelin:** giúp cách điện và dẫn truyền nhảy cóc qua eo Ranvier.
- **Synapse:** trước synapse → khe → sau synapse; chất dẫn truyền được phóng thích và gắn thụ thể.

## 4. Critic — đánh giá độc lập bản nháp

| Finding | Severity | Evidence/reason and impact | Required action |
|---|---|---|---|
| C-01 | Minor | Tài liệu không cung cấp tên tác giả, trường, giáo trình hoặc danh mục tham khảo; không thể lập trích dẫn thư mục đầy đủ. | Ghi rõ đây là tài liệu do người dùng cung cấp; không tự tạo thông tin thư mục. |
| C-02 | Minor | Cụm “RA” trong dòng mô tả sợi trục không được giải thích trong tài liệu. Tự mở rộng chữ viết tắt có thể làm sai ý nguồn. | Chỉ diễn giải chức năng dẫn truyền ly tâm theo nội dung rõ ràng; không tự định nghĩa “RA”. |
| C-03 | Minor | Ghi chú “2 giáo trình hơi khác nhau” về sửa chữa cơ tim không chỉ ra hai giáo trình hoặc điểm khác nhau. | Giữ nguyên sự tồn tại của ghi chú và công khai rằng không đủ dữ liệu để đối chiếu. |
| C-04 | Minor | Không có đề bài học phần, rubric, độ dài hay quy định trình bày của cơ sở đào tạo. | Không giả định mẫu báo cáo chính thức; dùng cấu trúc báo cáo học thuật phổ thông phù hợp với test. |
| C-05 | Enhancement | Nguồn là tài liệu ôn tập tóm tắt, không phải giáo trình đầy đủ. | Giới hạn kết luận trong phạm vi nội dung được cung cấp; không tuyên bố đã thẩm định độc lập tính đúng đắn chuyên môn. |

## 5. Editor — các điều chỉnh đã thực hiện

1. Chia nội dung thành hai phần lớn: mô cơ và mô thần kinh, giữ lại các tiểu mục tương ứng với cách tổ chức của tài liệu.
2. Chuyển bảng so sánh ba loại cơ và sáu loại tế bào đệm thành bảng để dễ đối chiếu.
3. Giữ nguyên các thuật ngữ và chuỗi cơ chế quan trọng như actin, myosin, sarcomere, TnC, MLCK, dyad, triad, myelin, eo Ranvier, synapse và BBB.
4. Không tự mở rộng chữ viết tắt “RA”, không tự chọn một trong hai giáo trình được nhắc đến, và không thêm tài liệu tham khảo giả.
5. Thêm phần giới hạn nguồn để phân biệt tóm lược tài liệu với xác minh kiến thức chuyên môn độc lập.

## 6. Re-check

- [x] Có cả hai phần mô cơ và mô thần kinh.
- [x] Có cấu tạo cơ vân, các băng sarcomere và cơ chế co/giãn.
- [x] Có bảng so sánh cơ vân, cơ tim và cơ trơn.
- [x] Có nguồn gốc, phân loại, cấu tạo neuron và bao myelin.
- [x] Có synapse, dây thần kinh, chất xám/chất trắng, BBB và sáu loại tế bào đệm.
- [x] Đã giữ các ghi chú/ngoại lệ quan trọng trong nguồn.
- [x] Không thêm trích dẫn, dữ liệu hoặc thông tin thư mục không có căn cứ.
- [x] Đã kiểm tra lại các finding của Critic; không phát hiện lỗi hồi quy sau chỉnh sửa.

## 7. Final audit

**Final Audit execution:** COMPLETED.

| Mandatory check | Result |
|---|---|
| Primary skill đúng và active | PASS |
| Đã truy xuất Registry và toàn văn Skill | PASS |
| Nguồn đầu vào đã được kiểm tra đủ 4 trang | PASS |
| Nội dung bám sát nguồn được cung cấp | PASS |
| Không bịa trích dẫn hoặc dữ liệu | PASS |
| Finding được xử lý hoặc công khai giới hạn | PASS |
| Đã có Critic, Editor, Re-check và Final Auditor như các lượt rà soát riêng | PASS |
| Định dạng theo yêu cầu cụ thể của trường/lớp | NOT SPECIFIED — không có quy định được cung cấp |

### Artifact score — canonical CORE rubric

| Criterion | Score | Rationale |
|---|---:|---|
| Requirement and goal fit | 25/25 | Đáp ứng yêu cầu tạo báo cáo có cấu trúc từ tài liệu nguồn. |
| Accuracy and evidence | 19/20 | Bám nguồn, không bịa nguồn; chưa xác minh độc lập các kiến thức chuyên môn vì test không yêu cầu nghiên cứu ngoài. |
| Completeness and depth | 14/15 | Bao quát các chủ đề chính; độ sâu bị giới hạn bởi bản chất tài liệu tóm tắt. |
| Logic and consistency | 15/15 | Cấu trúc và trình tự nội dung nhất quán. |
| Practical usefulness | 9/10 | Có bảng và phần ghi nhớ phục vụ ôn tập; chưa có rubric môn học để tối ưu theo đề chính thức. |
| Language and presentation | 10/10 | Trình bày rõ ràng, thuật ngữ nhất quán. |
| Format and constraint compliance | 5/5 | Không tự áp đặt định dạng hoặc quy định không được cung cấp. |
| **Total** | **97/100** | |

- **Process conformance:** PASS.
- **Artifact decision:** PASS WITH NOTES.
- **Unresolved Critical/Major issues:** none.
- **Notes:** Đây là báo cáo học thuật tóm lược dựa trên tài liệu người dùng cung cấp, không phải bài thẩm định giáo trình hoặc tài liệu y khoa đã được xác minh độc lập. Nếu dùng làm bài nộp chính thức, cần đối chiếu đề bài, rubric và quy định trình bày của giảng viên.

## 8. Test conclusion

T04 đã được thực hiện với nguồn tài liệu thực tế. Primary skill được chọn đúng là `academic-master`; không cần secondary skill. Quy trình rà soát hoàn tất và artifact đạt **97/100 — PASS WITH NOTES**.

T04 không còn BLOCKED vì thiếu tài liệu nguồn. Kết quả này chỉ xác nhận T04; không thay đổi trạng thái BLOCKED của T09 hoặc trạng thái tổng thể của toàn bộ suite.

---

**Traceability note:** Repository file blob SHA and commit SHA are recorded separately after GitHub creation/verification. The PDF SHA-256 above identifies the exact uploaded source file; it is not a Git blob SHA.
