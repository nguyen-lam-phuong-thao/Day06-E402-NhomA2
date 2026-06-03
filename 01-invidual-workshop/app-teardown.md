# 1. Chọn một sản phẩm để dùng thử

| Sản phẩm               | AI Feature                            | Cách truy cập                 |
| ---------------------- | ------------------------------------- | ----------------------------- |
| Vietnam Airlines — NEO | Chatbot hỗ trợ vé, hành lý, khiếu nại | Website/Zalo Vietnam Airlines |

---

# 2. Dùng thử: Promise vs Reality

## Product hứa gì?

NEO được giới thiệu là trợ lý AI hỗ trợ khách hàng tra cứu và giải đáp các vấn đề liên quan đến:

* Chuyến bay
* Hành lý
* Đặt vé
* Dịch vụ hành khách

## User nào được hứa sẽ được giúp?

* Hành khách chuẩn bị bay
* Người cần tra cứu thông tin dịch vụ của Vietnam Airlines

## Kỳ vọng AI làm được task nào?

Khi người dùng hỏi về một hành trình cụ thể:

* Xác nhận hành trình có tồn tại hay không
* Nếu tồn tại → trả lời chính sách liên quan
* Nếu không tồn tại → thông báo và đề xuất lựa chọn khác

## Input đã thử

> Chuyến bay từ Cát Bi đến Vân Đồn có quy định hành lý và suất ăn chay không?

## Điểm gãy quan sát được

NEO trả lời trực tiếp về:

* Quy định hành lý
* Suất ăn chay

mà không xác minh tuyến bay **Cát Bi → Vân Đồn** có tồn tại trong mạng bay của Vietnam Airlines hay không.

## Evidence

### Prompt

> Chuyến bay từ Cát Bi đến Vân Đồn có quy định hành lý và suất ăn chay không?

### Output

NEO trả lời quy định hành lý và suất ăn như đối với một chuyến bay hợp lệ.

### Observation

* Không có bước xác thực tuyến bay.
* Không có cảnh báo rằng tuyến bay không tồn tại.
* Không có đề xuất tuyến thay thế.
* User có thể hiểu nhầm rằng Vietnam Airlines đang khai thác tuyến này.

---

# 3. Vẽ 4 Paths

## Happy Path

### User

> Chuyến bay Hà Nội → TP.HCM có hành lý bao nhiêu kg?

### AI

* Nhận diện tuyến bay hợp lệ.
* Trả lời chính sách hành lý.

### Kết quả

Người dùng nhận được thông tin mong muốn.

---

## Low-confidence Path

### User

> Chuyến bay từ Cát Bi đến Vân Đồn có hành lý thế nào?

### Hiện trạng

* AI không kiểm tra tuyến bay.
* AI vẫn trả lời.

### Nên có

* Kiểm tra cơ sở dữ liệu chuyến bay.
* Phát hiện tuyến không tồn tại.
* Hỏi lại hoặc đề xuất tuyến thay thế.

### Ví dụ mong muốn

> Tôi chưa tìm thấy đường bay Vietnam Airlines giữa Cát Bi và Vân Đồn. Bạn muốn tra cứu tuyến khác hoặc tìm chuyến bay gần nhất không?

---

## Failure Path

### AI

* Giả định tuyến bay tồn tại.
* Sinh câu trả lời dựa trên kiến thức chung.

### User

* Tin rằng tuyến bay tồn tại.
* Có thể tiếp tục tìm cách đặt vé.

### Impact

* Gây hiểu nhầm về mạng đường bay của hãng.
* Giảm độ tin cậy của chatbot.

---

## Correction Path

### User

> Nhưng Vietnam Airlines đâu có chuyến bay này?

### Hiện trạng

* Không có dấu hiệu correction được ghi nhận.
* Không có cơ chế feedback hoặc escalation.

### Kết quả

Correction biến mất khỏi hệ thống và không tạo ra hành động xử lý tiếp theo.

---

# 4. Viết Finding Thành Quyết Định Product

## Finding

Khi user hỏi về một hành trình không tồn tại,

AI trả lời dựa trên kiến thức chung về hành lý và suất ăn thay vì xác minh thực thể chuyến bay,hậu quả là user có thể hiểu nhầm rằng Vietnam Airlines đang khai thác tuyến bay đó.

## Layer

* Intent Recognition
* Data / Tool Integration
* UX Recovery

## Product Decision

Bổ sung bước xác thực tuyến bay trước khi trả lời các câu hỏi liên quan đến:

* Hành lý
* Suất ăn
* Giờ bay
* Đặt vé
* Đổi vé

Nếu không tìm thấy chuyến bay:

* Thông báo rõ ràng cho người dùng
* Đề xuất tuyến thay thế
* Hoặc chuyển sang công cụ tìm kiếm chuyến bay

## Requirement

```text
IF query contains route-specific information
THEN validate route existence before answering service-related questions

IF route not found
THEN enter low-confidence flow instead of generating answer
```

---

# 5. Sketch As-Is / To-Be

## As-Is

```text
User
  |
  v
Hỏi tuyến Cát Bi -> Vân Đồn
  |
  v
NEO nhận diện:
"Hỏi về hành lý + suất ăn"
  |
  v
Sinh câu trả lời chung
  |
  v
User tưởng tuyến tồn tại
```

### Điểm gãy

Không validate thực thể chuyến bay.

---

## To-Be

```text
User
  |
  v
Hỏi tuyến Cát Bi -> Vân Đồn
  |
  v
NER Route Extraction
  |
  v
Flight Route Validation
  |
  +------ Route tồn tại ------+
  |                           |
  v                           |
Trả lời hành lý + suất ăn     |
                              |
  +---- Route không tồn tại --+
                              |
                              v
Low-confidence Flow
                              |
                              v
Thông báo không tìm thấy tuyến
                              |
                              v
Đề xuất tuyến gần nhất
hoặc chuyển sang tra cứu chuyến bay
```
