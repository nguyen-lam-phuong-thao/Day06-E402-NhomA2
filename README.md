# Mini Hackathon - AI Cafe Vibe Recommender

## 1. Project overview

Đây là prototype cho bài toán **local discovery / recommendation**, tập trung vào việc giúp user chọn quán cà phê để đi trong ngày mà không phải mở nhiều app và lọc thủ công.

Ý tưởng cốt lõi là:

- User thường **chọn bằng vibe qua hình ảnh trước**.
- Sau đó mới mở Google Maps để kiểm tra **địa chỉ, rating, khoảng cách**.
- Pain không phải thiếu danh sách quán, mà là **khó diễn tả gu quán bằng text** và mất thời gian verify từng quán.

Prototype này dùng AI để **augment bước hiểu visual preference** từ ảnh user chọn, sau đó trả về shortlist quán phù hợp hơn thay vì bắt user tự tìm qua nhiều nguồn.

## 2. Problem statement

User 18-30 tuổi, chủ yếu là sinh viên hoặc nhân viên văn phòng, thường gặp khó khăn khi chọn quán cà phê vì:

- Biết mình thích kiểu không gian nào khi nhìn ảnh.
- Nhưng khó mô tả bằng từ khóa.
- Phải nhảy giữa Instagram, TikTok và Google Maps để chốt quán.

Kết quả là flow chọn quán chậm, rời rạc và dễ mệt mỏi trước khi ra quyết định.

## 3. Proposed solution

Prototype đề xuất một flow ngắn:

1. Hiển thị **3 ảnh đại diện cho 3 kiểu vibe khác nhau**.
2. User chọn **2 ảnh** gần với gu của mình nhất.
3. Hệ thống chuyển mỗi ảnh thành một tín hiệu preference riêng, sau đó **lấy trung bình của 2 lựa chọn** để tạo ra vibe profile chung cho session hiện tại.
4. Hệ thống dùng AI + dataset quán đã chuẩn hóa để trả về **3 quán tương tự**.
5. Mỗi kết quả luôn đi kèm:
   - Tên quán
   - Ảnh chính
   - Rating
   - Địa chỉ
   - Lý do match ngắn

Logic này giúp recommendation bớt cực đoan theo một ảnh đơn lẻ, đồng thời phản ánh gu người dùng linh hoạt hơn, ví dụ vừa thích sáng sủa để làm việc, vừa thích không gian có tính thẩm mỹ để chụp ảnh.

## 4. AI role

Nhóm chọn hướng **Augmentation**.

- AI hỗ trợ nhận diện gu từ ảnh và gợi ý shortlist.
- User vẫn là người quyết định quán cuối cùng.
- Hệ thống không tự động "chốt hộ" vì taste rất chủ quan và dữ liệu hình ảnh dễ gây hiểu sai.

## 5. Prototype scope

Build slice hiện tại tập trung vào một case rõ ràng:

- User đang muốn chọn quán cà phê để đi trong hôm nay.
- Đầu vào là lựa chọn **2 trong 3 ảnh** thay vì text prompt dài.
- Hệ thống dùng **điểm trung bình của 2 ảnh đã chọn** để tính mức độ phù hợp với từng quán trong dataset.
- Đầu ra là shortlist quán có vibe tương đồng trong dataset đã crawl sẵn.

Failure mode cần xử lý ngay trong prototype:

- Kết quả lệch vibe
- Quán quá xa
- Rating thấp
- Kết quả không đủ tin cậy để user ra quyết định

## 6. Core user flows

### Happy path

- User chọn 2 ảnh đại diện cho gu mong muốn.
- Hệ thống kết hợp 2 tín hiệu này thành một profile trung bình.
- Hệ thống trả về 3-5 quán phù hợp, có thông tin đủ để cân nhắc ngay.

### Low-confidence path

- Nếu 2 ảnh vẫn tạo ra tín hiệu chưa đủ rõ hoặc cho ra nhiều quán có điểm gần nhau, hệ thống hỏi thêm 1 bước hẹp để làm rõ nhu cầu.

### Failure path

- Nếu kết quả không hợp gu hoặc không tiện, user có thể:
  - Chọn lại 2 ảnh khác
  - Đổi khu vực
  - Ẩn quán này

### Correction path

- Khi user bấm `không đúng gu`, hệ thống không reset hoàn toàn.
- Correction sẽ được dùng để đổi shortlist trong cùng session.

## 7. Data requirements

Prototype dự kiến dùng dataset mẫu khoảng **30 quán**, với các field chính:

- Tên quán
- Địa chỉ
- Ảnh chính
- Rating
- Category
- AI caption ngắn mô tả vibe
- Vibe score hoặc tag để tính độ gần với profile trung bình từ 2 ảnh người dùng chọn

## 8. Current repository status

Repo này hiện đang phục vụ cho phần **spec và định hướng prototype**.

Nguồn nội dung chính của dự án đang nằm trong thư mục:

`Batch02-Day05-AI-Product-Labs/02-group-spec`

Các file tham chiếu chính:

- `thin-spec-template.md`
- `evidence-pack-template.md`
- `synthesis-decide-toolkit.md`

## 9. Backlog

Các hạng mục tiếp theo để hoàn thiện prototype:

- Chuẩn hóa dataset quán
- Xây dựng logic match vibe từ **2 ảnh đầu vào** và cơ chế lấy điểm trung bình
- Thiết kế UI image-first cho bước chọn quán
- Bổ sung logic filter theo khu vực, rating và khoảng cách
- Tạo flow correction để refine kết quả trong session
- Viết test cases cho happy path, ambiguous path và correction path

## 10. Limitations

Prototype hiện có các giới hạn rõ ràng:

- Evidence hiện thiên về self-observation của nhóm.
- Dataset còn nhỏ và có thể bias theo khu vực thành thị.
- Chất lượng recommendation phụ thuộc mạnh vào chất lượng ảnh và dữ liệu quán.
- Chưa phải sản phẩm production-ready.

## 11. Team

- Huy: Research / evidence
- Thảo: SPEC
- Kiên, Hà, Thảo: Prototype
- Hà: Test / failure path
- Huy: Demo script / repo
