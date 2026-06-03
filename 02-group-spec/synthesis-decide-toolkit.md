## 1. Gom evidence thành cụm

- "Người dùng thường xem ảnh quán trước khi đọc review"
- "Khó hình dung được 'vibe' thực sự của quán qua text review"
- "Muốn tìm quán phong cách tương tự quán yêu thích nhưng tìm theo keyword trên map không ra"
- "Ảnh trên map quá lộn xộn, khó xác định góc đẹp/không gian tổng thể"

## 2. Viết insight

```text
Người thích đi cafe không chỉ cần danh sách quán gần đây.
Họ cần trải nghiệm thị giác (visual) để xác định 'vibe' (ấm cúng, thiên nhiên, cổ điển) có hợp gu hay không trước,
vì theo quan sát, họ thường lướt ảnh xem không gian trước khi quyết định đọc review hay xem địa chỉ.
```

## 3. Viết opportunity

```text
Cơ hội là dùng AI để phân tích ảnh, trích xuất vibe và tìm kiếm các quán tương đồng,
giúp user nhanh chóng tìm được loạt quán đúng gu chỉ từ một bức ảnh ưng ý,
trong khi vẫn kiểm soát rủi ro gợi ý sai vibe hoặc quán đã đóng cửa/chất lượng tệ.
```

## 4. Chọn build slice

Build slice tốt phải qua 5 câu hỏi:

| Câu hỏi | Đạt khi |
|---|---|
| User cụ thể chưa? | Người thích đi cafe cuối tuần, chú trọng không gian (vibe) để chụp ảnh hoặc thư giãn. |
| Task đủ hẹp chưa? | Show ảnh 1 quán -> user thích -> AI gợi ý 3 quán tương đồng (về vibe/ảnh). Demo trong 3 phút. |
| AI decision rõ chưa? | AI trích xuất 'vibe' từ ảnh và match các quán có vector ảnh/description tương tự. |
| Failure path rõ chưa? | AI gợi ý quán nhìn giống nhưng thực tế không hợp (ví dụ: nhìn giống cổ điển nhưng là quán nhậu), hoặc gợi ý lại quán cũ. |
| Có evidence không? | Có review/ảnh cào từ Google Maps và quan sát hành vi chọn quán thực tế. |

## 5. Quyết định: giữ, giảm scope, hay đổi hướng?

| Tình huống | Quyết định |
|---|---|
| Evidence yếu, user mơ hồ | Dừng build sâu; quay lại research 20 phút. |
| Ý tưởng quá rộng | Giữ domain, cắt xuống một flow (VD: flow lướt ảnh gợi ý). |
| AI không cần thiết | Dùng rule/manual prototype; ghi rõ vì sao không dùng AI sâu. |
| Rủi ro cao | Chọn augmentation (AI gợi ý, user vẫn xem review Google Maps để quyết định chốt). |
| Không demo được trong 6 giờ | Đưa phần scraping/model training vào backlog, dùng mock data/embedding sẵn cho vài chục quán để demo. |

## 6. Câu chốt cuối

```text
Dựa trên hành vi lướt ảnh tìm quán cafe thực tế,
nhóm Coffeeholic sẽ build prototype "gợi ý quán cafe dựa trên độ tương đồng của hình ảnh",
cho người dùng thích khám phá không gian cafe,
để giải quyết vấn đề khó tìm quán cùng vibe bằng keyword truyền thống,
bằng cách dùng AI augment việc match và recommend các quán có ảnh tương tự,
và sẽ test failure path là trường hợp AI gợi ý quán nhìn giống vibe nhưng rating thực tế quá thấp hoặc đã đóng cửa.
```

## 7. Backlog

Những thứ **không build trong Day 06**:

- Scraping dữ liệu real-time toàn bộ Google Maps (sẽ dùng bộ data tĩnh mẫu).
- Flow viết review và rating do user tự nhập.
- Tính năng đăng nhập, profile phức tạp & lịch sử check-in.
