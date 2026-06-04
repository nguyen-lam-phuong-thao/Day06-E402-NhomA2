# Template — Thin SPEC Cuối Day 05

Thin SPEC không phải PRD đầy đủ. Đây là bản cam kết đủ rõ để sáng Day 06 nhóm build ngay.

## 1. Track, product/app và user

**Track:** Local discovery / recommendation  
**Product/app thật:** workflow tìm quán qua Google Maps + Instagram/TikTok  
**User cụ thể:** sinh viên hoặc nhân viên văn phòng 18-30 tuổi, đang muốn chọn quán cà phê để đi trong hôm nay nhưng chưa biết nên đi đâu.
**Nhóm có phải user thật không? Nếu không, khác ở đâu?** Có, khá sát. Tuy vậy nhóm có bias về hành vi tìm quán ở khu vực thành thị và nhóm bạn trẻ, nên cần check thêm user ngoài nhóm nếu muốn mở rộng.  

## 2. Evidence summary

| Evidence | Nguồn | User/pain nói lên điều gì? | SPEC phải đổi gì? |
|---|---|---|---|
| Khi tự tìm quán, flow thường là xem ảnh trước, rồi mới qua Google Maps kiểm tra địa chỉ, rating, khoảng cách. | Self-use observation của nhóm | User đang chọn bằng "vibe" trước, nhưng phải nhảy nhiều app để validate. | Prototype phải là image-first, nhưng kết quả phải luôn đi kèm rating + địa chỉ + khoảng cách. |
| User khó mô tả gu quán bằng text kiểu "tôi thích quán thế nào", nhưng lại chọn rất nhanh khi nhìn ảnh. | Self-use observation của nhóm | Pain chính không phải thiếu danh sách quán, mà là khó diễn tả preference đầu vào. | Bỏ text prompt ở bước đầu. Dùng 4 ảnh đại diện cho 4 category để user chọn nhanh. |
| Ảnh đẹp một mình là chưa đủ; nếu quán xa, rating thấp hoặc không rõ nguồn thì user không dám tin recommendation. | Observation từ workflow dùng Google Maps; hiện vẫn cần verify thêm ngoài nhóm | Risk lớn nhất là AI recommend đúng vibe nhưng sai về tính tiện dụng hoặc độ tin cậy. | Recommendation phải bị ràng buộc bởi dữ liệu có cấu trúc: khu vực, rating tối thiểu, link nguồn ảnh/quán. |

## 3. Pain statement

```text
User đang gặp khó ở bước chọn quán cà phê để đi, vì họ biết mình thích "vibe" nào qua hình ảnh nhưng khó diễn tả bằng từ khóa, dẫn tới phải mở nhiều app và xem từng quán thủ công trước khi chốt.
Bằng chứng chính là self-observation: nhóm đều có flow xem ảnh trước rồi mới kiểm tra Google Maps từng quán.
```

## 4. Build slice

```text
Cho user đang chọn quán cà phê để đi trong hôm nay, prototype sẽ dùng AI để augment bước hiểu visual preference từ lựa chọn ảnh đầu vào, tạo ra shortlist 3-5 quán cùng gu trong dataset đã crawl sẵn,
và xử lý failure mode "chọn xong nhưng kết quả không đúng gu / quá xa / rating thấp" bằng filter cứng + nút chọn lại + đổi khu vực.
```

## 5. Auto/Aug decision

Chọn một:

- [x] **Augmentation:** AI gợi ý/draft/phân loại, user quyết cuối.
- [ ] **Conditional automation:** AI tự làm trong case hẹp; case mơ hồ/rủi ro chuyển người.
- [ ] **Automation:** AI tự quyết và tự hành động.

**Lý do chọn:** User vẫn là người quyết định quán sẽ đi. AI chỉ nên giúp rút ngắn bước tìm và lọc, không nên tự "chốt hộ" vì taste rất chủ quan và dữ liệu ảnh dễ gây hiểu sai.  
**Human role:** decider + rescuer  

## 6. Four paths

| Path | Prototype phải thể hiện gì? |
|---|---|
| Happy | User thấy 4 ảnh đại diện cho 4 category khác nhau, chọn 1 ảnh, rồi nhận được 3-5 quán có vibe tương tự kèm tên, ảnh, rating Google Maps, địa chỉ, khoảng cách và lý do match ngắn. |
| Low-confidence | Nếu tín hiệu từ 1 ảnh chưa đủ rõ hoặc nhiều quán có điểm match ngang nhau, hệ thống phải hỏi thêm 1 bước hẹp như `thích yên tĩnh hay đông vui`, `đi làm việc hay chụp ảnh`, hoặc `chọn khu vực muốn đi`. |
| Failure | Nếu AI/retrieval trả quán lệch vibe, quá xa hoặc rating thấp, user phải thấy rõ vì sao quán đó được gợi ý và có cách thoát nhanh như `đổi ảnh`, `đổi khu vực`, `ẩn quán này`. |
| Correction | Khi user bấm `không đúng gu`, hệ thống không chỉ reset toàn bộ mà phải dùng correction đó để đổi shortlist trong session hiện tại, ví dụ bỏ category hoặc bỏ những quán có style tương tự. |

## 7. Failure mode nguy hiểm nhất

```text
Nếu user chọn một ảnh đẹp theo cảm tính, AI có thể recommend các quán "trông giống" nhưng thực ra quá xa, rating thấp hoặc không đúng mục đích đi quán, hậu quả là user mất niềm tin và thấy sản phẩm chỉ là random ảnh đẹp chứ không giúp ra quyết định.
Prototype sẽ xử lý bằng filter cứng trước khi recommend: chỉ lấy quán trong dataset đã chuẩn hóa, có rating tối thiểu, có địa chỉ/khoảng cách rõ ràng, và nếu match score thấp thì hỏi thêm 1 câu thay vì trả kết quả luôn.
Owner kiểm thử path này là TBD.
```

## 8. Owner plan cho sáng Day 06

| Thành viên | Việc phụ trách | Bằng chứng cần có trong repo |
|---|---|---|
| Huy | Research / evidence | 5 self-observations, 3 nguồn ngoài nhóm hoặc ghi rõ giả định nào chưa verify |
| Thảo | SPEC | Thin SPEC đã chốt user, build slice, 4 paths, failure mode |
| Kiên, Hà, Thảo | Prototype | Dataset mẫu 20-40 quán với các field: tên, địa chỉ, lat/lng hoặc district, ảnh chính, rating, review count, category, caption AI 20 chữ |
| Hà | Test / failure path | 3 test cases: chọn đúng gu, chọn mơ hồ, correction `không đúng gu` |
| Huy | Demo script / repo | Flow demo 3-5 phút + README nói rõ backlog và giới hạn của prototype |


