# Template — Evidence Pack

Nộp kèm thin SPEC cuối Day 05.

## 1. Nhóm và track

**Tên nhóm:** Coffeeholic
**Track:** Khám phá & Gợi ý địa điểm (Discovery)  
**Product/app đã chọn:** Ứng dụng tìm quán cafe yêu thích qua độ tương đồng của ảnh và vibe (Tinder for Cafe).  
**Build slice đang nghĩ:** Người dùng xem ảnh 1 quán, nhấn "Thích" và AI sẽ tự động trả về top 3 quán có hình ảnh/không gian tương tự nhất.  

## 2. Self-use evidence

Nhóm tự dùng app/workflow (Google Maps, Facebook Group) và ghi lại điểm gãy.

| Observation | Screenshot/link | Path liên quan | Điều học được |
|---|---|---|---|
| Lên Google Maps gõ "cafe yên tĩnh, cổ điển" ra toàn kết quả sai hoặc chỉ dựa vào tên quán có chữ "yên tĩnh". | (Hình ảnh kết quả search trên map) | Failure | Tìm kiếm bằng từ khoá text thông thường không hiệu quả với những nhu cầu mang tính cảm nhận (vibe). |
| Tìm được 1 quán đẹp trên Tiktok, nhưng muốn tìm các quán tương tự ở gần nhà thì không biết search bằng từ khoá gì. | (Video Tiktok review cafe) | Low-confidence | User cần một hệ thống "Gợi ý tương tự (Similar Items)" dựa trên hình ảnh thay vì text. |

## 3. User / review / social evidence

Nguồn có thể là review App Store/Play, group, comment, phỏng vấn nhanh, hoặc nguồn public khác.

| Quote / review / observation | Nguồn | User là ai? | Pain/failure mode |
|---|---|---|---|
| "Quán này chụp hình nhìn vintage lắm nhưng ra ngoài ồn ào, không giống ảnh" | Comment hội review cafe Facebook | Bạn trẻ thích check-in, chụp ảnh. | Quán có ảnh đẹp nhưng thực tế không đúng Vibe. Cần cơ chế hiển thị rating Google đính kèm để double-check. |
| Lướt lưu hàng chục ảnh quán cafe trên Instagram/Pinterest nhưng cuối cùng không đi vì lười đọc thông tin rời rạc. | Phỏng vấn trực tiếp | Dân văn phòng thích đi cafe cuối tuần. | Lười đọc text, thích ra quyết định bằng thị giác nhanh (swipe/thả tim ảnh). |


## 4. Competitor / analog evidence

| App / mô hình tham khảo | Họ xử lý task này thế nào? | Pattern học được | Có áp dụng trong 1 ngày không? |
|---|---|---|---|
| **Pinterest** | Có nút "Tìm kiếm hình ảnh tương tự" (Visual Search) rất mạnh. | Dùng Computer Vision (AI) trích xuất đặc trưng ảnh để tìm ảnh giống. | CÓ. Dùng mô hình CLIP của OpenAI để lấy vector ảnh. |
| **Tinder** | Quẹt trái/phải (Swipe) cực kỳ gây nghiện và ra quyết định nhanh. | Tinh giản UI, chỉ hiển thị 1 ảnh to ở giữa màn hình. Bắt user ra quyết định Thích/Bỏ ngay lập tức. | CÓ. UI 1 thẻ ảnh to + 2 nút bấm (X/Tim) rất phù hợp làm MVP. |

## 5. Evidence -> Insight

```text
Evidence nổi bật nhất:
Hành vi lướt lưu ảnh trên mxh nhưng khó chuyển đổi thành quyết định đi thực tế vì mất công tìm kiếm lại trên Google Maps.

Insight:
User không chỉ gặp khó ở [việc gõ từ khoá tìm kiếm trên Maps].
Thật ra họ cần [công cụ hỗ trợ tìm quán dựa trên cảm nhận không gian (vibe) thông qua thị giác], vì chữ viết không thể diễn tả hết được cái "gu" của 1 quán.

Opportunity:
AI có thể giúp bằng cách [augment việc phân tích độ tương đồng giữa các bức ảnh quán bằng mô hình thị giác máy tính], giúp user chỉ cần "Thích 1 ảnh" là tự động list ra danh sách quán đúng gu mà không cần nghĩ keyword.
```

## 6. Evidence đổi SPEC như thế nào?

- [ ] Đổi user chính.
- [x] Đổi pain statement.
- [x] Đổi build slice.
- [ ] Đổi Auto/Aug decision.
- [ ] Đổi 4 paths.
- [x] Đổi failure mode.
- [ ] Đổi owner/test plan.


```text
Trước evidence, nhóm định: Làm 1 chatbot, user nhập text "Tôi muốn đi quán cổ điển", bot trả list.
Sau evidence, nhóm đổi thành: Dùng UI hiển thị ảnh (Visual-first), bắt user chọn ảnh thích, rồi dùng AI AI(CLIP) match ảnh tương tự.
Lý do: User lười gõ và lười đọc, họ có xu hướng chọn theo không gian (hình ảnh) nhiều hơn là chữ.
```
